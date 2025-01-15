# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import re

from .constants import (
    HTTP_RESOURCE_ALREADY_EXISTS,
    HTTP_RESOURCE_NOT_FOUND,
    HTTP_SUCCESS_CODES,
)
from .decorators import trace
from .logger import log
from .nitro_resource_map import NITRO_RESOURCE_MAP


@trace
def get_netscaler_version(client):
    is_exist, response = get_resource(client, "nsversion")
    if not is_exist:
        log("ERROR: Failed to get NetScaler version")
        return (0.0, 0.0)
    # response = [{'installedversion': True, 'version': 'NetScaler NS13.0: Build 79.1002.nc, Date: Jul  7 2021, 10:31:36   (64-bit)', 'mode': '1'}]
    try:
        # send a tuple of (major, minor) version. i.e. (13.0, 79.1002)
        pattern = r"NetScaler NS(\d+\.\d+): Build (\d+\.\d+)\.nc"
        version = response[0]["version"]
        major, minor = re.search(pattern, version).groups()
        return (float(major), float(minor))
    except Exception as e:
        log("ERROR: Failed to get NetScaler version: {}".format(e))
        return (0.0, 0.0)  # return a dummy version


@trace
def get_resource(client, resource_name, resource_id=None, resource_module_params=None):
    if resource_module_params is None:
        resource_module_params = {}
    get_args = {}
    try:
        for k in NITRO_RESOURCE_MAP[resource_name]["get_arg_keys"]:
            if k in resource_module_params:
                get_args[k] = resource_module_params[k]
    except KeyError:
        log(
            "WARNING: Resource name %s not found in NITRO_RESOURCE_MAP to get get_arg_keys"
            % resource_name
        )

    # FIXME: NITRO-BUG: in `sslprofile_sslcipher_binding`, the NITRO is not returning the `ciphername` attribute. It's a bug in NITRO.
    # Below is a hack to fix it.
    if resource_name == "sslprofile_sslcipher_binding":
        if "ciphername" in get_args:
            get_args["cipheraliasname"] = get_args["ciphername"]
            del get_args["ciphername"]

    if resource_name.endswith("_binding"):
        # binding resources require `filter` instead of `args` to uniquely identify a resource
        status_code, response_body = client.get(
            resource=resource_name,
            id=resource_id,
            filter=get_args,
        )
    elif resource_name in {"sslcertfile"}:
        status_code, response_body = client.get(
            resource=resource_name,
            id=resource_id,
            filter=get_args,
        )
    else:
        status_code, response_body = client.get(
            resource=resource_name,
            id=resource_id,
            args=get_args,
        )
    if status_code in {HTTP_RESOURCE_NOT_FOUND}:
        return False, []
    if status_code in HTTP_SUCCESS_CODES:
        # for zero bindings and some resources, the response_body will be {'errorcode': 0, 'message': 'Done', 'severity': 'NONE'}
        if resource_name not in response_body:
            if resource_name == "sslcipher":
                resource_primary_key = NITRO_RESOURCE_MAP[resource_name]["primary_key"]
                return True, [
                    {resource_primary_key: resource_module_params[resource_primary_key]}
                ]

            return False, []
        # `update-only` resources return a dict instead of a list.
        return_response = response_body[resource_name]
        # FIXME: NITRO-BUG: for some resources like `policypatset_pattern_binding`, NITRO returns keys with uppercase. eg: `String` for `string`.
        # So, we are converting the keys to lowercase.
        # except for `ping` and `traceroute`, all the othe resources returns a keys with lowercase.
        # These `ping` and `traceroute` do not have GET operation. So, we are not handling them here.
        if isinstance(return_response, dict):
            return_response = [{k.lower(): v for k, v in return_response.items()}]
        elif isinstance(return_response, list):
            return_response = [
                {k.lower(): v for k, v in resource.items()}
                for resource in return_response
            ]
        else:
            log(
                "WARNING: Unexpected response for resource `{}`. Expected a list or a dict, but got: {}".format(
                    resource_name, return_response
                )
            )

        # Take care of NITRO Anomolies
        return_response = fix_nitro_anomolies(
            resource_name, resource_module_params, return_response
        )
        return (True, return_response)
    return False, []


