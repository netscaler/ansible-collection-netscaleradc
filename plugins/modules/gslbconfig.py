#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: gslbconfig
short_description: Configuration for gslb config resource.
description: Configuration for gslb config resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  command:
    description:
      - Run the specified command on the master node and then on all the slave nodes.
        You cannot use this option with the force sync and preview options.
    type: str
  debug:
    description:
      - Generate verbose output when synchronizing the GSLB sites. The Debug option
        generates more verbose output than the sync gslb config command in which the
        option is not used, and is useful for analyzing synchronization issues.
    type: bool
  forcesync:
    description:
      - 'Force synchronization of the specified site even if a dependent configuration
        on the remote site is preventing synchronization or if one or more GSLB entities
        on the remote site have the same name but are of a different type. You can
        specify either the name of the remote site that you want to synchronize with
        the local site, or you can specify All Sites in the configuration utility
        (the string all-sites in the CLI). If you specify All Sites, all the sites
        in the GSLB setup are synchronized with the site on the master node. '
      - 'Note: If you select the Force Sync option, the synchronization starts without
        displaying the commands that are going to be executed.'
    type: str
  nowarn:
    description:
      - Suppress the warning and the confirmation prompt that are displayed before
        site synchronization begins. This option can be used in automation scripts
        that must not be interrupted by a prompt.
    type: bool
  preview:
    description:
      - Do not synchronize the GSLB sites, but display the commands that would be
        applied on the slave node upon synchronization. Mutually exclusive with the
        Save Configuration option.
    type: bool
  saveconfig:
    description:
      - Save the configuration on all the nodes participating in the synchronization
        process, automatically. The master saves its configuration immediately before
        synchronization begins. Slave nodes save their configurations after the process
        of synchronization is complete. A slave node saves its configuration only
        if the configuration difference was successfully applied to it. Mutually exclusive
        with the Preview option.
    type: bool
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
