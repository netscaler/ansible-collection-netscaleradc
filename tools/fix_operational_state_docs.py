#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2026 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

"""Fix the ``state`` doc/spec mismatch for operational-utility modules.

Why this exists
---------------
ping/ping6/traceroute/traceroute6 store no config; they only run a synchronous
NITRO action ("Ping", "Traceroute", ...). At runtime ``get_valid_desired_states``
deliberately adds ``present`` for these resources (common.py) so their
``state`` argument accepts its own default, giving an argument_spec of
``state: choices=['present']``.

The metadata generator, however, emits ``state: choices: []`` in the generated
DOCUMENTATION for these modules (it computes state choices only from
add/update-style operations, which these resources lack). ansible-core >= 2.18's
``validate-modules:doc-choices-do-not-match-spec`` then fails because the doc
(``[]``) disagrees with the spec (``['present']``).

Every OTHER module is fine: config/binding modules get non-empty choices in both
doc and spec, and the ~30 pure operational resources (reboot, nstrace, *session,
convert, ...) have an empty choices list in *both* doc and spec, so they match.

This fixup rewrites just the operational-utility modules' ``state.choices`` to
``[present]`` so doc and spec agree. It is idempotent and is run automatically by
``make refresh``. The permanent fix belongs in the generator (make its doc-side
state-choices computation match the runtime); until then this keeps refreshes
seamless. See metadatarefresh.md.
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
