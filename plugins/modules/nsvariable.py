#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: nsvariable
short_description: Configuration for variable resource.
description: Configuration for variable resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  comment:
    type: str
    description:
      - Comments associated with this variable.
  expires:
    type: int
    description:
      - Value expiration in seconds. If the value is not referenced within the expiration
        period it will be deleted. 0 (the default) means no expiration.
  iffull:
    type: str
    choices:
      - undef
      - lru
    description:
      - 'Action to perform if an assignment to a map exceeds its configured max-entries:'
      - '   C(lru) - (default) reuse the least recently used entry in the map.'
      - '   C(undef) - force the assignment to return an undefined (Undef) result
        to the policy executing the assignment.'
  ifnovalue:
    type: str
    choices:
      - undef
      - init
    description:
      - Action to perform if on a variable reference in an expression if the variable
        is single-valued and uninitialized
      - 'or if the variable is a map and there is no value for the specified key:'
      - '   C(init) - (default) initialize the single-value variable, or create a
        map entry for the key and the initial value,'
      - using the -C(init) value or its default.
      - '   C(undef) - force the expression evaluation to return an undefined (Undef)
        result to the policy executing the expression.'
  ifvaluetoobig:
    type: str
    choices:
      - undef
      - truncate
    description:
      - Action to perform if an value is assigned to a text variable that exceeds
        its configured max-size,
      - 'or if a key is used that exceeds its configured max-size:'
      - '   C(truncate) - (default) C(truncate) the text string to the first max-size
        bytes and proceed.'
      - '   C(undef) - force the assignment or expression evaluation to return an
        undefined (Undef) result to the policy executing the assignment or expression.'
  init:
    type: str
    description:
      - 'Initialization value for this variable, to which a singleton variable or
        map entry will be set if it is referenced before an assignment action has
        assigned it a value. If the singleton variable or map entry already has been
        assigned a value, setting this parameter will have no effect on that variable
        value. Default: 0 for ulong, NULL for text'
  name:
    type: str
    description:
      - 'Variable name.  This follows the same syntax rules as other expression entity
        names:'
      - '   It must begin with an alpha character (A-Z or a-z) or an underscore (_).'
      - '   The rest of the characters must be alpha, numeric (0-9) or underscores.'
      - '   It cannot be re or xp (reserved for regular and XPath expressions).'
      - '   It cannot be an expression reserved word (e.g. SYS or HTTP).'
      - '   It cannot be used for an existing expression object (HTTP callout, patset,
        dataset, stringmap, or named expression).'
  scope:
    type: str
    choices:
      - global
      - transaction
    description:
      - 'Scope of the variable:'
      - '   C(global) - (default) one set of values visible across all Packet Engines
        on a standalone Citrix ADC, an HA pair, or all nodes of a cluster'
      - '   C(transaction) - one value for each request-response C(transaction) (singleton
        variables only; no expiration)'
  type:
    type: str
    description:
      - 'Specification of the variable type; one of the following:'
      - '   ulong - singleton variable with an unsigned 64-bit value.'
      - '   text(value-max-size) - singleton variable with a text string value.'
      - '   map(text(key-max-size),ulong,max-entries) - map of text string keys to
        unsigned 64-bit values.'
      - '   map(text(key-max-size),text(value-max-size),max-entries) - map of text
        string keys to text string values.'
      - where
      - '   value-max-size is a positive integer that is the maximum number of bytes
        in a text string value.'
      - '   key-max-size is a positive integer that is the maximum number of bytes
        in a text string key.'
      - '   max-entries is a positive integer that is the maximum number of entries
        in a map variable.'
      - '      For a global singleton text variable, value-max-size <= 64000.'
      - '      For a global map with ulong values, key-max-size <= 64000.'
      - '      For a global map with text values,  key-max-size + value-max-size <=
        64000.'
      - '   max-entries is a positive integer that is the maximum number of entries
        in a map variable. This has a theoretical maximum of 2^64-1, but in actual
        use will be much smaller, considering the memory available for use by the
        map.'
      - 'Example:'
      - '   map(text(10),text(20),100) specifies a map of text string keys (max size
        10 bytes) to text string values (max size 20 bytes), with 100 max entries.'
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
diff:
  description: Dictionary of before and after changes
  returned: always
  type: dict
  sample: {'before': {'key1': 'xyz'}, 'after': {'key2': 'pqr'}, 'prepared': 'changes
      done'}
diff_list:
  description: List of differences between the actual configured object and the configuration
    specified in the module
  returned: when changed
  type: list
  sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class
      'str'>) PQR"]
failed:
  description: Indicates if the module failed or not
  returned: always
  type: bool
  sample: false
loglines:
  description: list of logged messages by the module
  returned: always
  type: list
  sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
