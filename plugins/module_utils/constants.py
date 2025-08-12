# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
        "ipaddress": "ip",  # For PUT payloads and GET responses
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
    netscaler_console_as_proxy_server=dict(
        type="bool",
        required=False,
        default=False,
        fallback=(env_fallback, ["NETSCALER_CONSOLE_AS_PROXY_SERVER"]),
    ),
    managed_netscaler_instance_name=dict(
        type="str",
        required=False,
        fallback=(env_fallback, ["MANAGED_NETSCALER_INSTANCE_NAME"]),
    ),
    managed_netscaler_instance_ip=dict(
        type="str",
        required=False,
        fallback=(env_fallback, ["MANAGED_NETSCALER_INSTANCE_IP"]),
    ),
    managed_netscaler_instance_id=dict(
        type="str",
        required=False,
        fallback=(env_fallback, ["MANAGED_NETSCALER_INSTANCE_ID"]),
    ),
    managed_netscaler_instance_username=dict(
        type="str",
        required=False,
        fallback=(env_fallback, ["MANAGED_NETSCALER_INSTANCE_USERNAME"]),
    ),
    managed_netscaler_instance_password=dict(
        type="str",
        required=False,
        no_log=True,
        fallback=(env_fallback, ["MANAGED_NETSCALER_INSTANCE_PASSWORD"]),
    ),
)

# this list contains globalbindings whose GET call must have query params args=type and filter=get_arg_keys (check in nitro_resource_map)
GLOBAL_BINDING_ARG_LIST = [
    'dnsglobal_dnspolicy_binding',
    'responderglobal_responderpolicy_binding',
    'contentinspectionglobal_contentinspectionpolicy_binding',
    'appflowglobal_appflowpolicy_binding',
    'appfwglobal_auditnslogpolicy_binding',
    'appfwglobal_auditsyslogpolicy_binding',
    'appfwglobal_appfwpolicy_binding',
    'rewriteglobal_rewritepolicy_binding',
    'transformglobal_transformpolicy_binding',
    'sslglobal_sslpolicy_binding',
    'tunnelglobal_tunneltrafficpolicy_binding',
    'cmpglobal_cmppolicy_binding',
    'feoglobal_feopolicy_binding',
    'icaglobal_icapolicy_binding',
    'lbglobal_lbpolicy_binding',
    'cacheglobal_cachepolicy_binding',
    'botglobal_botpolicy_binding',
]