@trace
def fix_nitro_anomolies(resource_name, resource_module_params, return_response):
    for resource in return_response:
        # FIXME: NITRO-BUG: in lbmonitor, for `interval=60`, the `units3` will wrongly be set to `MIN` by the NetScaler.
        # Hence, we will set it to `SEC` to make it idempotent
        # Refer Issue: #324 (https://github.com/netscaler/ansible-collection-netscaleradc/issues/324)
        if resource_name == "lbmonitor":
            # default value for `units3` is `SEC`
            if (
                "units3" not in resource_module_params
                or resource_module_params["units3"] == "SEC"
            ):
                if "units3" in resource and resource["units3"] == "MIN":
                    resource["interval"] = int(resource["interval"]) * 60
                    resource["units3"] = "SEC"

        # FIXME:NITRO-BUG: in `sslprofile_sslcipher_binding`, the NITRO is not returning the `ciphername` attribute. It's a bug in NITRO.
        # Below is a hack to fix it.
        elif resource_name == "sslprofile_sslcipher_binding":
            if "ciphername" not in resource and "cipheraliasname" in resource:
                resource["ciphername"] = resource["cipheraliasname"]
    return return_response


@trace
def get_bindings(client, binding_name, binding_id, resource_module_params):
    return get_resource(
        client,
        resource_name=binding_name,
        resource_id=binding_id,
        resource_module_params=resource_module_params,
    )


@trace
def is_resource_exists(client, resource_name, resource_module_params):
    resource_primary_key = get_primary_key(resource_name, resource_module_params)

    resource_id = (
        resource_module_params[resource_primary_key] if resource_primary_key else None
    )

    is_exists, resources = get_resource(
        client,
        resource_name=resource_name,
        resource_id=resource_id,
        resource_module_params=resource_module_params,
    )
    return is_exists


@trace
def _check_create_resource_params(resource_name, resource_module_params, action=None):
    post_data = {}

    resource_add_keys = NITRO_RESOURCE_MAP[resource_name]["add_payload_keys"]
    try:
        resource_action_keys = NITRO_RESOURCE_MAP[resource_name]["action_payload_keys"][
            action
        ]
    except KeyError:
        resource_action_keys = []

    # TODO: Should we allow non-add keys for the resource? OR should we error out if any non-add key is passed?
    for key in resource_module_params.keys():
        if not action:
            if key in resource_add_keys:
                post_data[key] = resource_module_params[key]
            elif resource_name == "service" and key == "ipaddress":
                post_data["ip"] = resource_module_params[key]
            else:
                log(
                    "WARNING: Key `{}` is not allowed for the resource `{}` for CREATE operation. Skipping the key for the operation".format(
                        key, resource_name
                    )
                )
        else:
            if key in resource_action_keys:
                post_data[key] = resource_module_params[key]
            else:
                log(
                    "WARNING: Key `{}` is not allowed for the resource `{}` for `{}` action. Skipping the key for the operation".format(
                        key, resource_name, action.upper()
                    )
                )

    return True, None, post_data


@trace
def create_resource_with_action(client, resource_name, resource_module_params, action):
    ok, err, post_data = _check_create_resource_params(
        resource_name, resource_module_params, action=action
    )
    if not ok:
        return False, err

    post_data = {resource_name: post_data}
    status_code, response_body = client.post(
        post_data=post_data,
        resource=resource_name,
        action=action,
    )

    if status_code == HTTP_RESOURCE_ALREADY_EXISTS:
        response_body.update({"status_code": status_code})
        return True, response_body

    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="create_resource",
        resource_name=resource_name,
    )


@trace
def create_resource(client, resource_name, resource_module_params, action=None):
    ok, err, post_data = _check_create_resource_params(
        resource_name, resource_module_params
    )
    if not ok:
        return False, err

    post_data = {resource_name: post_data}
    status_code, response_body = client.post(
        post_data=post_data,
        resource=resource_name,
        action=action,
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="create_resource",
        resource_name=resource_name,
    )


@trace
def get_bindprimary_key(binding_name, binding_member):
    bindprimary_key = NITRO_RESOURCE_MAP[binding_name]["bindprimary_key"]

    # `ip` and `servername` are the two possible bind_primary_keys for `servicegroup_servicegroupmember_binding` resource.
    if binding_name == "servicegroup_servicegroupmember_binding":
        if bindprimary_key == "ip":
            if (
                "ip" not in binding_member
                or binding_member["ip"] == "0.0.0.0"  # nosec: B104
            ):
                bindprimary_key = "servername"
            elif "servername" in binding_member and binding_member["servername"]:
                bindprimary_key = "servername"

    return bindprimary_key


@trace
def get_primary_key(resource_name, resource_module_params):
    resource_primary_key = NITRO_RESOURCE_MAP[resource_name]["primary_key"]
    if resource_primary_key in resource_module_params.keys():
        return resource_primary_key

    return None


