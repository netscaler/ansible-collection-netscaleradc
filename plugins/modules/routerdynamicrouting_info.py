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
module: routerdynamicrouting_info
short_description: Retrieve information from dynamic routing configuration.
description:
  - Retrieve information from dynamic routing configuration.
  - This module is a read-only data source that executes show commands.
  - The commandstring parameter must start with 'sh' or 'show' for security.
version_added: 2.13.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
  - Lakshman M J (@lakshmj)
options:
  commandstring:
    type: str
    required: true
    description:
      - Show command to be executed to retrieve routing information.
      - Must start with 'sh' or 'show' (case insensitive).
      - 'Example: "show ip bgp summary" or "sh ip route"'
  nodeid:
    type: int
    description:
      - Unique number that identifies the cluster node.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Get BGP routing information
  delegate_to: localhost
  netscaler.adc.routerdynamicrouting_info:
    nsip: 10.0.0.1
    nitro_user: nsroot
    nitro_pass: nsroot
    nitro_protocol: https
    validate_certs: false
    commandstring: "show ip bgp summary"
  register: bgp_info

- name: Display BGP info
  debug:
    var: bgp_info

- name: Get IP route information
  delegate_to: localhost
  netscaler.adc.routerdynamicrouting_info:
    nsip: 10.0.0.1
    nitro_user: nsroot
    nitro_pass: nsroot
    nitro_protocol: https
    validate_certs: false
    commandstring: "sh ip route"
  register: route_info

- name: Display route info
  debug:
    var: route_info
"""

RETURN = r"""
---
changed:
  description: Always false for info modules as they do not modify state
  returned: always
  type: bool
  sample: false
info:
  description: Information retrieved from the dynamic routing configuration
  returned: success
  type: dict
  sample: {
    "commandstring": "show ip bgp summary",
    "response": "router response data here"
  }
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

from ansible.module_utils.basic import AnsibleModule

from ..module_utils.client import NitroAPIClient
from ..module_utils.common import get_resource
from ..module_utils.constants import NETSCALER_COMMON_ARGUMENTS
from ..module_utils.logger import log, loglines
from ..module_utils.nitro_resource_map import NITRO_RESOURCE_MAP

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def validate_commandstring(commandstring):
    """
    Validate that commandstring starts with 'sh' or 'show' (case insensitive).
    Returns tuple (is_valid, error_message)
    """
    if not commandstring:
        return False, "commandstring cannot be empty"

    # Strip leading/trailing whitespace
    cmd = commandstring.strip()

    # Check if it starts with 'sh' or 'show' (case insensitive)
    if not (cmd.lower().startswith("sh ") or cmd.lower().startswith("show ")):
        return (
            False,
            "commandstring must start with 'sh' or 'show' (case insensitive). Got: '{}'".format(
                commandstring
            ),
        )

    return True, None


def main():
    module_specific_arguments = NITRO_RESOURCE_MAP[RESOURCE_NAME]["readwrite_arguments"]
    argument_spec = dict()
    argument_spec.update(NETSCALER_COMMON_ARGUMENTS)
    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        mutually_exclusive=[
            ("nitro_pass", "nitro_auth_token"),
            (
                "managed_netscaler_instance_name",
                "managed_netscaler_instance_ip",
                "managed_netscaler_instance_id",
            ),
        ],
        required_together=[
            (
                "managed_netscaler_instance_username",
                "managed_netscaler_instance_password",
            ),
        ],
        required_if=[
            (
                "netscaler_console_as_proxy_server",
                True,
                (
                    "managed_netscaler_instance_name",
                    "managed_netscaler_instance_ip",
                    "managed_netscaler_instance_id",
                    "managed_netscaler_instance_username",
                    "managed_netscaler_instance_password",
                ),
                True,
            ),
        ],
    )

    module_result = dict(
        changed=False,  # Info modules never change state
        failed=False,
        loglines=loglines,
    )

    try:
        # Validate commandstring
        commandstring = module.params.get("commandstring")
        is_valid, error_msg = validate_commandstring(commandstring)

        if not is_valid:
            module.fail_json(msg=error_msg, **module_result)

        log("DEBUG: commandstring validation passed: %s" % commandstring)

        # Initialize NITRO client
        client = NitroAPIClient(module, RESOURCE_NAME)

        # NetScaler Console proxy handling
        netscaler_console_as_proxy_server = module.params.get(
            "netscaler_console_as_proxy_server", False
        )
        if netscaler_console_as_proxy_server:
            module.params["api_path"] = "nitro/v2/config"

        # Prepare resource parameters
        resource_module_params = {}
        if commandstring:
            resource_module_params["commandstring"] = commandstring
        if module.params.get("nodeid"):
            resource_module_params["nodeid"] = module.params["nodeid"]

        log(
            "DEBUG: Fetching router dynamic routing info with params: %s"
            % resource_module_params
        )

        # Get the resource information
        # For routerdynamicrouting, we use "routerdynamicrouting" as the resource_name
        # since the info variant uses the same API endpoint
        is_exist, response = get_resource(
            client,
            resource_name="routerdynamicrouting",
            resource_id=None,
            resource_module_params=resource_module_params,
        )

        if is_exist and response:
            module_result["info"] = {
                "commandstring": commandstring,
                "response": response[0].get("output", "")
            }
            log("INFO: Successfully retrieved routing information")
        else:
            # Even if no data, return success with empty response
            module_result["info"] = {"commandstring": commandstring, "response": ""}
            log("INFO: No routing information found or empty response")

        module.exit_json(**module_result)

    except Exception as e:
        msg = "Exception %s: %s" % (type(e).__name__, str(e))
        log("ERROR: %s" % msg)
        module.fail_json(msg=msg, **module_result)


if __name__ == "__main__":
    main()
