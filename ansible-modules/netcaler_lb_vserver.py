#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO review status and supported_by when migrating to github
ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'commiter',
                    'version': '1.0'}


# TODO: Add appropriate documentation
DOCUMENTATION = '''
---
module: netscaler_lb_vserver
short_description: Manage lbvserver configuration in Netscaler
description:
    - Manages configuration of lb vserver in Netscaler appliances

version_added: "tbd"
options:
    nsip:
        description:
            - The Nescaler ip address.

        required: True
'''

# TODO: Add appropriate examples
EXAMPLES = '''
- name: Connect to netscaler appliance
    netscaler_lb_vserver:
        nsip: "172.17.0.2"
'''

# TODO: Update as module progresses
RETURN = '''
config_updated:
    description: determine if a change in the netscaler configuration happened
    returned: always
    type: boolean
    sample: False
'''

from ansible.module_utils.basic import AnsibleModule

# TODO
# Actual implementation of the module goes here


# TODO add actual module instantiation code
def main():
    module = AnsibleModule(
        argument_spec=dict(
            nsip=dict(required=True),
        )
    )

    module.exit_json(config_updated=True)

if __name__ == "__main__":
    main()
