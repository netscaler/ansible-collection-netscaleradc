# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.basic import env_fallback

HTTP_SUCCESS_CODES = {0, 200, 201}  # 0 is for check_mode
HTTP_RESOURCE_NOT_FOUND = 404
HTTP_RESOURCE_ALREADY_EXISTS = 409

HTTP_STATUS_CODES = {
    404: "Resource Not Found",
    409: "Resource already exists",
}

NETSCALER_EMPTY_ADD_PAYLOAD_RESOURCES = [
    "logout",
]

ATTRIBUTES_NOT_PRESENT_IN_GET_RESPONSE = {
    "sslcertkey": {"password"},
}

# NITRO accepts some attributes with a name and responsds with a different name in its GET reponse.
# Eg: For "gslbservice" resource, NITRO expects "ip" in POST request
# but expects "ipaddress" in PUT payload and returns "ipaddress" in GET response.
NITRO_ATTRIBUTES_ALIASES = {
    # "resource": {
    #     "attribute": "attribute_alias",
    # }
    "gslbservice": {
        "ip": "ipaddress",
        "ipaddress": "ip", # For PUT payloads and GET responses
    }
}

# https://docs.ansible.com/ansible/latest/dev_guide/developing_program_flow_modules.html#argument-spec
NETSCALER_COMMON_ARGUMENTS = dict(
    nsip=dict(
        required=True,
        fallback=(env_fallback, ["NETSCALER_NSIP"]),
    ),
    nitro_user=dict(
        required=False,
        fallback=(env_fallback, ["NETSCALER_NITRO_USER"]),
        no_log=True,
    ),
    nitro_pass=dict(
        required=False,
        fallback=(env_fallback, ["NETSCALER_NITRO_PASS"]),
        no_log=True,
    ),
    nitro_protocol=dict(
        required=False,
        choices=["http", "https"],
        fallback=(env_fallback, ["NETSCALER_NITRO_PROTOCOL"]),
        default="https",
    ),
    validate_certs=dict(
        default=True,
        type="bool",
        fallback=(env_fallback, ["NETSCALER_VALIDATE_CERTS"]),
    ),
    save_config=dict(
        type="bool",
        default=False,
        fallback=(env_fallback, ["NETSCALER_SAVE_CONFIG"]),
    ),
    nitro_auth_token=dict(
        type="str",
        no_log=True,
        fallback=(env_fallback, ["NETSCALER_NITRO_AUTH_TOKEN"]),
    ),
    api_path=dict(
        type="str",
        required=False,
        default="nitro/v1/config",
    ),
)