@trace
def _check_update_resource_params(resource_name, resource_module_params):
    put_data = {}

    if resource_name.endswith("_binding"):
        resource_update_keys = NITRO_RESOURCE_MAP[resource_name]["add_payload_keys"]
    else:
        resource_update_keys = NITRO_RESOURCE_MAP[resource_name]["update_payload_keys"]

    # TODO: Should we allow non-update keys for the resource? OR should we error out if any non-update key is passed?
    for key in resource_module_params.copy().keys():
        if key in resource_update_keys:
            put_data[key] = resource_module_params[key]
        elif resource_name == "service" and key == "ip":
            put_data["ipaddress"] = resource_module_params[key]
        else:
            log(
                "WARNING: Key `{}` is not allowed for the resource `{}` for the UPDATE operation. Skipping the key for the operation".format(
                    key, resource_name
                )
            )

    return True, None, put_data


@trace
def update_resource(client, resource_name, resource_module_params):
    ok, err, put_payload = _check_update_resource_params(
        resource_name, resource_module_params
    )
    if not ok:
        return False, err

    put_data = {resource_name: put_payload}

    status_code, response_body = client.put(
        put_data=put_data,
        resource=resource_name,
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="update_resource",
        resource_name=resource_name,
        # resource_id=resource_id,
    )


@trace
def delete_resource(client, resource_name, resource_module_params):
    resource_primary_key = get_primary_key(resource_name, resource_module_params)

    resource_id = (
        resource_module_params[resource_primary_key] if resource_primary_key else None
    )

    args = {}
    for arg_key in NITRO_RESOURCE_MAP[resource_name]["delete_arg_keys"]:
        if resource_primary_key == arg_key:
            continue
        if resource_name == "servicegroup_servicegroupmember_binding":
            if arg_key == "ip":
                # Reason:{'errorcode': 1092, 'message': 'Arguments cannot both be specified [serverName, IP]', 'severity': 'ERROR'}"
                if "servername" in resource_module_params:
                    if resource_module_params["servername"]:
                        continue
                    else:
                        err = "ERROR: `servername` cannnot be empty for the resource `{}`".format(
                            resource_name
                        )
                        return False, err
        if resource_name == "lbvserver_servicegroup_binding":
            if arg_key == "servicename":
                # Reason: {'errorcode': 1092, 'message': 'Arguments cannot both be specified [serviceName, serviceGroupName]', 'severity': 'ERROR'}
                if "servicegroupname" in resource_module_params:
                    if resource_module_params["servicegroupname"]:
                        continue
                    else:
                        err = "ERROR: `servicegroupname` cannnot be empty for the resource `{}`".format(
                            resource_name
                        )
                        return False, err

        try:
            args[arg_key] = resource_module_params[arg_key]
        except KeyError:
            # TODO: Should we return False here? Or should we just log and continue?
            log(
                "WARNING: arg_key `{}` is missing for the resource `{}`".format(
                    arg_key, resource_name
                )
            )
            continue

    if not is_resource_exists(client, resource_name, resource_module_params):
        return True, None

    status_code, response_body = client.delete(
        resource=resource_name,
        id=resource_id,
        args=args,
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="delete_resource",
        resource_name=resource_name,
        resource_id=resource_id,
    )


@trace
def get_transformed_dict(transforms, values_dict):
    transformed_dict = {}
    for key in values_dict:
        value = values_dict.get(key)
        transform = transforms.get(key)
        if transform is not None:
            value = transform(values_dict.get(key))
        transformed_dict[key] = value
    return transformed_dict


@trace
def bind_resource(client, binding_name, binding_module_params):
    return update_resource(
        client=client,
        resource_name=binding_name,
        resource_module_params=binding_module_params,
    )


@trace
def unbind_resource(client, binding_name, binding_module_params):
    return delete_resource(
        client=client,
        resource_name=binding_name,
        resource_module_params=binding_module_params,
    )


@trace
def return_response(
    status_code, response_body, operation, resource_name, resource_id=None
):
    if status_code in HTTP_SUCCESS_CODES:
        if resource_id:
            log("DEBUG: %s %s/%s SUCCESS" % (operation, resource_name, resource_id))
        else:
            log("DEBUG: %s %s SUCCESS" % (operation, resource_name))
        return True, response_body
    else:
        err = "ERROR: %s FAILED; status_code: %s; Reason:%s" % (
            operation,
            status_code,
            response_body,
        )
        log(err)
        return False, err


