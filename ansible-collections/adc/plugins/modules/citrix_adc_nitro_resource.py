#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (c) 2018 Citrix Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: citrix_adc_nitro_resource
short_description: Manage NITRO resources
description:
    - Manage NITRO resources
    - Implements full lifecycle of nitro resource.

version_added: "1.0.0"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)

options:

    state:
        description:
            - state of the resource
        choices:
            - present
            - absent
        default: present

    workflow:
        description:
            - Workflow options
        type: dict
        suboptions:
            lifecycle:
                description:
                    - Describe the lifecycle type of this object
                    - >-
                        The lifecyle value determines how the resource will be identified as existing or non existing
                        whether the attributes of the object need to be updated if existing and
                        how to create and delete a particular object.
                choices:
                    - 'object'
                    - 'binding'
                    - 'bindings_list'
                    - 'non_updateable_object'
            endpoint:
                description:
                    - NITRO endpoint for the object
            resource_missing_errorcode:
                description:
                    - NITRO response code that is returned when the resource cannot be retrieved
            non_updateable_attributes:
                description:
                    - Non updateable attributes
                type: list
            allow_recreate:
                description:
                    - Whether to allow deletion and recreation of the resource
                    - Relevant only for the object lifecycle
            primary_id_attribute:
                description:
                    - Primary id attribute
            delete_id_attributes:
                description:
                    - Attributes list which identify the resource uniquely when deleting

    resource:
        type: dict
        description:
            - Dictionary containing the resource attributes
            - Contents of the dictionary differ depending on which specific NITRO object is configured.

extends_documentation_fragment: citrix.adc.citrixadc
'''

EXAMPLES = '''
'''

RETURN = '''
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

msg:
    description: Message detailing the failure reason
    returned: failure
    type: str
    sample: "Action does not exist"
