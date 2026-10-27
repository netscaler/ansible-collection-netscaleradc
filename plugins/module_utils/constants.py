# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)


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
    # action-only parameters of `disable`: never returned by GET, not in add/update payloads
    "server": {"delay", "graceful"},
    "service": {"delay", "graceful"},
    "servicegroup": {"delay", "graceful"},
    "gslbservicegroup": {"delay", "graceful"},
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

# NITRO-BUG (issue #636): for some boolean-like attributes NITRO accepts one vocabulary on
# write but returns another one in its GET response. Eg: `nsrpcnode.secure` is set with
# YES/NO but read back as ON/OFF; `nsappflowparam.http*` are set with ENABLED/DISABLED but
# read back as ON/OFF. `fix_nitro_anomolies()` rewrites such a GET value to the declared
# choice with the same meaning, but only when the attribute's declared choices are exactly
# one word from each set below and the returned value is not one of the declared choices.
# Do not relax the "exactly 2 choices" rule: NITRO does not treat these words as synonyms
# everywhere. Eg: `vpnsessionaction.clientlessvpnmode` declares ON/OFF/DISABLED, and there
# OFF != DISABLED. Note also that widening the generated choices of an affected attribute
# (eg: adding ON/OFF to `nsrpcnode.secure`) silently disables this rule for it.
NITRO_BOOLEAN_TRUE_VALUES = {"YES", "ON", "ENABLED", "ENABLE", "TRUE"}
NITRO_BOOLEAN_FALSE_VALUES = {"NO", "OFF", "DISABLED", "DISABLE", "FALSE"}

# `state: enabled|disabled` sends the enable/disable action only when the current state read
# from the GET response differs (issue #636). The current state is read from the attribute
# listed here, or from `state` for resources not listed. `None` means that the state cannot be
# read reliably, so the action is always sent (legacy behaviour).
ENABLE_DISABLE_STATE_ATTRIBUTE = {
    # GET returns no `state` for lbvserver; its operational `curstate` is read instead
    # (see ENABLE_DISABLE_CURSTATE_VALUES)
    "lbvserver": "curstate",
    "systemextramgmtcpu": "configuredstate",
    "systemnsbtracing": "configuredstate",
    # only `effectivestate` is returned, which may differ from the configured state until reboot
    "filesystemencryption": None,
    # the enabled features/modes are returned as a list, not as a single state
    "nsfeature": None,
    "nsmode": None,
    # NITRO enable/disable of lbmonitor always targets a monitor binding (servicename/servicegroupname
    # is mandatory, errorcode 1095); the monitor's own `state` is not what the action changes
    "lbmonitor": None,
    # GET returns no `state`; `svrstate` is OUT OF SERVICE and `dup_state` vanishes also when only the
    # parent server is disabled, so the service's own admin state cannot be read (14.1-73.33)
    "service": None,
    # enable/disable is redirected to `service`; same ambiguity (not verified on a device)
    "gslbservice": None,
    # GET is identical for an enabled and a disabled authentication vserver (14.1-73.33)
    "authenticationvserver": None,
}

# For these singletons the GET returns one boolean per feature/mode, keyed by the lower-case short
# code (eg: `lb`, `usnip`). Long aliases (eg: `LoadBalancing`) have no such key and are "unknown".
ENABLE_DISABLE_LIST_ATTRIBUTE = {"nsfeature": "feature", "nsmode": "mode"}

# Values of the above state attributes and the configured state that they imply. Any other
# value (eg: `UNSET` for snmpalarm, `GOING OUT OF SERVICE`) is treated as unknown.
ENABLE_DISABLE_STATE_VALUES = {
    "ENABLED": "ENABLED",
    "DISABLED": "DISABLED",
}
# Operational vserver state values; only used for attributes named `curstate` (see above).
# UP/DOWN imply that the vserver itself is enabled. `OUT OF SERVICE` is deliberately not
# mapped: it is also reported for an enabled vserver whose VIP is disabled (14.1-73.33), so
# it is treated as unknown and the disable action is always sent.
ENABLE_DISABLE_CURSTATE_VALUES = dict(
    ENABLE_DISABLE_STATE_VALUES,
    **{"UP": "ENABLED", "DOWN": "ENABLED"},
)

# Enable/disable payload keys that redirect the action to a sub-object (eg: a servicegroup member
# or a monitor bound to a service). The state of that sub-object is not the `state` returned for the
# resource itself, so the action is always sent when any of these keys is given.
ENABLE_DISABLE_SUBOBJECT_KEYS = {
    "gslbservicegroup": {"servername", "port"},
    "servicegroup": {"servername", "port"},
}

# Deprecated single-letter option names that collided under ansible-core >= 2.18
# `validate-modules:option-equal-up-to-casing` (e.g. I/i, S/s, T/t) are no longer
# tracked here. The generator now emits, per affected resource, a
# `deprecated_aliases` map ({old_name: new_snake_case}) directly in NITRO_RESOURCE_MAP
# ModuleExecutor reads it to keep old playbooks working (pre-parse translation + deprecation warning) and to restore
# the single-letter NITRO wire fields before the POST.

# Operational "utility" resources: they do not store config. Each is a synchronous
# NITRO action (plain POST to /nitro/v1/config/<resource>, no `?action=`) that runs a
# BSD command on the ADC and returns its output in the response body.
# ModuleExecutor.main() dispatches these to `run_operational_action` instead of the
# normal create/update/delete flow.
OPERATIONAL_UTILITY_RESOURCES = {"ping", "ping6", "traceroute", "traceroute6"}

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
    "dnsglobal_dnspolicy_binding",
    "responderglobal_responderpolicy_binding",
    "contentinspectionglobal_contentinspectionpolicy_binding",
    "appflowglobal_appflowpolicy_binding",
    "appfwglobal_auditnslogpolicy_binding",
    "appfwglobal_auditsyslogpolicy_binding",
    "appfwglobal_appfwpolicy_binding",
    "rewriteglobal_rewritepolicy_binding",
    "transformglobal_transformpolicy_binding",
    "sslglobal_sslpolicy_binding",
    "tunnelglobal_tunneltrafficpolicy_binding",
    "cmpglobal_cmppolicy_binding",
    "feoglobal_feopolicy_binding",
    "icaglobal_icapolicy_binding",
    "lbglobal_lbpolicy_binding",
    "cacheglobal_cachepolicy_binding",
    "botglobal_botpolicy_binding",
]

GETALL_ONLY_RESOURCES = [
    "appfwlearningdata",
    "application",
    "bridgetable",
    "gslbldnsentry",
    "locationfile",
    "locationfile6",
    "routerdynamicrouting",
    "sslcertbundle",
    "sslcertfile",
    "sslcrlfile",
    "ssldhfile",
    "sslkeyfile",
    "systementitydata",
]

# Dynamic Protocol list
DYNAMIC_PROTOCOLS = [
    "accesslist",
    "bfdinterface",
    "iproute",
    "ospf6interface",
    "routemap",
    "ospf6router",
    "bgprouter",
    "ospfrouter",
    "ospfinterface",
]

DYNAMIC_PROTOCOLS_ALIAS = {
    "accesslist": "accessList",
    "bfdinterface": "bfdInterface",
    "iproute": "ipRoute",
    "ospf6interface": "ospf6Interface",
    "routemap": "routeMap",
    "ospf6router": "ospf6Router",
    "bgprouter": "bgpRouter",
    "ospfrouter": "ospfRouter",
    "ospfinterface": "ospfInterface",
}
