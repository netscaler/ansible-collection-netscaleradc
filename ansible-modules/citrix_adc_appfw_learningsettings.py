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
module: citrix_adc_appfw_learningsettings
short_description: Configuration for learning settings resource.
description: Configuration for learning settings resource.

version_added: "2.9"

author:
    - George Nikolopoulos (@giorgos-nikolopoulos)
    - Sumanth Lingappa (@sumanth-lingappa)

options:

    profilename:
        description:
            - "Name of the profile."
            - "Minimum length =  1"
        type: str

    starturlminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn start
            - "Minimum value = C(1)"
        type: str

    starturlpercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular start URL pattern
                the learning engine to learn that start URL.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    cookieconsistencyminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn
            - "Minimum value = C(1)"
        type: str

    cookieconsistencypercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular cookie pattern for
                learning engine to learn that cookie.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    csrftagminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn
                request forgery (CSRF) tags.
            - "Minimum value = C(1)"
        type: str

    csrftagpercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular CSRF tag for the
                engine to learn that CSRF tag.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    fieldconsistencyminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn field
                information.
            - "Minimum value = C(1)"
        type: str

    fieldconsistencypercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular field consistency
                for the learning engine to learn that field consistency pattern.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    crosssitescriptingminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn HTML
                scripting patterns.
            - "Minimum value = C(1)"
        type: str

    crosssitescriptingpercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular cross-site
                pattern for the learning engine to learn that cross-site scripting pattern.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    sqlinjectionminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn HTML
                injection patterns.
            - "Minimum value = C(1)"
        type: str

    sqlinjectionpercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular HTML SQL injection
                for the learning engine to learn that HTML SQL injection pattern.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    fieldformatminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn field
            - "Minimum value = C(1)"
        type: str

    fieldformatpercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular web form field
                for the learning engine to recommend a field format for that form field.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    creditcardnumberminthreshold:
        description:
            - "Minimum threshold to learn Credit Card information."
            - "Minimum value = C(1)"
        type: str

    creditcardnumberpercentthreshold:
        description:
            - "Minimum threshold in percent to learn Credit Card information."
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    contenttypeminthreshold:
        description:
            - "Minimum threshold to learn Content Type information."
            - "Minimum value = C(1)"
        type: str

    contenttypepercentthreshold:
        description:
            - "Minimum threshold in percent to learn Content Type information."
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    xmlwsiminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn web
                interoperability (WSI) information.
            - "Minimum value = C(1)"
        type: str

    xmlwsipercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular pattern for the
                engine to learn a web services interoperability (WSI) pattern.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    xmlattachmentminthreshold:
        description:
            - >-
                Minimum number of application firewall sessions that the learning engine must observe to learn XML
                patterns.
            - "Minimum value = C(1)"
        type: str

    xmlattachmentpercentthreshold:
        description:
            - >-
                Minimum percentage of application firewall sessions that must contain a particular XML attachment
                for the learning engine to learn that XML attachment pattern.
            - "Minimum value = C(0)"
            - "Maximum value = C(100)"
        type: str

    fieldformatautodeploygraceperiod:
        description:
            - "The number of minutes after the threshold hit alert the learned rule will be deployed."
            - "Minimum value = C(5)"
            - "Maximum value = C(43200)"
        type: str

    sqlinjectionautodeploygraceperiod:
        description:
            - "The number of minutes after the threshold hit alert the learned rule will be deployed."
            - "Minimum value = C(5)"
            - "Maximum value = C(43200)"
        type: str

    crosssitescriptingautodeploygraceperiod:
        description:
            - "The number of minutes after the threshold hit alert the learned rule will be deployed."
            - "Minimum value = C(5)"
            - "Maximum value = C(43200)"
        type: str



extends_documentation_fragment: netscaler
'''

EXAMPLES = '''
- hosts: citrix_adc

  gather_facts: False
  tasks:
    - name: Setup learning settings
      delegate_to: localhost
      citrix_adc_appfw_learningsettings:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 192.168.1.2
        state: present

        profilename: test_profile
        starturlminthreshold: 100
        starturlpercentthreshold: 100
        cookieconsistencyminthreshold: 100
        cookieconsistencypercentthreshold: 100
        csrftagminthreshold: 100
        csrftagpercentthreshold: 100
        fieldconsistencyminthreshold: 100
        fieldconsistencypercentthreshold: 100
        crosssitescriptingminthreshold: 100
        crosssitescriptingpercentthreshold: 100
        sqlinjectionminthreshold: 100
        sqlinjectionpercentthreshold: 100
        fieldformatminthreshold: 100
        fieldformatpercentthreshold: 100
        creditcardnumberminthreshold: 100
        creditcardnumberpercentthreshold: 100
        contenttypeminthreshold: 100
        contenttypepercentthreshold: 100
        xmlwsiminthreshold: 100
        xmlwsipercentthreshold: 100
        xmlattachmentminthreshold: 100
        xmlattachmentpercentthreshold: 100
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
from ansible.module_utils.network.netscaler.netscaler import NitroResourceConfig, NitroException, netscaler_common_arguments, log, loglines


