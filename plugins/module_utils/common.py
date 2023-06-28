import copy

from .constants import HTTP_RESOURCE_NOT_FOUND, HTTP_SUCCESS_CODES
from .decorators import trace
from .log import log
from .nitro_resource_map import NITRO_RESOURCE_MAP


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
    status_code, _ = client.get(
        resource=resource_name,
        id=resource_id,
        args=args,
        attrs=attrs,
        filter=filter,
    )
    return True if status_code in HTTP_SUCCESS_CODES else False


@trace
def _check_create_resource_params(resource_name, resource_module_params):
    # check if resource_module_params contains any key other than allowed keys for the resource
    # check also if resource_module_params contains all the required keys for the resource
    # if not, return False, err

    post_data = {}

    resource_add_keys = NITRO_RESOURCE_MAP[resource_name]["add_payload_keys"]
    resource_primary_key = NITRO_RESOURCE_MAP[resource_name]["primary_key"]

    if resource_primary_key not in resource_module_params.keys():
        err = "ERROR: Primary key `{}` is missing for the resource `{}`".format(
            resource_primary_key, resource_name
        )
        log(err)
        return False, err, {}

    # TODO: check for other mandatory keys for the resource

    # TODO: Should we allow non-add keys for the resource? OR should we error out if any non-add key is passed?
    for key in resource_module_params.keys():
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

    return True, None, post_data


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

    if resource_primary_key not in resource_module_params.keys():
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
        # FIXME: after discussion with Nitro team
        if (
            resource_name == "lbvserver_servicegroup_binding"
            and arg_key == "servicename"
        ):
            # status_code: 400; Reason:{'errorcode': 1092, 'message': 'Arguments cannot both be specified [serviceGroupName, serviceName]', 'severity': 'ERROR'}
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

    resource_id = resource_module_params[
        NITRO_RESOURCE_MAP[resource_name]["primary_key"]
    ]

    if resource_name.endswith("_binding"):
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
    # put_values = copy.deepcopy(configured_dict)
    # put_values["name"] = self.module.params["name"]
    # put_values = get_transformed_dict(
    #     transforms=self.attribute_config["servicebindings"]["transforms"],
    #     values_dict=put_values,
    # )

    put_data = {binding_name: payload}
    status_code, response_body = client.put(put_data=put_data, resource=binding_name)

    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="bind_resource",
        resource_name=binding_name,
    )


@trace
def unbind_resource(client, binding_name, binding_module_params):
    return delete_resource(
        client=client,
        resource_name=binding_name,
        resource_module_params=binding_module_params,
    )
    service_binding = copy.deepcopy(binding_module_params)
    args = {}
    delete_id_attributes = NITRO_RESOURCE_MAP[binding_name]["delete_arg_keys"]
    for attribute in delete_id_attributes:
        value = service_binding.get(attribute)
        if value is not None and value != "":
            log("Appending to args %s:%s" % (attribute, value))
            args[attribute] = value

    status_code, response_body = client.delete(
        resource=binding_name,
        id=binding_id,
        args=args,
    )
    return return_response(
        status_code=status_code,
        response_body=response_body,
        operation="unbind_resource",
        resource_name=binding_name,
        resource_id=binding_id,
    )


@trace
def return_response(
    status_code, response_body, operation, resource_name, resource_id=None
):
    if status_code in HTTP_SUCCESS_CODES:
        if resource_id:
            log(f"DEBUG: {operation} {resource_name}/{resource_id} SUCCESS")
        else:
            log(f"DEBUG: {operation} {resource_name} SUCCESS")
        return True, None
    else:
        err = f"ERROR: {operation} FAILED; status_code: {status_code}; Reason:{response_body}"
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
def get_valid_desired_states(resource_name):
    desired_states = set()
    # Read the desired states from the resource map
    resource_map_keys = NITRO_RESOURCE_MAP[resource_name].keys()
    if "add_payload_keys" in resource_map_keys:
        desired_states.add("present")
    if "delete_arg_keys" in resource_map_keys:
        desired_states.add("absent")
    try:
        if len(NITRO_RESOURCE_MAP[resource_name]["enable_payload_keys"]) > 0:
            desired_states.add("enabled")
    except KeyError:
        pass
    try:
        if len(NITRO_RESOURCE_MAP[resource_name]["disable_payload_keys"]) > 0:
            desired_states.add("disabled")
    except KeyError:
        pass
    return desired_states
