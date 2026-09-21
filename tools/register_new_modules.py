#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2026 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

"""Register brand-new NITRO modules after a metadata refresh.

A refresh drops freshly generated ``plugins/modules/*.py`` into the collection.
The generator doesn't apply two collection-packaging conventions, so this tool
does them mechanically:

1. **Action group** -- add each new module (alphabetically) under
   ``action_groups: default_args:`` in ``meta/runtime.yml`` (enables
   ``module_defaults``).
2. **License waiver** -- add a ``missing-gplv3-license`` ignore line for each new
   module to every ``tests/sanity/ignore-2.XX.txt`` (the collection is MIT).

"New" = a module on disk but not tracked in git HEAD -- exactly what the refresh
just added. Detection is git-based (not "missing from default_args") because a
few real modules are intentionally excluded from the action group
(``routerdynamicrouting_info``, ``nslaslicense_offline``). Override with
``--modules name1 name2`` outside git.

Both edits are idempotent and insert only new lines (existing lines unchanged),
so the diff is minimal. Use ``--check`` in CI, ``--dry-run`` to preview. It does
NOT bump ``galaxy.yml``/``CHANGELOG.md`` or create a new ansible-core lane's
ignore file, and it adds *every* new module to the action group -- delete the line
by hand for any operational/``*_info`` module that should be excluded.
See metadatarefresh.md.
"""

import argparse
import glob
import os
import re
import shutil
import subprocess  # nosec B404 - only used to run a fixed git command (list args, no shell)
import sys

WAIVER = "validate-modules:missing-gplv3-license # We use MIT license"

# meta/runtime.yml list item, e.g. "    - lbvserver"
_ITEM_RE = re.compile(r"^(\s*)-\s+([A-Za-z0-9_]+)\s*$")


