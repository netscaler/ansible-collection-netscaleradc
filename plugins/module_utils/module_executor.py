# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
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
    delete_resource,
    disable_resource,
    enable_resource,
    get_bindings,
    get_netscaler_version,
    get_resource,
    get_valid_desired_states,
    save_config,
    unbind_resource,
    update_resource,
)
from .constants import NETSCALER_COMMON_ARGUMENTS, NETSCALER_NO_GET_RESOURCE
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
            # mutually_exclusive=[
            #     ("nitro_auth_token", "nitro_user"),
            #     ("nitro_auth_token", "nitro_pass"),
            # ],
            # required_together=[
            #     ("nitro_user", "nitro_pass"),
            # ],
            # required_one_of=[
            #     ("nitro_auth_token", "nitro_user"),
            #     ("nitro_auth_token", "nitro_pass"),
            # ],
        )

        self.client = NitroAPIClient(self.module)
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
        self.desired_bindings = []
        self.existing_resource = dict()

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        log(
            "DEBUG: All params (including non module-specific params) are: %s"
            % self.module.params
        )

        # Fiter out non-resource module params in the playbook such as `state`, `delegate_to`, `nitro_user`, `nitro_pass`, etc
        self._filter_resource_module_params()
        if not self.resource_name.endswith("_binding"):
            self._filter_desired_bindings()
        if self.resource_name not in NETSCALER_NO_GET_RESOURCE:
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
    def update_diff_list(self, existing=dict(), desired=dict(), delete=False, **kwargs):
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
                    self.desired_bindings.append(k)
        log(
            "DEBUG: Desired `%s` module specific bindings are: %s"
            % (self.resource_name, self.desired_bindings)
        )

    @trace
    def _filter_resource_module_params(self):
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
        log(
            "DEBUG: Desired `%s` module specific params are: %s"
            % (self.resource_name, self.resource_module_params)
        )

    @trace
    def get_existing_resource(self):
        get_args = {}
        for attr in NITRO_RESOURCE_MAP[self.resource_name]["get_arg_keys"]:
            if attr in self.resource_module_params:
                get_args[attr] = self.resource_module_params[attr]

        # binding resources require `filter` instead of `args` to uniquely identify a resource
        existing_resource = get_resource(
            self.client,
            resource_name=self.resource_name,
            resource_id=self.resource_id,
            args=get_args if not self.resource_name.endswith("_binding") else {},
            filter=get_args if self.resource_name.endswith("_binding") else {},
        )
        if len(existing_resource) > 1:
            msg = (
                "ERROR: Found more than one resource with the same primary key %s and get arguments %s"
                % (
                    self.resource_id,
                    get_args,
                )
            )
            self.return_failure(msg)

        self.existing_resource = existing_resource[0] if existing_resource else {}
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
        if attribute_type == "int":
            # convert the existing attribute type to int
            return int(existing_attribute_value) == int(module_params_attribute_value)
        elif attribute_type == "str":
            return str(existing_attribute_value) == str(module_params_attribute_value)

        return existing_attribute_value == module_params_attribute_value

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
            # if existing_attribute_value != module_params_attribute_value:
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
        self.get_existing_resource()
        self.update_diff_list(
            existing=self.existing_resource, desired=self.resource_module_params
        )
        if not self.existing_resource:
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
            # FIXME: Should we rollback create/update?
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
        self, binding_name, bindprimary_key, to_be_deleted_bindings, existing_bindings
    ):
        for d in list(to_be_deleted_bindings):
            deleting_binding = {}
            for e in existing_bindings:
                if d == e[bindprimary_key]:
                    deleting_binding = e
                    break
            if not deleting_binding:
                msg = (
                    "Binding %s not found in the existing resources. Continuing..." % d
                )
                log(msg)
                continue
            ok, err = unbind_resource(
                self.client,
                binding_name=binding_name,
                binding_module_params=deleting_binding,
            )
            if not ok:
                return False, err
            self.module_result["changed"] = True
            self.update_diff_list(
                custom_msg="-   %s--%s:%s DELETED" % (binding_name, self.resource_id, d)
            )
        return True, None

    @trace
    def add_bindings(
        self, binding_name, bindprimary_key, to_be_added_bindings, desired_bindings
    ):
        for b in list(to_be_added_bindings):
            desired_binding = {}
            for d in desired_bindings:
                if b == d[bindprimary_key]:
                    desired_binding = d
                    break
            if not desired_binding:
                msg = (
                    "Binding %s not found in the module_params" % b
                )  # This code should not hit
                return False, msg
            ok, err = bind_resource(
                self.client,
                binding_name=binding_name,
                binding_module_params=desired_binding,
            )
            if not ok:
                return False, err
            self.update_diff_list(
                custom_msg="+   %s--%s:%s ADDED" % (binding_name, self.resource_id, b)
            )
            self.module_result["changed"] = True
        return True, None

    @trace
    def update_bindings(
        self,
        binding_name,
        bindprimary_key,
        to_be_updated_bindings,
        desired_bindings,
        existing_bindings,
    ):
        for b in list(to_be_updated_bindings):
            desired_binding = {}
            for x in desired_bindings:
                if b == x[bindprimary_key]:
                    desired_binding = x
                    break

            existing_binding = {}
            for x in existing_bindings:
                if b == x[bindprimary_key]:
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

                ok, err = bind_resource(
                    self.client,
                    binding_name=binding_name,
                    binding_module_params=desired_binding,
                )
                if not ok:
                    self.return_failure(err)
                self.module_result["changed"] = True
                self.update_diff_list(
                    custom_msg="~   %s--%s:%s` UPDATED"
                    % (binding_name, self.resource_id, b)
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
        for binding_name in self.desired_bindings:
            self.sync_single_binding(binding_name)

    @trace
    def sync_single_binding(self, binding_name):
        bindprimary_key = NITRO_RESOURCE_MAP[binding_name]["bindprimary_key"]
        binding_module_params = self.module.params[binding_name]
        binding_mode = binding_module_params["mode"]
        log("INFO: Binding mode is `%s`" % binding_mode)
        desired_binding_members = binding_module_params["binding_members"]
        log("DEBUG: Desired binding members: %s" % desired_binding_members)

        if not isinstance(desired_binding_members, list):
            err = "`%s.binding_members` should be a `list`" % binding_name
            self.return_failure(err)

        existing_bindings = get_bindings(
            self.client,
            binding_name=binding_name,
            binding_id=self.resource_id,
        )
        log("DEBUG: Existing `%s` bindings: %s" % (binding_name, existing_bindings))

        desired_binding_members_bindprimary_keys = {
            x[bindprimary_key] for x in desired_binding_members
        }
        existing_binding_members_bindprimary_keys = {
            x[bindprimary_key] for x in existing_bindings
        }

        if self.module.params["state"] == "absent":
            # In `absent` state, we will delete all the existing bindings
            to_be_deleted_bindings = existing_binding_members_bindprimary_keys
            ok, err = self.delete_bindings(
                binding_name=binding_name,
                bindprimary_key=bindprimary_key,
                to_be_deleted_bindings=to_be_deleted_bindings,
                existing_bindings=existing_bindings,
            )
            if not ok:
                self.return_failure(err)
            return

        to_be_deleted_bindings = (
            existing_binding_members_bindprimary_keys
            - desired_binding_members_bindprimary_keys
        )
        to_be_added_bindings = (
            desired_binding_members_bindprimary_keys
            - existing_binding_members_bindprimary_keys
        )
        to_be_updated_bindings = (
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

            log("DEBUG: To be deleted bindings: %s" % to_be_deleted_bindings)
            log("DEBUG: To be added bindings: %s" % to_be_added_bindings)
            log("DEBUG: To be updated bindings: %s" % to_be_updated_bindings)

            if to_be_deleted_bindings:
                ok, err = self.delete_bindings(
                    binding_name=binding_name,
                    bindprimary_key=bindprimary_key,
                    to_be_deleted_bindings=to_be_deleted_bindings,
                    existing_bindings=existing_bindings,
                )
                if not ok:
                    self.return_failure(err)

            if to_be_added_bindings:
                ok, err = self.add_bindings(
                    binding_name=binding_name,
                    bindprimary_key=bindprimary_key,
                    to_be_added_bindings=to_be_added_bindings,
                    desired_bindings=desired_binding_members,
                )
                if not ok:
                    self.return_failure(err)

            if to_be_updated_bindings:
                ok, err = self.update_bindings(
                    binding_name=binding_name,
                    bindprimary_key=bindprimary_key,
                    to_be_updated_bindings=to_be_updated_bindings,
                    desired_bindings=desired_binding_members,
                    existing_bindings=existing_bindings,
                )
                if not ok:
                    self.return_failure(err)

        elif binding_mode == "bind":
            # In `bind` mode, we will only add the bindings specified in the playbook. If a binding already exists, we will update it

            log("DEBUG: To be added bindings: %s" % to_be_added_bindings)
            log("DEBUG: To be updated bindings: %s" % to_be_updated_bindings)

            if to_be_added_bindings:
                ok, err = self.add_bindings(
                    binding_name=binding_name,
                    bindprimary_key=bindprimary_key,
                    to_be_added_bindings=to_be_added_bindings,
                    desired_bindings=desired_binding_members,
                )
                if not ok:
                    self.return_failure(err)

            if to_be_updated_bindings:
                ok, err = self.update_bindings(
                    binding_name=binding_name,
                    bindprimary_key=bindprimary_key,
                    to_be_updated_bindings=to_be_updated_bindings,
                    desired_bindings=desired_binding_members,
                    existing_bindings=existing_bindings,
                )
                if not ok:
                    self.return_failure(err)

        elif binding_mode == "unbind":
            # In `unbind` mode, we will only delete the bindings specified in the playbook

            to_be_deleted_bindings = desired_binding_members_bindprimary_keys

            log("DEBUG: To be deleted bindings: %s" % to_be_deleted_bindings)

            if to_be_deleted_bindings:
                ok, err = self.delete_bindings(
                    binding_name=binding_name,
                    bindprimary_key=bindprimary_key,
                    to_be_deleted_bindings=to_be_deleted_bindings,
                    existing_bindings=existing_bindings,
                )
                if not ok:
                    self.return_failure(err)

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
    def main(self):
        try:
            if self.module.params["state"] in {"present", "enabled", "disabled"}:
                self.create_or_update()
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

            elif self.module.params["state"] in {"absent"}:
                if self.resource_primary_key:
                    # Bindings
                    if "bindings" in NITRO_RESOURCE_MAP[self.resource_name].keys():
                        self.sync_all_bindings()
                    self.delete()
                else:
                    # `primary_key` will not be present for `update-only` resources such as
                    # `sslparameter`, `lbparameter`, etc. Hence `DELETE` is not supported
                    # for such resources.
                    # FIXME: Should we `unset` the resource instead?
                    pass
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
            self.return_success()
        except Exception as e:
            msg = "Exception %s: %s" % (type(e), str(e))
            self.return_failure(msg)
