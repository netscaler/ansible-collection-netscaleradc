# -*- coding: utf-8 -*-

# Copyright (c) 2026 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

"""Prune orphan example playbooks from the collection ``examples/`` directory.

The example generator emits YAMLs for more NITRO resources than it generates
modules for (binding-only globals, namespaces, read-only or dropped resources).
Those "orphans" reference a ``netscaler.adc.<resource>`` module that does not
exist, so ``ansible-lint`` / ``--syntax-check`` over ``examples/`` fails with
"couldn't resolve module/action".

An example is pruned when it references a ``netscaler.adc.<module>`` for which no
``plugins/modules/<module>.py`` exists (and which is not an action group).
Hand-written playbooks that use only real modules are always kept. Run after a
refresh (``make prune_examples``), or with ``--check`` in CI. See metadatarefresh.md.
"""

import argparse
import os
import re
import sys

# netscaler.adc.<name>, optionally prefixed by "group/" for a module_defaults
# action-group reference. <name> is a module/resource/group identifier.
FQCN_RE = re.compile(r"(group/)?netscaler\.adc\.([a-z0-9_]+)")


def collection_root():
    """Return the collection root (this file lives in ``<root>/tools/``)."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def existing_modules(root):
    """Set of module names that have a ``plugins/modules/<name>.py`` file."""
    mod_dir = os.path.join(root, "plugins", "modules")
    return {
        f[:-3] for f in os.listdir(mod_dir) if f.endswith(".py") and f != "__init__.py"
    }


def action_group_names(root):
    """Top-level action-group names declared under ``action_groups:`` in
    meta/runtime.yml (referenced in playbooks as ``group/netscaler.adc.<name>``).

    Parsed with a tiny indentation scanner to avoid a hard PyYAML dependency for
    a Makefile/CI helper.
    """
    runtime = os.path.join(root, "meta", "runtime.yml")
    groups = set()
    if not os.path.exists(runtime):
        return groups
    in_block = False
    with open(runtime, encoding="utf-8") as fh:
        for line in fh:
            if re.match(r"^action_groups:\s*$", line):
                in_block = True
                continue
            if in_block:
                if re.match(r"^\S", line):  # dedent to another top-level key
                    break
                m = re.match(r"^  ([A-Za-z0-9_]+):\s*$", line)  # 2-space key
                if m:
                    groups.add(m.group(1))
    return groups


def find_orphans(root):
    """Return (orphans, reasons): example files referencing a non-existent module."""
    examples_dir = os.path.join(root, "examples")
    modules = existing_modules(root)
    groups = action_group_names(root)
    orphans = []
    reasons = {}
    for name in sorted(os.listdir(examples_dir)):
        if not (name.endswith(".yaml") or name.endswith(".yml")):
            continue
        path = os.path.join(examples_dir, name)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        missing = set()
        for is_group, ref in FQCN_RE.findall(text):
            if is_group:
                continue  # action-group reference, resolved via meta/runtime.yml
            if ref in modules or ref in groups:
                continue
            missing.add(ref)
        if missing:
            orphans.append(name)
            reasons[name] = sorted(missing)
    return orphans, reasons


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not delete; exit non-zero if any orphan example exists (for CI)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="list orphans that would be deleted, but do not delete them",
    )
    args = parser.parse_args()

    root = collection_root()
    orphans, reasons = find_orphans(root)

    if not orphans:
        print("prune_examples: no orphan examples found.")
        return 0

    for name in orphans:
        print(
            "orphan: examples/%s -> references non-existent module(s): %s"
            % (name, ", ".join(reasons[name]))
        )

    if args.check:
        print(
            "prune_examples: %d orphan example(s) found (run `make prune_examples`)."
            % len(orphans)
        )
        return 1

    if args.dry_run:
        print("prune_examples: %d orphan(s) would be deleted (dry-run)." % len(orphans))
        return 0

    deleted = 0
    for name in orphans:
        path = os.path.join(root, "examples", name)
        try:
            os.remove(path)
            deleted += 1
        except OSError as exc:  # warn and continue; do not abort the refresh
            print("prune_examples: WARNING could not delete %s: %s" % (path, exc))
    print("prune_examples: deleted %d orphan example(s)." % deleted)
    return 0


if __name__ == "__main__":
    sys.exit(main())
