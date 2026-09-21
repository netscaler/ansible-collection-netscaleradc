# -*- coding: utf-8 -*-

# Copyright (c) 2026 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

"""Fix the ``state`` doc/spec mismatch for operational-utility modules.

ping/ping6/traceroute/traceroute6 store no config -- they only run a NITRO
action. At runtime ``get_valid_desired_states`` (common.py) adds ``present`` for
them, so their argument_spec is ``state: choices=['present']``. But the generator
emits ``state: choices: []`` in their DOCUMENTATION, and ansible-core >= 2.18's
``validate-modules:doc-choices-do-not-match-spec`` fails on the mismatch.

This rewrites those modules' doc ``state.choices`` to ``[present]`` so doc and
spec agree. Idempotent; run by ``make refresh_metadata`` (target ``fix_docs``).
The permanent fix belongs in the generator. See metadatarefresh.md.
"""

import os
import re
import sys

EMPTY = "  state:\n    choices: []\n"
FIXED = "  state:\n    choices:\n      - present\n"


def collection_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def operational_resources(root):
    """Read OPERATIONAL_UTILITY_RESOURCES from constants.py (single source of truth)."""
    const = os.path.join(root, "plugins", "module_utils", "constants.py")
    with open(const, encoding="utf-8") as fh:
        text = fh.read()
    m = re.search(r"OPERATIONAL_UTILITY_RESOURCES\s*=\s*\{([^}]*)\}", text)
    if not m:
        return []
    return re.findall(r"[\"']([a-z0-9_]+)[\"']", m.group(1))


def main():
    root = collection_root()
    fixed = []
    for res in operational_resources(root):
        path = os.path.join(root, "plugins", "modules", "%s.py" % res)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        if EMPTY in text:
            text = text.replace(EMPTY, FIXED, 1)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
            fixed.append(res)
    if fixed:
        print(
            "fix_operational_state_docs: set state.choices=[present] for: %s"
            % ", ".join(fixed)
        )
    else:
        print("fix_operational_state_docs: nothing to fix.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