class ModuleExecutor(object):

    def __init__(self, module):
        self.module = module
        self.main_nitro_class = 'appfwlearningsettings'

        # Dictionary containing attribute information
        # for each NITRO object utilized by this module
        self.attribute_config = {
            'appfwlearningsettings': {
                'attributes_list': [
                    'profilename',
                    'starturlminthreshold',
                    'starturlpercentthreshold',
                    'cookieconsistencyminthreshold',
                    'cookieconsistencypercentthreshold',
                    'csrftagminthreshold',
                    'csrftagpercentthreshold',
                    'fieldconsistencyminthreshold',
                    'fieldconsistencypercentthreshold',
                    'crosssitescriptingminthreshold',
                    'crosssitescriptingpercentthreshold',
                    'sqlinjectionminthreshold',
                    'sqlinjectionpercentthreshold',
                    'fieldformatminthreshold',
                    'fieldformatpercentthreshold',
                    'creditcardnumberminthreshold',
                    'creditcardnumberpercentthreshold',
                    'contenttypeminthreshold',
                    'contenttypepercentthreshold',
                    'xmlwsiminthreshold',
                    'xmlwsipercentthreshold',
                    'xmlattachmentminthreshold',
                    'xmlattachmentpercentthreshold',
                    'fieldformatautodeploygraceperiod',
                    'sqlinjectionautodeploygraceperiod',
                    'crosssitescriptingautodeploygraceperiod',
                ],
                'transforms': {
                },
                'get_id_attributes': [
                    'profilename',
                ],
                'delete_id_attributes': [
                ],
            },

        }

        self.module_result = dict(
            changed=False,
            failed=False,
            loglines=loglines,
        )

    def update(self):
        log('ModuleExecutor.update()')
        # Check if main object exists
        config = NitroResourceConfig(
            module=self.module,
            resource=self.main_nitro_class,
            attribute_values_dict=self.module.params,
            attributes_list=self.attribute_config[self.main_nitro_class]['attributes_list'],
            transforms=self.attribute_config[self.main_nitro_class]['transforms'],
        )

        config.get_actual(self.attribute_config[self.main_nitro_class]['get_id_attributes'])
        if not config.values_subgroup_of_actual():
            self.module_result['changed'] = True
            if not self.module.check_mode:
                config.update()

    def main(self):
        try:

            if self.module.params['state'] == 'present':
                self.update()
            elif self.module.params['state'] == 'absent':
                log('Nothing to do for state absent')

            self.module.exit_json(**self.module_result)

        except NitroException as e:
            msg = "Nitro exception: errorcode=%s, message=%s, severity=%s" % (str(e.errorcode), e.message, e.severity)
            self.module.fail_json(msg=msg, **self.module_result)
        except Exception as e:
            msg = 'Exception %s: %s' % (type(e), str(e))
            self.module.fail_json(msg=msg, **self.module_result)


def main():

    argument_spec = dict()

    module_specific_arguments = dict(
        profilename=dict(type='str'),
        starturlminthreshold=dict(type='str'),
        starturlpercentthreshold=dict(type='str'),
        cookieconsistencyminthreshold=dict(type='str'),
        cookieconsistencypercentthreshold=dict(type='str'),
        csrftagminthreshold=dict(type='str'),
        csrftagpercentthreshold=dict(type='str'),
        fieldconsistencyminthreshold=dict(type='str'),
        fieldconsistencypercentthreshold=dict(type='str'),
        crosssitescriptingminthreshold=dict(type='str'),
        crosssitescriptingpercentthreshold=dict(type='str'),
        sqlinjectionminthreshold=dict(type='str'),
        sqlinjectionpercentthreshold=dict(type='str'),
        fieldformatminthreshold=dict(type='str'),
        fieldformatpercentthreshold=dict(type='str'),
        creditcardnumberminthreshold=dict(type='str'),
        creditcardnumberpercentthreshold=dict(type='str'),
        contenttypeminthreshold=dict(type='str'),
        contenttypepercentthreshold=dict(type='str'),
        xmlwsiminthreshold=dict(type='str'),
        xmlwsipercentthreshold=dict(type='str'),
        xmlattachmentminthreshold=dict(type='str'),
        xmlattachmentpercentthreshold=dict(type='str'),
        fieldformatautodeploygraceperiod=dict(type='str'),
        sqlinjectionautodeploygraceperiod=dict(type='str'),
        crosssitescriptingautodeploygraceperiod=dict(type='str'),

    )

    argument_spec.update(netscaler_common_arguments)
    argument_spec.update(module_specific_arguments)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    executor = ModuleExecutor(module=module)
    executor.main()


if __name__ == '__main__':
    main()
