#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
---
module: rewritepolicylabel
short_description: Configuration for rewrite policy label resource.
description: Configuration for rewrite policy label resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - renamed
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(renamed), the resource will be renamed on the NetScaler ADC node.
    type: str
  comment:
    type: str
    description:
      - Any comments to preserve information about this rewrite policy label.
  labelname:
    type: str
    description:
      - Name for the rewrite policy label. Must begin with a letter, number, or the
        underscore character (_), and must contain only letters, numbers, and the
        hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:),
        and underscore characters. Cannot be changed after the rewrite policy label
        is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my rewrite policy label" or 'my rewrite policy
        label').
  newname:
    type: str
    description:
      - 'New name for the rewrite policy label. '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my policy label" or 'my policy label').
  transform:
    type: str
    choices:
      - http_req
      - http_res
      - othertcp_req
      - othertcp_res
      - url
      - text
      - clientless_vpn_req
      - clientless_vpn_res
      - sipudp_req
      - sipudp_res
      - siptcp_req
      - siptcp_res
      - diameter_req
      - diameter_res
      - radius_req
      - radius_res
      - dns_req
      - dns_res
      - httpquic_req
      - httpquic_res
      - mqtt_req
      - mqtt_res
    description:
      - 'Types of transformations allowed by the policies bound to the label. For
        Rewrite, the following types are supported:'
      - '* C(http_req) - HTTP requests'
      - '* C(http_res) - HTTP responses'
      - '* C(othertcp_req) - Non-HTTP TCP requests'
      - '* C(othertcp_res) - Non-HTTP TCP responses'
      - '* C(url) - URLs'
      - '* C(text) - Text strings'
      - '* C(clientless_vpn_req) - Citrix ADC clientless VPN requests'
      - '* C(clientless_vpn_res) - Citrix ADC clientless VPN responses'
      - '* C(sipudp_req) - SIP requests'
      - '* C(sipudp_res) - SIP responses'
      - '* C(diameter_req) - DIAMETER requests'
      - '* C(diameter_res) - DIAMETER responses'
      - '* C(radius_req) - RADIUS requests'
      - '* C(radius_res) - RADIUS responses'
      - '* C(dns_req) - DNS requests'
      - '* C(dns_res) - DNS responses'
      - '* C(mqtt_req) - MQTT requests'
      - '* C(mqtt_res) - MQTT responses'
  rewritepolicylabel_rewritepolicy_binding:
    type: dict
    description: Bindings for rewritepolicylabel_rewritepolicy_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample rewritepolicylabel playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure rewritepolicylabel
      delegate_to: localhost
      netscaler.adc.rewritepolicylabel:
        state: present
        labelname: ia_rwrtpolabl6
        transform: http_req
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
diff:
  description: Dictionary of before and after changes
  returned: always
  type: dict
  sample: {'before': {'key1': 'xyz'}, 'after': {'key2': 'pqr'}, 'prepared': 'changes
      done'}
diff_list:
  description: List of differences between the actual configured object and the configuration
    specified in the module
  returned: when changed
  type: list
  sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class
      'str'>) PQR"]
failed:
  description: Indicates if the module failed or not
  returned: always
  type: bool
  sample: false
loglines:
  description: list of logged messages by the module
  returned: always
  type: list
  sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