def collection_root():
    """Return the collection root (this file lives in ``<root>/tools/``)."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def disk_modules(root):
    """Set of module names that have a ``plugins/modules/<name>.py`` file."""
    mod_dir = os.path.join(root, "plugins", "modules")
    return {
        f[:-3] for f in os.listdir(mod_dir) if f.endswith(".py") and f != "__init__.py"
    }


def tracked_modules(root):
    """Module names tracked in git HEAD, or ``None`` if git/HEAD is unavailable."""
    git = shutil.which("git")  # absolute path (avoids Bandit B607 partial-path)
    if git is None:
        return None
    try:
        out = subprocess.run(  # nosec B603 - fixed argument list, no shell, no untrusted input
            [git, "-C", root, "ls-tree", "-r", "--name-only", "HEAD", "--", "plugins/modules/"],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except (subprocess.CalledProcessError, OSError):
        return None
    names = set()
    for line in out.splitlines():
        base = os.path.basename(line)
        if base.endswith(".py") and base != "__init__.py":
            names.add(base[:-3])
    return names


def detect_new_modules(root):
    """New modules = on disk but not tracked in HEAD. Raises if git is unavailable."""
    tracked = tracked_modules(root)
    if tracked is None:
        raise RuntimeError(
            "cannot detect new modules: not a git repo (or no HEAD). "
            "Pass the module names explicitly with --modules."
        )
    return sorted(disk_modules(root) - tracked)


def _read_lines(path):
    with open(path, encoding="utf-8") as fh:
        return fh.readlines()


def _write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as fh:
        fh.writelines(lines)


def _merge_sorted(existing_lines, existing_keys, additions):
    """Insert each ``(key, line)`` from ``additions`` before the first existing
    line whose key is byte-greater; append leftovers. Existing lines are kept
    verbatim so the diff is only the inserted lines. Returns the new line list."""
    remaining = sorted(additions)  # (key, line) tuples, byte order on key
    result = []
    ri = 0
    for line, key in zip(existing_lines, existing_keys):
        while ri < len(remaining) and remaining[ri][0] < key:
            result.append(remaining[ri][1])
            ri += 1
        result.append(line)
    if ri < len(remaining) and result and not result[-1].endswith("\n"):
        result[-1] += "\n"
    while ri < len(remaining):
        result.append(remaining[ri][1])
        ri += 1
    return result


def _find_default_args_block(lines):
    """Return (start, end, indent, names): the slice [start:end) of contiguous list
    items under ``default_args:`` in meta/runtime.yml, their indent, and names."""
    start = None
    for i, line in enumerate(lines):
        if re.match(r"^\s*default_args:\s*$", line):
            start = i + 1
            break
    if start is None:
        raise RuntimeError("could not find 'default_args:' in meta/runtime.yml")
    end = start
    indent = None
    names = []
    for i in range(start, len(lines)):
        m = _ITEM_RE.match(lines[i])
        if not m:
            break
        if indent is None:
            indent = m.group(1)
        names.append(m.group(2))
        end = i + 1
    if indent is None:
        raise RuntimeError("found 'default_args:' but no list items beneath it")
    return start, end, indent, names


def apply_runtime(root, modules, write=True):
    """Add ``modules`` to default_args in meta/runtime.yml. Returns names added."""
    path = os.path.join(root, "meta", "runtime.yml")
    lines = _read_lines(path)
    start, end, indent, names = _find_default_args_block(lines)
    present = set(names)
    to_add = [m for m in modules if m not in present]
    if to_add:
        block = lines[start:end]
        additions = [(m, "%s- %s\n" % (indent, m)) for m in to_add]
        merged = _merge_sorted(block, names, additions)
        new_lines = lines[:start] + merged + lines[end:]
        if write:
            _write_lines(path, new_lines)
    return sorted(to_add)


def _ignore_first_token(line):
    parts = line.split()
    return parts[0] if parts else line


def _ignore_module_names(lines):
    names = set()
    for line in lines:
        tok = _ignore_first_token(line)
        if tok.startswith("plugins/modules/") and tok.endswith(".py"):
            names.add(tok[len("plugins/modules/"):-3])
    return names


def apply_ignore(path, modules, write=True):
    """Add ``missing-gplv3-license`` waivers for ``modules`` to one ignore file.
    Returns names added."""
    lines = _read_lines(path)
    present = _ignore_module_names(lines)
    to_add = [m for m in modules if m not in present]
    if to_add:
        keys = [_ignore_first_token(l) for l in lines]
        additions = [
            ("plugins/modules/%s.py" % m, "plugins/modules/%s.py %s\n" % (m, WAIVER))
            for m in to_add
        ]
        merged = _merge_sorted(lines, keys, additions)
        if write:
            _write_lines(path, merged)
    return sorted(to_add)


def ignore_files(root):
    return sorted(glob.glob(os.path.join(root, "tests", "sanity", "ignore-*.txt")))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--modules",
        nargs="+",
        metavar="NAME",
        help="module names to register (bare, no .py); default: git-detect new modules",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write; exit non-zero if any new module is unregistered (for CI)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report what would change, but do not write",
    )
    args = parser.parse_args()

    root = collection_root()

    if args.modules:
        modules = sorted(set(args.modules))
    else:
        try:
            modules = detect_new_modules(root)
        except RuntimeError as exc:
            print("register_new_modules: ERROR %s" % exc, file=sys.stderr)
            return 2

    if not modules:
        print("register_new_modules: no new modules to register.")
        return 0

    print("register_new_modules: %d candidate module(s): %s" % (len(modules), ", ".join(modules)))

    write = not (args.check or args.dry_run)
    changed = False

    added = apply_runtime(root, modules, write=write)
    if added:
        changed = True
        print("  meta/runtime.yml (default_args): + %s" % ", ".join(added))
    else:
        print("  meta/runtime.yml (default_args): already up to date")

    for path in ignore_files(root):
        rel = os.path.relpath(path, root)
        added = apply_ignore(path, modules, write=write)
        if added:
            changed = True
            print("  %s: + %s" % (rel, ", ".join(added)))
        else:
            print("  %s: already up to date" % rel)

    if args.check:
        if changed:
            print("register_new_modules: unregistered module(s) found (run `make register_modules`).")
            return 1
        print("register_new_modules: all modules registered.")
        return 0

    if args.dry_run:
        print("register_new_modules: dry-run, nothing written.")
        return 0

    if changed:
        print("register_new_modules: done. Remember (manual): bump galaxy.yml version + CHANGELOG.md;")
        print("  review that no new module should be excluded from the default_args action group.")
    else:
        print("register_new_modules: nothing to do; everything already registered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
