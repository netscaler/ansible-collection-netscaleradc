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
    response = get_resource(client, "nsversion")
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
def get_resource(
    client, resource_name, resource_id=None, args=None, attrs=None, filter=None
):
    status_code, response_body = client.get(
        resource=resource_name,
        id=resource_id,
        args=args,
        attrs=attrs,
        filter=filter,
    )
    if status_code in {HTTP_RESOURCE_NOT_FOUND}:
        return []
    try:
        # `update-only` resources return a dict instead of a list.
        return_response = response_body[resource_name]
        return (
            return_response if isinstance(return_response, list) else [return_response]
        )
    except (
        KeyError
    ):  # for zero bindings, the response_body will be {'errorcode': 0, 'message': 'Done', 'severity': 'NONE'}
        return []


@trace
def get_bindings(client, binding_name, binding_id=None):
    return get_resource(
        client,
        resource_name=binding_name,
        resource_id=binding_id,
    )


@trace
def is_resource_exists(
    client, resource_name, resource_id=None, args=None, attrs=None, filter=None
):
    status_code, resources = client.get(
        resource=resource_name,
        id=resource_id,
        args=args,
        attrs=attrs,
        filter=filter,
    )
    # FIXME: Handle the case where invalid argument caused 599 status code
    return True if status_code in HTTP_SUCCESS_CODES else False


@trace
def _check_create_resource_params(resource_name, resource_module_params, action=None):
    # check if resource_module_params contains any key other than allowed keys for the resource
    # check also if resource_module_params contains all the required keys for the resource
    # if not, return False, err

    post_data = {}

    resource_add_keys = NITRO_RESOURCE_MAP[resource_name]["add_payload_keys"]
    try:
        resource_action_keys = NITRO_RESOURCE_MAP[resource_name]["action_payload_keys"][
            action
        ]
    except KeyError:
        resource_action_keys = []
    resource_primary_key = NITRO_RESOURCE_MAP[resource_name]["primary_key"]

    if (
        resource_primary_key
        and resource_primary_key not in resource_module_params.keys()
    ):
        err = "ERROR: Primary key `{}` is missing for the resource `{}`".format(
            resource_primary_key, resource_name
        )
        log(err)
        return False, err, {}

    # TODO: check for other mandatory keys for the resource
    # This will be checked by ansible itself by reading the `required` field in the schema

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
                    "WARNING: Key `{}` is not allowed for the resource `{}` for CREATE operation. Skipping the key for the operation".format(
                        key, resource_name
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

    # FIXME: if action=unset, check for idempotency, as of now, unset always leads to changed state

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
def _check_update_resource_params(resource_name, resource_module_params):
    # check if resource_module_params contains any key other than allowed keys for the resource
    # check also if resource_module_params contains all the required keys for the resource
    # if not, return False, err

    put_data = {}

    if resource_name.endswith("_binding"):
        resource_update_keys = NITRO_RESOURCE_MAP[resource_name]["add_payload_keys"]
    else:
        resource_update_keys = NITRO_RESOURCE_MAP[resource_name]["update_payload_keys"]

    resource_primary_key = NITRO_RESOURCE_MAP[resource_name]["primary_key"]

    if resource_primary_key and (
        resource_primary_key not in resource_module_params.keys()
    ):
        err = "ERROR: Primary key `{}` is missing for the resource `{}`".format(
            resource_primary_key, resource_name
        )
        log(err)
        return False, err, {}

    # TODO: check for other mandatory keys for the resource

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

    # if non_updatable_attributes:
    #     for attribute in resource_module_params.keys():
    #         if attribute in non_updatable_attributes:
    #             del put_payload[attribute]

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
def _check_delete_resource_params(resource_name, resource_module_params):
    # check if resource_module_params contains any key other than allowed keys for the resource
    # check also if resource_module_params contains all the required keys for the resource
    # if not, return False, err

    resource_primary_key = NITRO_RESOURCE_MAP[resource_name]["primary_key"]

    if (
        resource_primary_key
        and resource_primary_key not in resource_module_params.keys()
    ):
        err = "ERROR: Primary key `{}` is missing for the resource `{}`".format(
            resource_primary_key, resource_name
        )
        log(err)
        return False, err

    return True, None


@trace
def delete_resource(client, resource_name, resource_module_params):
    ok, err = _check_delete_resource_params(resource_name, resource_module_params)
    if not ok:
        return False, err

    args = {}
    for arg_key in NITRO_RESOURCE_MAP[resource_name]["delete_arg_keys"]:
        log("DEBUG: arg_key: {}".format(arg_key))
        # FIXME: after discussion with Nitro team
        if (
            resource_name == "lbvserver_servicegroup_binding"
            and arg_key == "servicename"
        ):
            # status_code: 400;
            # Reason:{'errorcode': 1092, 'message': 'Arguments cannot both be specified [serviceGroupName, serviceName]', 'severity': 'ERROR'}
            continue
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

    if NITRO_RESOURCE_MAP[resource_name]["primary_key"]:
        resource_id = resource_module_params[
            NITRO_RESOURCE_MAP[resource_name]["primary_key"]
        ]
    else:
        resource_id = None

    if resource_name.endswith("_binding"):
        if not is_resource_exists(client, resource_name, resource_id, filter=args):
            return True, None
    elif resource_name in {"sslcertfile"}:
        if not is_resource_exists(client, resource_name, resource_id, filter=args):
            return True, None
    else:
        if not is_resource_exists(client, resource_name, resource_id, args=args):
            return True, None
    # send() returned (599, {'errorcode': 278, 'message': 'Invalid argument [servicename]', 'severity': 'ERROR'})",
    # In the above case, we can't tell if the resource exists or not. So, we are not checking for resource existence.

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
def save_config(client):
    # Save the config in the current partition.
    post_payload = {"nsconfig": {}}
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
    enable_payload_keys = NITRO_RESOURCE_MAP[resource_name]["enable_payload_keys"]

    for key in enable_payload_keys:
        try:
            post_payload[resource_name][key] = resource_params[key]
        except KeyError:
            continue  # TODO: Should we return False here? Or should we just log and continue?

    status_code, response_body = client.post(
        post_data=post_payload, resource=resource_name, action="enable"
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="enable_resource",
        resource_name=resource_name,
    )


@trace
def disable_resource(client, resource_name, resource_params):
    post_payload = {resource_name: {}}
    disable_payload_keys = NITRO_RESOURCE_MAP[resource_name]["disable_payload_keys"]

    for key in disable_payload_keys:
        try:
            post_payload[resource_name][key] = resource_params[key]
        except KeyError:
            continue  # TODO: Should we return False here? Or should we just log and continue?

    status_code, response_body = client.post(
        post_data=post_payload, resource=resource_name, action="disable"
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
    if "add" in supported_operations or "update" in supported_operations:
        desired_states.add("present")
    if "delete" in supported_operations or "unset" in supported_operations:
        desired_states.add("absent")
    if "enable" in supported_operations:
        desired_states.add("enabled")
    if "disable" in supported_operations:
        desired_states.add("disabled")
    if "create" in supported_operations:
        desired_states.add("created")
    if "import" in supported_operations or "Import" in supported_operations:
        desired_states.add("imported")
    if "Switch" in supported_operations:
        desired_states.add("switched")
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
