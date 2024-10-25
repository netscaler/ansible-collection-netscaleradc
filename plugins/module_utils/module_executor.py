# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import os

from ansible.module_utils.basic import AnsibleModule

from .client import NitroAPIClient
from .common import (
    adc_login,
    adc_logout,
    bind_resource,
    create_resource,
    create_resource_with_action,
    delete_resource,
    disable_resource,
    enable_resource,
    get_bindings,
    get_bindprimary_key,
    get_netscaler_version,
    get_resource,
    get_valid_desired_states,
    is_global_binding,
    is_resource_exists,
    is_singleton_resource,
    save_config,
    unbind_resource,
    update_resource,
)
from .constants import (
    ATTRIBUTES_NOT_PRESENT_IN_GET_RESPONSE,
    HTTP_RESOURCE_ALREADY_EXISTS,
    NETSCALER_COMMON_ARGUMENTS,
    NITRO_ATTRIBUTES_ALIASES,
)
from .decorators import trace
from .logger import log, loglines
from .nitro_resource_map import NITRO_RESOURCE_MAP


class ModuleExecutor(object):
    def __init__(self, resource_name, supports_check_mode=True):
        self.resource_name = resource_name
        if self.resource_name == "login":
            self.sessionid = ""
        log("DEBUG: Initializing ModuleExecutor for resource %s" % self.resource_name)
        self.valid_states = get_valid_desired_states(self.resource_name)
        self.supported_operations = NITRO_RESOURCE_MAP[self.resource_name][
            "_supported_operations"
        ]
        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )
        module_specific_arguments = NITRO_RESOURCE_MAP[self.resource_name][
            "readwrite_arguments"
        ]
        argument_spec = dict()
        argument_spec.update(NETSCALER_COMMON_ARGUMENTS)
        argument_spec.update(module_specific_arguments)
        module_state_argument = dict(
            state=dict(
                type="str",
                choices=list(self.valid_states),
                default="present",
            ),
        )
        argument_spec.update(module_state_argument)

        self.module = AnsibleModule(
            argument_spec=argument_spec,
            supports_check_mode=supports_check_mode,
            mutually_exclusive=[
                (
                    "managed_netscaler_instance_name",
                    "managed_netscaler_instance_ip",
                    "managed_netscaler_instance_id",
                ),
            ],
            required_together=[
                ("nitro_user", "nitro_pass"),
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

        self.netscaler_console_as_proxy_server = self.module.params[
            "netscaler_console_as_proxy_server"
        ]

        if not self.netscaler_console_as_proxy_server:
            for k in (
                "managed_netscaler_instance_name",
                "managed_netscaler_instance_ip",
                "managed_netscaler_instance_id",
                "managed_netscaler_instance_username",
                "managed_netscaler_instance_password",
            ):
                if self.module.params[k] is not None:
                    msg = (
                        "ERROR: You can only use %s with `netscaler_console_as_proxy_server=true`"
                        % k
                    )
                    self.return_failure(msg)

        if self.netscaler_console_as_proxy_server and self.resource_name in {
            "login",
            "logout",
        }:
            self.module.params["api_path"] = "nitro/v2/config"

        self.client = NitroAPIClient(self.module, self.resource_name)
        self.ns_major_version, self.ns_minor_version = get_netscaler_version(
            self.client
        )
        log(
            "INFO: NetScaler version: %s-%s"
            % (self.ns_major_version, self.ns_minor_version)
        )
        self.diff_dict = {}
        self.resource_primary_key = NITRO_RESOURCE_MAP[self.resource_name][
            "primary_key"
        ]
        if self.resource_primary_key == "":
            # For `unnamed` resources like `sslparameter`, `lbparameter` etc
            self.resource_id = ""
        else:
            self.resource_id = self.module.params[self.resource_primary_key]
        self.resource_module_params = {}
        self.desired_bindings = {}
        self.existing_resource = dict()

        log(
            "DEBUG: All params (including non module-specific params) are: %s"
            % self.module.params
        )

        # Fiter out non-resource module params in the playbook such as `state`, `delegate_to`, `nitro_user`, `nitro_pass`, etc
        self._filter_resource_module_params()
        if not self.resource_name.endswith("_binding"):
            self._filter_desired_bindings()
        if {"get", "get-byname", "get-all"} & set(self.supported_operations):
            self.get_existing_resource()

    @trace
    def return_success(self):
        if self.diff_dict:  # and self.module._diff:
            self.module_result["diff"] = self.diff_dict
            # self.module_result["diff"] = {
            #     "before": {"a":"b"},
            #     "after": {"a":"c"},
            #     "prepared": "prepared string",
            # }
        if self.resource_name == "login":
            self.module_result["sessionid"] = self.sessionid
        self.module.exit_json(**self.module_result)

    @trace
    def update_diff_list(self, existing=None, desired=None, delete=False, **kwargs):
        if existing is None:
            existing = {}
        if desired is None:
            desired = {}
        if "custom_msg" in kwargs:
            prepared_str = (
                self.diff_dict.get("prepared", "") + os.linesep + kwargs["custom_msg"]
            )
            self.diff_dict["prepared"] = prepared_str

        if existing or desired:
            self.diff_dict = {
                # prepare `before` dict from `existing` keys for the keys present in the `desired` dict
                "before": {k: v for k, v in existing.items() if k in desired.keys()},
                "after": {} if delete else desired,
            }

    @trace
    def return_failure(self, msg):
        self.module.fail_json(msg=msg, **self.module_result)

    @trace
    def _filter_desired_bindings(self):
        for k, v in self.module.params.items():
            if (
                k.endswith("_binding")
                and k
                in NITRO_RESOURCE_MAP[self.resource_name]["readwrite_arguments"].keys()
            ):
                if v:
                    self.desired_bindings.update({k: v})
        log(
            "DEBUG: Desired `%s` module specific bindings are: %s"
            % (self.resource_name, self.desired_bindings)
        )

    @trace
    def _add_nitro_attributes_aliases(self, payload):
        for k, v in payload.copy().items():
            if k in NITRO_ATTRIBUTES_ALIASES[self.resource_name]:
                alias_key = NITRO_ATTRIBUTES_ALIASES[self.resource_name][k]
                log(
                    "DEBUG: Found alias key `%s` for `%s`. Adding the alias key to resource_module_params"
                    % (alias_key, k)
                )
                payload[alias_key] = v
        return payload

    @trace
    def _filter_resource_module_params(self):
        log("DEBUG: self.module.params: %s" % self.module.params)
        for k, v in self.module.params.items():
            if (not k.endswith("_binding")) and (
                k
                in NITRO_RESOURCE_MAP[self.resource_name]["readwrite_arguments"].keys()
            ):
                # self.module.params is a dict of key:value pairs. If an attribute is not
                # defined in the playbook, it's value will be None. So, filter out those attributes.
                # Also, filter out attributes ending with `_binding` as they are handled separately
                if v is not None:
                    self.resource_module_params[k] = v

        if self.resource_name in NITRO_ATTRIBUTES_ALIASES:
            self.resource_module_params = self._add_nitro_attributes_aliases(
                self.resource_module_params
            )
        log(
            "DEBUG: Desired `%s` module specific params are: %s"
            % (self.resource_name, self.resource_module_params)
        )

    @trace
    def get_existing_resource(self):
        is_exist, existing_resource = get_resource(
            self.client,
            resource_name=self.resource_name,
            resource_id=self.resource_id,
            resource_module_params=self.resource_module_params,
        )
        if is_exist is False:
            return {}
        if len(existing_resource) > 1:
            msg = (
                "ERROR: For resource `%s` Found more than one resource with the same primary key `%s` and resource_module_params %s"
                % (
                    self.resource_name,
                    self.resource_id,
                    self.resource_module_params,
                )
            )
            self.return_failure(msg)

        self.existing_resource = existing_resource[0]

        if self.resource_name in NITRO_ATTRIBUTES_ALIASES:
            self.existing_resource = self._add_nitro_attributes_aliases(
                self.existing_resource
            )

        # The below return is not mandatory. However, required for debugging purpose
        return self.existing_resource

    @trace
    def is_attribute_equal(
        self, attribute_name, existing_attribute_value, module_params_attribute_value
    ):
        # existing_attribute value will be None when there is no existing attribute for the resource.
        if existing_attribute_value is None:
            return False
        # check their type and convert the existing attribute type to the module params attribute type
        attribute_type = NITRO_RESOURCE_MAP[self.resource_name]["readwrite_arguments"][
            attribute_name
        ]["type"]
        if attribute_type == "raw":
            # for "raw" type, compare as string values
            return str(existing_attribute_value) == str(module_params_attribute_value)
        if attribute_type == "int":
            return int(existing_attribute_value) == int(module_params_attribute_value)
        if attribute_type == "float":
            return float(existing_attribute_value) == float(
                module_params_attribute_value
            )
        if attribute_type == "str":
            # NITRO is case insensitive for string attribute values. So, convert both to lower case and compare
            return (
                str(existing_attribute_value).lower()
                == str(module_params_attribute_value).lower()
            )
        # By default, compare as string values
        return str(existing_attribute_value) == str(module_params_attribute_value)

    @trace
    def is_resource_identical(self):
        """
        check the diff between module_params and the target resource.
        If both are same, don't do anything (idempotency)
        """
        diff_list = []
        immutable_resource_module_params = []
        # immutable_resource_module_params contains those elemets which are changed values in the playbook but are not updateable
        for attr in self.resource_module_params.keys():
            existing_attribute_value = self.existing_resource.get(attr)
            module_params_attribute_value = self.resource_module_params.get(attr)

            # If the attribute is a password, skip it as the NITRO returns None for the existing password attributes
            if attr in NITRO_RESOURCE_MAP[self.resource_name]["password_keys"]:
                continue
            try:
                if attr in ATTRIBUTES_NOT_PRESENT_IN_GET_RESPONSE[self.resource_name]:
                    continue
            except KeyError:
                pass
            if not self.is_attribute_equal(
                attr, existing_attribute_value, module_params_attribute_value
            ):
                str_tuple = (
                    attr,
                    type(module_params_attribute_value),
                    module_params_attribute_value,
                    type(existing_attribute_value),
                    existing_attribute_value,
                )
                msg_str = (
                    "Attribute `%s` differs. Desired: (%s) %s. Existing: (%s) %s"
                    % str_tuple
                )
                diff_list.append(msg_str)
                log(msg_str)
                # Also append changed values to the non updateable list
                if attr in NITRO_RESOURCE_MAP[self.resource_name]["immutable_keys"]:
                    immutable_resource_module_params.append(attr)

        self.module_result["diff_list"] = diff_list
        if not self.module_result["diff_list"]:
            del self.module_result["diff_list"]
        if immutable_resource_module_params != []:
            msg = (
                "Cannot change value for the following non-updateable attributes %s"
                % immutable_resource_module_params
            )
            self.return_failure(msg)

        return False if diff_list else True

    @trace
    def create_or_update(self):
        self.update_diff_list(
            existing=self.existing_resource, desired=self.resource_module_params
        )
        if not self.existing_resource and "add" in self.supported_operations:
            self.module_result["changed"] = True
            log(
                "INFO: Resource %s:%s does not exist. Will be CREATED."
                % (
                    self.resource_name,
                    self.resource_id,
                )
            )
            ok, err = create_resource(
                self.client, self.resource_name, self.resource_module_params
            )
            if not ok:
                self.return_failure(err)

            # There can be module_params in the playbook which are not part of `add_payload_keys`,
            # but part of `update_payload_keys` in the NITRO_RESOURCE_MAP
            # For example, `ntpserver` resource has `preferredntpserver` attribute
            # which is not part of `add_payload_keys`, but part of `update_payload_keys`.
            # If `preferredntpserver` is also part of the playbook-task, to make it true desired state,
            # we will update the resource with the module_params
            add_payload_keys = NITRO_RESOURCE_MAP[self.resource_name][
                "add_payload_keys"
            ]
            update_payload_keys = NITRO_RESOURCE_MAP[self.resource_name][
                "update_payload_keys"
            ]

            keys_in_upload_payload_and_not_in_add_payload = set(
                update_payload_keys
            ) - set(add_payload_keys)

            is_module_params_contain_update_params = bool(
                set(keys_in_upload_payload_and_not_in_add_payload).intersection(
                    set(self.resource_module_params.keys())
                )
            )

            if is_module_params_contain_update_params:
                log(
                    "INFO: module_params has keys %s which are not part of `add_payload_keys`. Hence updating the resource again"
                    % keys_in_upload_payload_and_not_in_add_payload
                )
                ok, err = update_resource(
                    self.client, self.resource_name, self.resource_module_params
                )
                if not ok:
                    self.return_failure(err)
        else:
            # Update only if resource is not identical (idempotent)
            if self.is_resource_identical():
                log(
                    "INFO: Resource `%s:%s` exists and is identical. No change required."
                    % (
                        self.resource_name,
                        self.resource_id,
                    )
                )
            else:
                self.module_result["changed"] = True
                if self.resource_name.endswith("_binding"):
                    # Generally bindings are not updated. They are removed and added again.
                    log(
                        "INFO: Resource %s:%s exists and is different. Will be REMOVED and ADDED."
                        % (self.resource_name, self.resource_id)
                    )
                    self.delete()
                    ok, err = create_resource(
                        self.client, self.resource_name, self.resource_module_params
                    )
                else:
                    log(
                        "INFO: Resource %s:%s exists. Will be UPDATED."
                        % (
                            self.resource_name,
                            self.resource_id,
                        )
                    )
                    ok, err = update_resource(
                        self.client, self.resource_name, self.resource_module_params
                    )
                if not ok:
                    self.return_failure(err)

    @trace
    def enable_or_disable(self, desired_state):
        not_implemented_msg = (
            "--diff mode is not implemented for enable/disable operations"
        )
        self.update_diff_list(custom_msg=not_implemented_msg)
        self.module_result["changed"] = True
        if desired_state == "enabled":
            ok, err = enable_resource(
                self.client, self.resource_name, self.resource_module_params
            )
        else:
            ok, err = disable_resource(
                self.client, self.resource_name, self.resource_module_params
            )
        if not ok:
            self.return_failure(err)

    @trace
    def delete(self):
        self.update_diff_list(
            self.existing_resource, self.resource_module_params, delete=True
        )
        if self.existing_resource:
            self.module_result["changed"] = True
            ok, err = delete_resource(
                self.client, self.resource_name, self.resource_module_params
            )
            if not ok:
                self.return_failure(err)

    @trace
    def delete_bindings(
        self,
        binding_name,
        bindings_to_delete,
    ):
        for b in bindings_to_delete:
            if is_resource_exists(self.client, binding_name, b):
                ok, err = unbind_resource(
                    self.client,
                    binding_name=binding_name,
                    binding_module_params=b,
                )
                if not ok:
                    self.return_failure(err)
                self.module_result["changed"] = True
                self.update_diff_list(
                    custom_msg="-   DELETED %s--%s" % (binding_name, b)
                )

    @trace
    def add_bindings(self, binding_name, desired_bindings):
        for b in desired_bindings:
            ok, err = bind_resource(
                self.client,
                binding_name=binding_name,
                binding_module_params=b,
            )
            if not ok:
                self.return_failure(err)
            self.update_diff_list(custom_msg="+   ADDED %s--%s" % (binding_name, b))
        self.module_result["changed"] = True

    @trace
    def update_bindings(
        self,
        binding_name,
        to_be_updated_bindprimary_keys,
        desired_bindings,
        existing_bindings,
    ):
        for b in list(to_be_updated_bindprimary_keys):
            desired_binding = {}
            for x in desired_bindings:
                if b == x[get_bindprimary_key(binding_name, x)]:
                    desired_binding = x
                    break

            existing_binding = {}
            for x in existing_bindings:
                if b == x[get_bindprimary_key(binding_name, x)]:
                    existing_binding = x
                    break

            if not self.is_binding_identical(
                binding_name, existing_binding, desired_binding
            ):
                log(
                    "INFO: Resource %s:%s's binding %s:%s exists and is different. Will be REMOVED and ADDED."
                    % (
                        self.resource_name,
                        self.resource_id,
                        binding_name,
                        b,
                    )
                )
                ok, err = unbind_resource(
                    self.client,
                    binding_name=binding_name,
                    binding_module_params=existing_binding,
                )
                if not ok:
                    self.return_failure(err)

                self.update_diff_list(
                    custom_msg="-   DELETED %s--%s" % (binding_name, existing_binding)
                )

                ok, err = bind_resource(
                    self.client,
                    binding_name=binding_name,
                    binding_module_params=desired_binding,
                )
                if not ok:
                    self.return_failure(err)

                self.module_result["changed"] = True

                self.update_diff_list(
                    custom_msg="+   ADDED %s--%s" % (binding_name, desired_binding)
                )

            else:
                log(
                    "INFO: Resource %s:%s's binding %s:%s exists and is identical. No change required."
                    % (
                        self.resource_name,
                        self.resource_id,
                        binding_name,
                        b,
                    )
                )
        return True, None

    @trace
    def sync_all_bindings(self):
        for binding_name in self.desired_bindings.keys():
            self.sync_single_binding(binding_name)

    @trace
    def sync_single_binding(self, binding_name):
        is_exists, existing_bindings = get_bindings(
            self.client,
            binding_name=binding_name,
            binding_id=self.resource_id,
            resource_module_params=self.resource_module_params,
        )
        log("DEBUG: Existing `%s` bindings: %s" % (binding_name, existing_bindings))

        if self.module.params["state"] == "absent":
            # In `absent` state, we will delete all the existing bindings
            self.delete_bindings(
                binding_name=binding_name,
                bindings_to_delete=existing_bindings,
            )
            return

        binding_module_params = self.module.params[binding_name]
        binding_mode = binding_module_params["mode"]
        desired_binding_members = binding_module_params["binding_members"]
        log("INFO: Binding mode is `%s`" % binding_mode)
        log("DEBUG: Desired binding members: %s" % desired_binding_members)

        if not isinstance(desired_binding_members, list):
            err = "`%s.binding_members` should be a `list`" % binding_name
            self.return_failure(err)

        desired_binding_members_bindprimary_keys = {
            x[get_bindprimary_key(binding_name, x)] for x in desired_binding_members
        }
        existing_binding_members_bindprimary_keys = {
            x[get_bindprimary_key(binding_name, x)] for x in existing_bindings
        }
        log(
            "DEBUG: Existing binding members bindprimary keys: %s"
            % existing_binding_members_bindprimary_keys
        )
        log(
            "DEBUG: Desired binding members bindprimary keys: %s"
            % desired_binding_members_bindprimary_keys
        )
        to_be_deleted_bindprimary_keys = (
            existing_binding_members_bindprimary_keys
            - desired_binding_members_bindprimary_keys
        )
        to_be_added_bindprimary_keys = (
            desired_binding_members_bindprimary_keys
            - existing_binding_members_bindprimary_keys
        )
        to_be_updated_bindprimary_keys = (
            desired_binding_members_bindprimary_keys
            & existing_binding_members_bindprimary_keys
        )

        if binding_mode == "desired":
            # In `desired` mode, we will check if the existing bindings are identical to the desired
            # bindings, if not, we will delete the existing bindings and add the desired bindings.
            # If they are identical, we will do nothing. If there are no existing bindings,
            # we will add the desired bindings. If there are no desired bindings,
            # we will delete the existing bindings. If there are no existing and desired bindings,
            # we will do nothing.

            log(
                "INFO: to_be_deleted_bindprimary_keys bindings: %s"
                % to_be_deleted_bindprimary_keys
            )
            log(
                "INFO: to_be_added_bindprimary_keys bindings: %s"
                % to_be_added_bindprimary_keys
            )
            log(
                "INFO: to_be_updated_bindprimary_keys bindings: %s"
                % to_be_updated_bindprimary_keys
            )

            if to_be_added_bindprimary_keys:
                self.add_bindings(
                    binding_name=binding_name,
                    desired_bindings=[
                        x for x in desired_binding_members
                        if x[get_bindprimary_key(binding_name, x)] in to_be_added_bindprimary_keys
                    ],
                )

            # If there is any default bindings, after adding the custom bindings, the default bindings will be deleted automatically
            # Hence GET the existing bindings again and construct the `to_be_deleted_bindprimary_keys` list
            is_exists, existing_bindings = get_bindings(
                self.client,
                binding_name=binding_name,
                binding_id=self.resource_id,
                resource_module_params=self.resource_module_params,
            )
            existing_binding_members_bindprimary_keys = {
                x[get_bindprimary_key(binding_name, x)] for x in existing_bindings
            }
            to_be_deleted_bindprimary_keys = (
                existing_binding_members_bindprimary_keys
                - desired_binding_members_bindprimary_keys
            )
            log(
                "INFO: New to_be_deleted_bindprimary_keys bindings: %s"
                % to_be_deleted_bindprimary_keys
            )

            to_be_deleted_bindings = []
            for b in existing_bindings:
                if (
                    b[get_bindprimary_key(binding_name, b)]
                    in to_be_deleted_bindprimary_keys
                ):
                    to_be_deleted_bindings.append(b)

            if to_be_deleted_bindprimary_keys:
                self.delete_bindings(
                    binding_name=binding_name,
                    bindings_to_delete=to_be_deleted_bindings,
                )

            if to_be_updated_bindprimary_keys:
                self.update_bindings(
                    binding_name=binding_name,
                    to_be_updated_bindprimary_keys=to_be_updated_bindprimary_keys,
                    desired_bindings=desired_binding_members,
                    existing_bindings=existing_bindings,
                )

        elif binding_mode == "bind":
            # In `bind` mode, we will only add the bindings specified in the playbook. If a binding already exists, we will update it

            log("INFO: To be added bindings: %s" % to_be_added_bindprimary_keys)
            log("INFO: To be updated bindings: %s" % to_be_updated_bindprimary_keys)

            if to_be_added_bindprimary_keys:
                self.add_bindings(
                    binding_name=binding_name,
                    desired_bindings=desired_binding_members,
                )

            if to_be_updated_bindprimary_keys:
                self.update_bindings(
                    binding_name=binding_name,
                    to_be_updated_bindprimary_keys=to_be_updated_bindprimary_keys,
                    desired_bindings=desired_binding_members,
                    existing_bindings=existing_bindings,
                )

        elif binding_mode == "unbind":
            # In `unbind` mode, we will only delete the bindings specified in the playbook-task
            log("INFO: To be deleted bindings: %s" % desired_binding_members)

            self.delete_bindings(
                binding_name=binding_name,
                bindings_to_delete=desired_binding_members,
            )

    @trace
    def is_binding_identical(
        self, binding_name, existing_binding_members, desired_binding_members
    ):
        """
        Check if the existing binding is identical to the desired binding
        """
        binding_readwrite_arguments = NITRO_RESOURCE_MAP[binding_name][
            "readwrite_arguments"
        ]
        for k, v in desired_binding_members.items():
            # This is because, NITRO returns all values as strings!
            if k not in binding_readwrite_arguments.keys():
                self.return_failure(
                    "ERROR: Unknown binding member `%s` for binding `%s`. Valid binding members are %s"
                    % (k, binding_name, binding_readwrite_arguments.keys())
                )
            if binding_readwrite_arguments[k]["type"] == "int":
                if int(v) != int(existing_binding_members[k]):
                    return False
            elif binding_readwrite_arguments[k]["type"] == "float":
                if float(v) != float(existing_binding_members[k]):
                    return False
            else:
                if v != existing_binding_members[k]:
                    return False
        return True

    @trace
    def change_password(self):
        try:
            if self.module.check_mode:
                self.module_result["changed"] = True
                self.return_success()
            else:
                if self.resource_module_params["first_boot"]:
                    ok, err = adc_login(
                        self.client,
                        self.resource_module_params["username"],
                        self.resource_module_params["password"],
                        self.resource_module_params["new_password"],
                    )
                else:
                    # set system user USERNAME -password NEW_PASSWORD
                    self.resource_module_params[
                        "password"
                    ] = self.resource_module_params["new_password"]
                    ok, err = update_resource(
                        self.client, "systemuser", self.resource_module_params
                    )
                if not ok:
                    self.return_failure(err)

                self.module_result["changed"] = True
                self.return_success()
        except Exception as e:
            msg = "Exception %s: %s" % (type(e), str(e))
            self.return_failure(msg)

    @trace
    def login(self):
        try:
            if self.module.check_mode:
                self.sessionid = "check_mode_sessionid"
                self.module_result["changed"] = True
                self.return_success()
            else:
                ok, response_body = adc_login(
                    self.client,
                    self.resource_module_params["username"],
                    self.resource_module_params["password"],
                )
                if not ok:
                    self.return_failure(response_body)

                self.module_result["changed"] = True
                if self.netscaler_console_as_proxy_server:
                    self.sessionid = response_body[self.resource_name][0]["sessionid"]
                else:
                    self.sessionid = response_body["sessionid"]
                self.return_success()
        except Exception as e:
            msg = "Exception %s: %s" % (type(e), str(e))
            self.return_failure(msg)

    @trace
    def logout(self):
        try:
            if self.module.check_mode:
                self.module_result["changed"] = True
                self.return_success()
            else:
                ok, response_body = adc_logout(self.client)
                if not ok:
                    self.return_failure(response_body)

                self.module_result["changed"] = True
                self.return_success()
        except Exception as e:
            msg = "Exception %s: %s" % (type(e), str(e))
            self.return_failure(msg)

    @trace
    def act_on_resource(self, action):
        self.module_result["changed"] = True
        ok, err = create_resource_with_action(
            self.client,
            self.resource_name,
            self.resource_module_params,
            action=action,
        )
        if ok:
            if (
                "status_code" in err
                and err["status_code"] == HTTP_RESOURCE_ALREADY_EXISTS
            ):
                self.module_result["changed"] = False
        else:
            self.return_failure(err)

    @trace
    def config_save(self):
        all = False
        if (
            "all" in self.resource_module_params
            and self.resource_module_params["all"] is True
        ):
            all = True
        ok, err = save_config(self.client, all)
        if not ok:
            self.return_failure(err)
        self.module_result["changed"] = True
        self.update_diff_list(custom_msg="+   CONFIG SAVED")
        self.return_success()

    @trace
    def force(self):
        # resources like hasync, hafailover, clustersync have `force` action
        self.act_on_resource(action="force")
        self.module_result["changed"] = True
        self.update_diff_list(
            custom_msg="+   %s applied" % (self.resource_name.upper())
        )
        self.return_success()

    @trace
    def main(self):
        try:
            if self.module.params["state"] in {"present", "enabled", "disabled"}:
                if (
                    "add" in self.supported_operations
                    or "update" in self.supported_operations
                ):
                    self.create_or_update()
                    if "linkcertkeyname" in self.resource_module_params:
                        self.act_on_resource(action="link")
                if self.module.params["state"] in {"enabled", "disabled"}:
                    if self.module.check_mode:
                        log(
                            "WARNING: --check mode not implemented for state=%s"
                            % self.module.params["state"]
                        )
                    else:
                        self.enable_or_disable(self.module.params["state"])
                # Bindings
                if "bindings" in NITRO_RESOURCE_MAP[self.resource_name].keys():
                    self.sync_all_bindings()

            elif self.module.params["state"] in {
                "created",
                "imported",
                "flushed",
                "switched",
                "unset",
            }:
                state_action_map = {
                    "created": "create",
                    "imported": "import",
                    "flushed": "flush",
                    "switched": "switch",
                    "unset": "unset",
                }
                self.act_on_resource(
                    action=state_action_map[self.module.params["state"]]
                )
            elif self.module.params["state"] in {"absent"}:
                if self.resource_primary_key:
                    # Bindings
                    if (
                        "bindings" in NITRO_RESOURCE_MAP[self.resource_name].keys()
                        and NITRO_RESOURCE_MAP[self.resource_name]["bindings"]
                    ):
                        self.sync_all_bindings()
                    # FIXME: commenting the below code as we cannot achieve idempotency for `linkcertkeyname` attribute
                    # if "linkcertkeyname" in self.resource_module_params:
                    #     self.act_on_resource(action="unlink")
                    self.delete()
                else:
                    # `primary_key` will not be present for

                    # 1. `update-only` resources such as `sslparameter`, `lbparameter`, etc. Hence `DELETE` is not supported
                    # 2. Few other resources -- `appfwlearningdata`, `application`, `bridgetable`,
                    #   `gslbldnsentry`, `locationfile`, `locationfile6`, `routerdynamicrouting`, `sslcertbundle`,
                    #   `sslcertfile`, `sslcrlfile`, `ssldhfile`, `sslkeyfile`, `systementitydata` and global bindings
                    #   FIXME: challenge is there is no `primary_key` and in most cases `get_args_keys`.
                    #   How can we get the exact resource to GET before DELETE for itempotency?
                    if is_global_binding(self.resource_name):
                        self.delete()
                    elif is_singleton_resource(self.resource_name):
                        if "delete" in self.supported_operations:
                            self.delete()
                        else:
                            msg = (
                                "ERROR: For now, `state=absent` is not supported for the resource `%s`. \
                                    Please raise an issue at https://github.com/netscaler/ansible-collection-netscaleradc/issues"
                                % self.resource_name
                            )
                            self.return_failure(msg)
                    elif NITRO_RESOURCE_MAP[self.resource_name]["delete_arg_keys"]:
                        self.delete()
                    else:
                        msg = (
                            "ERROR: `state=absent` is not supported for resource `%s`"
                            % self.resource_name
                        )
                        self.return_failure(msg)
            else:
                msg = "Unknown state `%s`. Valid states are %s" % (
                    self.module.params["state"],
                    self.valid_states,
                )
                self.return_failure(msg)

            if self.module.params["save_config"] and self.module_result["changed"]:
                ok, err = save_config(self.client)
                if not ok:
                    self.return_failure(err)
                self.update_diff_list(custom_msg="+   CONFIG SAVED")
            self.return_success()
        except Exception as e:
            msg = "Exception %s: %s" % (type(e), str(e))
            self.return_failure(msg)