@trace
def save_config(client, all=False):
    # Save the config in the current partition.
    post_payload = {"nsconfig": {} if not all else {"all": True}}
    status_code, response_body = client.post(
        post_data=post_payload, resource="nsconfig", action="save"
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="save_config",
        resource_name="nsconfig",
    )


@trace
def enable_resource(client, resource_name, resource_params):
    post_payload = {resource_name: {}}
    if resource_name == "gslbservice":
        post_payload = {"service": {}}
        enable_payload_keys = NITRO_RESOURCE_MAP["service"]["enable_payload_keys"]
        resource_params["name"] = resource_params["servicename"]
    else:
        post_payload = {resource_name: {}}
        enable_payload_keys = NITRO_RESOURCE_MAP[resource_name]["enable_payload_keys"]

    for key in enable_payload_keys:
        try:
            post_payload[list(post_payload.keys())[0]][key] = resource_params[key]
        except KeyError:
            continue  # TODO: Should we return False here? Or should we just log and continue?

    status_code, response_body = client.post(
        post_data=post_payload, resource=list(post_payload.keys())[0], action="enable"
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="enable_resource",
        resource_name=resource_name,
    )


@trace
def disable_resource(client, resource_name, resource_params):
    if resource_name == "gslbservice":
        post_payload = {"service": {}}
        disable_payload_keys = NITRO_RESOURCE_MAP["service"]["disable_payload_keys"]
        resource_params["name"] = resource_params["servicename"]
    else:
        post_payload = {resource_name: {}}
        disable_payload_keys = NITRO_RESOURCE_MAP[resource_name]["disable_payload_keys"]

    for key in disable_payload_keys:
        try:
            post_payload[list(post_payload.keys())[0]][key] = resource_params[key]
        except KeyError:
            continue  # TODO: Should we return False here? Or should we just log and continue?

    status_code, response_body = client.post(
        post_data=post_payload, resource=list(post_payload.keys())[0], action="disable"
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="disable_resource",
        resource_name=resource_name,
    )


@trace
def adc_login(client, username, password, new_password=None):
    post_data = {
        "login": {
            "username": username,
            "password": password,
        }
    }
    if new_password:
        post_data["login"]["new_password"] = new_password

    status_code, response_body = client.post(
        post_data=post_data,
        resource="login",
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="login",
        resource_name="login",
    )


@trace
def adc_logout(client):
    post_data = {
        "logout": {},
    }
    if client._module.params["netscaler_console_as_proxy_server"]:
        post_data["logout"]["sessionid"] = client._module.params["nitro_auth_token"]
    status_code, response_body = client.post(
        post_data=post_data,
        resource="logout",
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="logout",
        resource_name="logout",
    )


@trace
def get_supported_operations(resource_name):
    return NITRO_RESOURCE_MAP[resource_name]["_supported_operations"]


@trace
def get_valid_desired_states(resource_name):
    desired_states = set()
    # Read the desired states from the resource map
    # All supported operations are
    # 'delete', 'change', 'Ping6', 'get-byname', 'enable', 'Switch', 'Force', 'init', 'Traceroute6', 'kill',
    # 'Traceroute', 'add', 'check', 'reset', 'rename', 'convert', 'unset', 'send', 'clear', 'update', 'Reboot',
    # 'unsign', 'Install', 'Ping', 'export', 'save', 'expire', 'get-all', 'flush', 'unlock', 'diff', 'Import',
    # 'disable', 'create', 'sign', 'get', 'apply', 'restore', 'unlink', 'link', 'count', 'join', 'renumber', 'sync'
    supported_operations = NITRO_RESOURCE_MAP[resource_name]["_supported_operations"]
    if (
        "add" in supported_operations
        or "update" in supported_operations
        or "Force" in supported_operations
        or "force" in supported_operations
    ):
        desired_states.add("present")
    if "delete" in supported_operations:
        desired_states.add("absent")
    if "enable" in supported_operations:
        desired_states.add("enabled")
    if "disable" in supported_operations:
        desired_states.add("disabled")
    if "create" in supported_operations:
        desired_states.add("created")
    if "flush" in supported_operations:
        desired_states.add("flushed")
    if "import" in supported_operations or "Import" in supported_operations:
        desired_states.add("imported")
    if "Switch" in supported_operations or "switch" in supported_operations:
        desired_states.add("switched")
    if "unset" in supported_operations:
        desired_states.add("unset")
    return desired_states


@trace
def is_global_binding(resource_name):
    return (
        True
        if (resource_name.endswith("_binding") and "global" in resource_name)
        else False
    )


@trace
def is_singleton_resource(resource_name):
    return NITRO_RESOURCE_MAP[resource_name]["singleton"]