'''

import copy
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.citrix.adc.plugins.module_utils.citrix_adc import (
    NitroResourceConfig,
    NitroException,
    netscaler_common_arguments,
    log,
    loglines,
    NitroAPIFetcher
)


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.fetcher = NitroAPIFetcher(self.module)

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

        self.lifecycle = self.module.params['workflow']['lifecycle']

        self.retrieved_object = None
        self.configured_object = self.module.params['resource']

        self.endpoint = self.module.params['workflow'].get('endpoint')

        self.differing_attributes = []

        # Parse non updateable attributes
        self.non_updateable_attributes = self.module.params['workflow'].get('non_updateable_attributes')
        if self.non_updateable_attributes is None:
            self.non_updateable_attributes = []

        id_key = self.module.params['workflow'].get('primary_id_attribute')
        if id_key is not None:
            self.id = self.module.params['resource'][id_key]
        else:
            self.id = None

        log('self.id %s' % self.id)

        # Parse delete id attributes
        self.delete_id_attributes = self.module.params['workflow'].get('delete_id_attributes')
        if self.delete_id_attributes is None:
            self.delete_id_attributes = []

    def resource_exists(self):
        log('ModuleExecutor.resource_exists()')
        if self.lifecycle == 'object':
            return self.object_exists()
        elif self.lifecycle == 'binding':
            return self.binding_exists()
        elif self.lifecycle == 'bindings_list':
            return self.bindings_list_exists()
        elif self.lifecycle == 'non_updateable_object':
            return self.non_updateable_object_exists()
        else:
            msg = 'Unrecognized lifecycle value "%s"' % self.lifecycle
            self.module.fail_json(msg=msg, **self.module_result)

    def resource_identical(self):
        log('ModuleExecutor.resource_identical()')
        if self.lifecycle == 'object':
            return self.object_identical()
        elif self.lifecycle == 'binding':
            return self.binding_identical()
        elif self.lifecycle == 'bindings_list':
            return self.bindings_list_identical()
        elif self.lifecycle == 'non_updateable_object':
            return self.non_updateable_object_identical()

    def resource_create(self):
        log('ModuleExecutor.resource_create()')
        if self.lifecycle == 'object':
            self.object_create()
        elif self.lifecycle == 'binding':
            self.binding_create()
        elif self.lifecycle == 'bindings_list':
            self.bindings_list_create()
        elif self.lifecycle == 'non_updateable_object':
            return self.non_updateable_object_create()

    def resource_update(self):
        log('ModuleExecutor.resource_update()')
        if self.lifecycle == 'object':
            self.object_update()
        elif self.lifecycle == 'binding':
            self.binding_update()
        elif self.lifecycle == 'bindings_list':
            self.bindings_list_update()
        elif self.lifecycle == 'non_updateable_object':
            return self.non_updateable_object_update()

    def resource_delete(self):
        log('ModuleExecutor.resource_delete()')
        if self.lifecycle == 'object':
            self.object_delete()
        elif self.lifecycle == 'binding':
            self.binding_delete()
        elif self.lifecycle == 'bindings_list':
            self.bindings_list_delete()
        elif self.lifecycle == 'non_updateable_object':
            return self.non_updateable_object_delete()

    def binding_matches_id_attributes(self, binding):
        log('ModuleExecutor.binding_matches_id_attributes()')
        retval = True
        id_keys = []
        id_keys.append(self.module.params['workflow']['primary_id_attribute'])
        id_keys.extend(self.module.params['workflow']['delete_id_attributes'])

        for attribute in self.module.params['resource'].keys():
            if attribute in id_keys:
                configured_value = self.module.params['resource'][attribute]
                retrieved_value = binding.get(attribute)
                if configured_value != retrieved_value:
                    log('Non matching id attribute %s' % attribute)
                    retval = False

        return retval

    def binding_exists(self):
        log('ModuleExecutor.binding_exists()')

        result = self.fetcher.get(self.endpoint, self.id)

        log('get result %s' % result)

        if result['nitro_errorcode'] == 0:
            if self.endpoint not in result['data']:
                return False

            objects_returned = result['data'][self.endpoint]
            matching_objects = []

            # Compare the present id attributes
            for object in objects_returned:
                if self.binding_matches_id_attributes(object):
                    matching_objects.append(object)

            if len(matching_objects) == 0:
                return False
            elif len(matching_objects) == 1:
                self.retrieved_object = matching_objects[0]
                return True
            elif len(matching_objects) > 1:
                msg = 'Found multiple matching objects for binding'
                self.module.fail_json(msg=msg, **self.module_result)
        elif result['nitro_errorcode'] == self.module.params['workflow']['bound_resource_missing_errorcode']:
            return False
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def binding_identical(self):
        log('ModuleExecutor.binding_identical()')
        return self.object_identical()

    def binding_create(self):
        log('ModuleExecutor.binding_create()')

        attributes = self.module.params['resource']

        put_data = {
            self.endpoint: attributes
        }

        log('request put data: %s' % put_data)

        result = self.fetcher.put(put_data=put_data, resource=self.endpoint)

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def binding_update(self):
        log('ModuleExecutor.binding_update()')
        self.binding_delete()
        self.binding_create()

    def binding_delete(self):
        log('ModuleExecutor.binding_delete()')

        args = {}
        for key in self.module.params['workflow']['delete_id_attributes']:
            if key in self.configured_object:
                args[key] = self.configured_object[key]

        result = self.fetcher.delete(resource=self.endpoint, id=self.id, args=args)
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def bindings_list_exists(self):
        log('ModuleExecutor.bindings_list_exists()')
        return self.bindings_list_identical()

    def bindings_list_identical(self):
        log('ModuleExecutor.bindings_list_identical()')

        configured_bindings = self.configured_object['bindings_list']

        self.key_attributes = copy.deepcopy(self.module.params['workflow']['binding_workflow']['delete_id_attributes'])
        self.key_attributes.insert(0, self.module.params['workflow']['binding_workflow']['primary_id_attribute'])

        # Sanity check that at least one item is defined in bindings_list
        if len(configured_bindings) == 0:
            msg = 'Bindings list must have at least one item.'
            self.module.fail_json(msg=msg, **self.module_result)
        # Fallthrough

        # Sanity check that all bindings have uniform resource attribute keys
        key_tuples = []
        for binding in configured_bindings:
            attribute_keys_present = list(frozenset(binding.keys()) & frozenset(self.key_attributes))
            key_tuple = tuple(sorted(attribute_keys_present))
            key_tuples.append(key_tuple)

        key_tuple_set = frozenset(key_tuples)
        log('key_tuple_set %s' % key_tuple_set)
        if len(key_tuple_set) > 1:
            key_tuples = [item for item in key_tuple_set]
            msg = 'Bindings list key attributes are not uniform. Attribute key sets found %s' % key_tuples
            self.module.fail_json(msg=msg, **self.module_result)

        # Fallthrough

        # Sanity check that all primary ids are one and the same
        primary_id_key = self.module.params['workflow']['binding_workflow']['primary_id_attribute']
        primary_ids_list = [item[primary_id_key] for item in configured_bindings]
        primary_ids_set = frozenset(primary_ids_list)
        log('primary_ids_set %s' % primary_ids_set)
        if len(primary_ids_set) > 1:
            keys = [item for item in primary_ids_set]
            msg = 'Need to have only one primary id value. Found: %s' % keys
            self.module.fail_json(msg=msg, **self.module_result)

        # Fallthrough

        # Get existing bindings
        self.id = list(primary_ids_set)[0]
        self.endpoint = self.module.params['workflow']['binding_workflow']['endpoint']

        result = self.fetcher.get(self.endpoint, self.id)

        log('get result %s' % result)

        existing_bindings = []
        if result['nitro_errorcode'] == 0:
            if self.endpoint not in result['data']:
                existing_bindings = []
            else:
                existing_bindings = result['data'][self.endpoint]

        elif result['nitro_errorcode'] == self.module.params['workflow']['binding_workflow']['bound_resource_missing_errorcode']:
            existing_bindings = []
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

        # Construct the dictionaries keyed by tuple of key attributes
        # First attribute must be the primary id attribute
        self.key_attributes_present = []
        for item in self.key_attributes:
            if item in list(key_tuple_set)[0]:
                self.key_attributes_present.append(item)

        self.configured_bindings_dict = {}
        for binding in configured_bindings:
            binding_key = self._get_binding_key_tuple(binding)

            if binding_key in self.configured_bindings_dict:
                msg = 'Found duplicate key for configured bindings %s' % (binding_key,)
                self.module.fail_json(msg=msg, **self.module_result)

            log('Configured binding id %s registered to dict' % (binding_key,))
            self.configured_bindings_dict[binding_key] = binding

        self.existing_bindings_dict = {}

        for binding in existing_bindings:
            binding_key = self._get_binding_key_tuple(binding)

            if binding_key in self.existing_bindings_dict:
                msg = 'Found duplicate key for existing bindings %s' % (binding_key,)
                self.module.fail_json(msg=msg, **self.module_result)

            log('Existing binding id %s registered to dict' % (binding_key,))
            self.existing_bindings_dict[binding_key] = binding

        # Calculate to delete keys
        self.to_delete_keys = []
        for existing_key in self.existing_bindings_dict:
            if existing_key not in self.configured_bindings_dict:
                log('Existing binding key marked for delete %s' % (existing_key,))
                self.to_delete_keys.append(existing_key)

        # Calculate to update keys
        self.to_update_keys = []
        for existing_key in self.existing_bindings_dict:
            if existing_key in self.configured_bindings_dict:
                configured = self.configured_bindings_dict[existing_key]
                existing = self.existing_bindings_dict[existing_key]
                if not self._binding_list_item_identical_to_configured(configured, existing):
                    log('Existing binding key marked for update %s' % (existing_key,))
                    self.to_update_keys.append(existing_key)

        # Calculate to create keys
        self.to_create_keys = []
        for configured_key in self.configured_bindings_dict:
            if configured_key not in self.existing_bindings_dict:
                log('Configured binding key marked for create %s' % (configured_key,))
                self.to_create_keys.append(configured_key)

        # Calculate all changes
        all_change_keys = self.to_create_keys + self.to_update_keys + self.to_delete_keys
        if len(all_change_keys) == 0:
            return True
        else:
            return False

    def _get_binding_key_tuple(self, binding_dict):
        log('ModuleExecutor._get_binding_key_tuple()')
        ret_val = []
        # Order of attribute values is determined by ordering of self.key_attributes_present
        for attribute in self.key_attributes_present:
            if attribute in binding_dict:
                attribute_value = binding_dict[attribute]
                ret_val.append(attribute_value)
        return tuple(ret_val)

    def _binding_list_item_identical_to_configured(self, configured_dict, retrieved_dict):
        log('ModuleExecutor._binding_list_item_identical_to_configured()')
        ret_val = True

        for attribute in configured_dict.keys():
            configured_value = configured_dict[attribute]
            retrieved_value = retrieved_dict.get(attribute)
            if configured_value != retrieved_value:
                ret_val = False
                str_tuple = (
                    attribute,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                self.differing_attributes.append(attribute)
                log('Attribute "%s" differs. Configured parameter: (%s) %s. Retrieved NITRO parameter: (%s) %s' % str_tuple)

        return ret_val

    def _binding_list_item_delete(self, binding):
        log('ModuleExecutor._binding_list_item_delete()')

        log('Deleting binding %s' % binding)

        # First attribute is the primary id attribute
        id_key = self.key_attributes_present[0]
        id = binding[id_key]

        args = {}
        for key in self.key_attributes_present[1:]:
            if key in binding:
                args[key] = binding[key]

        result = self.fetcher.delete(resource=self.endpoint, id=id, args=args)
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def _binding_list_item_create(self, binding):
        log('ModuleExecutor._binding_list_item_create()')

        put_data = {
            self.endpoint: binding
        }

        log('request put data: %s' % put_data)

        result = self.fetcher.put(put_data=put_data, resource=self.endpoint)

        log('result of put: %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def bindings_list_create(self):
        log('ModuleExecutor.bindings_list_create()')
        self.bindings_list_update()

    def bindings_list_update(self):
        log('ModuleExecutor.bindings_list_update()')

        for key in self.to_delete_keys:
            self._binding_list_item_delete(self.existing_bindings_dict[key])

        for key in self.to_update_keys:
            self._binding_list_item_delete(self.existing_bindings_dict[key])

        for key in self.to_update_keys:
            self._binding_list_item_create(self.configured_bindings_dict[key])

        for key in self.to_create_keys:
            self._binding_list_item_create(self.configured_bindings_dict[key])

    def bindings_list_delete(self):
        log('ModuleExecutor.bindings_list_delete()')

        for key in self.configured_bindings_dict:
            binding = self.configured_bindings_dict[key]
            self._binding_list_item_delete(binding)

    def object_exists(self):
        log('ModuleExecutor.object_exists()')

        resource_missing_errorcode = self.module.params['workflow'].get('resource_missing_errorcode')
        log('resource missing errorcode %a' % resource_missing_errorcode)

        if resource_missing_errorcode is None:
            msg = 'object lifecycle requires resource_missing_errorcode workflow parameter'
            self.module.fail_json(msg=msg, **self.module_result)

        result = self.fetcher.get(self.endpoint, self.id)

        log('get result %s' % result)
        if result['nitro_errorcode'] == 0:
            self.retrieved_object = result['data'][self.endpoint][0]
            return True
        elif result['nitro_errorcode'] == resource_missing_errorcode:
            return False
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def object_identical(self):
        log('ModuleExecutor.object_identical()')
        ret_val = True

        if self.retrieved_object is None:
            raise Exception('Should have a retrieved object by now.')

        for attribute in self.module.params['resource'].keys():
            configured_value = self.module.params['resource'][attribute]
            retrieved_value = self.retrieved_object.get(attribute)
            if configured_value != retrieved_value:
                ret_val = False
                str_tuple = (
                    attribute,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                self.differing_attributes.append(attribute)
                log('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)

        return ret_val

    def object_create(self):
        log('ModuleExecutor.object_create()')
        attributes = self.module.params['resource']
        post_data = {
            self.endpoint: attributes
        }

        log('post data %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource=self.endpoint)
        log('post result %s' % result)

        if result['http_response_data']['status'] == 201:
            if result.get('nitro_errorcode') is not None:
                if result['nitro_errorcode'] != 0:
                    raise NitroException(
                        errorcode=result['nitro_errorcode'],
                        message=result.get('nitro_message'),
                        severity=result.get('nitro_severity'),
                    )
        elif 400 <= result['http_response_data']['status'] <= 599:
            raise NitroException(
                errorcode=result.get('nitro_errorcode'),
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        else:
            msg = 'Did not get nitro errorcode and http status was not 201 or 4xx (%s)' % result['http_response_data']['status']
            self.module.fail_json(msg=msg, **self.module_result)

    def object_update(self):
        log('ModuleExecutor.object_update()')

        non_updateables_changed = list(
            frozenset(self.non_updateable_attributes) & frozenset(self.differing_attributes)
        )
        if len(non_updateables_changed) > 0:
            log('Non updateables changed %s' % non_updateables_changed)
            if self.module.params['workflow']['allow_recreate']:
                self.object_delete()
                self.object_create()
            else:
                msg = ('Not allowed to recreate object. Non updateable attributes changed %s' % non_updateables_changed)
                self.module.fail_json(msg=msg, **self.module_result)
        else:
            attributes = self.module.params['resource']
            for attribute in self.non_updateable_attributes:
                if attribute in attributes:
                    del attributes[attribute]

            put_data = {
                self.endpoint: attributes
            }

            log('request put data: %s' % put_data)

            result = self.fetcher.put(put_data=put_data, resource=self.endpoint)

            log('result of put: %s' % result)

            if result['nitro_errorcode'] != 0:
                raise NitroException(
                    errorcode=result['nitro_errorcode'],
                    message=result.get('nitro_message'),
                    severity=result.get('nitro_severity'),
                )

    def object_delete(self):
        log('ModuleExecutor.object_delete()')

        args = {}
        for key in self.module.params['workflow'].get('delete_id_attributes', []):
            if key in self.configured_object:
                args[key] = self.configured_object[key]

        result = self.fetcher.delete(resource=self.endpoint, id=self.id, args=args)
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def non_updateable_object_exists(self):
        log('ModuleExecutor.non_updateable_object_exists()')

        resource_missing_errorcode = self.module.params['workflow'].get('resource_missing_errorcode')
        log('resource missing errorcode %a' % resource_missing_errorcode)

        if resource_missing_errorcode is None:
            msg = 'object lifecycle requires resource_missing_errorcode workflow parameter'
            self.module.fail_json(msg=msg, **self.module_result)

        args = {}
        for key in self.module.params['workflow'].get('delete_id_attributes', []):
            if key in self.configured_object:
                args[key] = self.configured_object[key]

        log('self.id %s' % self.id)
        result = self.fetcher.get(self.endpoint, id=self.id, args=args)
        log('get result %s' % result)

        if result['nitro_errorcode'] == 0:
            returned_list = result['data'][self.endpoint]
            if len(returned_list) > 1:
                msg = 'Found more than one existing objects'
                self.module.fail_json(msg=msg, **self.module_result)

            # Fallthrough
            self.retrieved_object = result['data'][self.endpoint][0]
            return True
        elif result['nitro_errorcode'] == resource_missing_errorcode:
            return False
        else:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def non_updateable_object_identical(self):
        log('ModuleExecutor.non_updateable_object_identical()')

        ret_val = True

        if self.retrieved_object is None:
            raise Exception('Should have a retrieved object by now.')

        for attribute in self.module.params['resource'].keys():
            configured_value = self.module.params['resource'][attribute]
            retrieved_value = self.retrieved_object.get(attribute)
            if configured_value != retrieved_value:
                ret_val = False
                str_tuple = (
                    attribute,
                    type(configured_value),
                    configured_value,
                    type(retrieved_value),
                    retrieved_value,
                )
                self.differing_attributes.append(attribute)
                log('Attribute "%s" differs. Playbook parameter: (%s) %s. Retrieved NITRO object: (%s) %s' % str_tuple)

        return ret_val

    def non_updateable_object_create(self):
        log('ModuleExecutor.non_updateable_object_create()')

        attributes = self.module.params['resource']
        post_data = {
            self.endpoint: attributes
        }

        log('post data %s' % post_data)
        result = self.fetcher.post(post_data=post_data, resource=self.endpoint)
        log('post result %s' % result)

        if result['http_response_data']['status'] == 201:
            if result.get('nitro_errorcode') is not None:
                if result['nitro_errorcode'] != 0:
                    raise NitroException(
                        errorcode=result['nitro_errorcode'],
                        message=result.get('nitro_message'),
                        severity=result.get('nitro_severity'),
                    )
        elif 400 <= result['http_response_data']['status'] <= 599:
            raise NitroException(
                errorcode=result.get('nitro_errorcode'),
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )
        else:
            msg = 'Did not get nitro errorcode and http status was not 201 or 4xx (%s)' % result['http_response_data']['status']
            self.module.fail_json(msg=msg, **self.module_result)

    def non_updateable_object_update(self):
        log('ModuleExecutor.non_updateable_object_update()')
        self.non_updateable_object_delete()
        self.non_updateable_object_create()

    def non_updateable_object_delete(self):
        log('ModuleExecutor.non_updateable_object_delete()')

        args = {}
        for key in self.module.params['workflow']['delete_id_attributes']:
            if key in self.configured_object:
                args[key] = self.configured_object[key]

        result = self.fetcher.delete(resource=self.endpoint, id=self.id, args=args)
        log('delete result %s' % result)

        if result['nitro_errorcode'] != 0:
            raise NitroException(
                errorcode=result['nitro_errorcode'],
                message=result.get('nitro_message'),
                severity=result.get('nitro_severity'),
            )

    def update_or_create_resource(self):
        log('ModuleExecutor.update_or_create_resource()')

        # Create or update main object
        if not self.resource_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.resource_create()
        else:
            if not self.resource_identical():
                self.module_result['changed'] = True
                if not self.module.check_mode:
                    self.resource_update()
            else:
                log('Existing resource has identical values to configured.')

    def delete_resource(self):
        log('ModuleExecutor.delete_resource()')

        if self.resource_exists():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                self.resource_delete()

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update_or_create_resource()
            elif self.module.params['state'] == 'absent':
                self.delete_resource()

            self.module.exit_json(**self.module_result)

        except NitroException as e:
            msg = "nitro exception errorcode=%s, message=%s, severity=%s" % (str(e.errorcode), e.message, e.severity)
            self.module.fail_json(msg=msg, **self.module_result)
        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

    argument_spec.update(netscaler_common_arguments)

    module_specific_arguments = dict(
        state=dict(
            type='str',
            choices=['present', 'absent'],
            default='present',
        ),
        workflow=dict(type='dict'),
        resource=dict(type='dict'),
        nitro_protocol=dict(
            type='str',
            default='https',
            choices=['http', 'https']
        )
    )

    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()
