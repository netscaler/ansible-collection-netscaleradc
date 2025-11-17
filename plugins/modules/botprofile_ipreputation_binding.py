#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: botprofile_ipreputation_binding
short_description: Binding Resource definition for describing association between
  botprofile and ipreputation resources
description: Binding Resource definition for describing association between botprofile
  and ipreputation resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  remove_non_updatable_params:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - When given yes, the module will remove any parameters that are not updatable
        in the resource.
      - If no, the module will return error if any non-updatable parameters are provided.
    type: str
  bot_bind_comment:
    type: str
    description:
      - Any comments about this binding.
  bot_iprep_action:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
      - MITIGATION
    description:
      - One or more actions to be taken if bot is detected based on this IP Reputation
        binding. Only C(LOG) action can be combinded with C(DROP), C(RESET), C(REDIRECT)
        or C(MITIGATION) action.
    elements: str
  bot_iprep_enabled:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enabled or disabled IP-repuation binding.
  bot_ipreputation:
    type: bool
    description:
      - IP reputation binding. For each category, only one binding is allowed. To
        update the values of an existing binding, user has to first unbind that binding,
        and then needs to bind again with the new values.
  category:
    type: str
    choices:
      - IP
      - BOTNETS
      - SPAM_SOURCES
      - SCANNERS
      - DOS
      - REPUTATION
      - PHISHING
      - PROXY
      - NETWORK
      - MOBILE_THREATS
      - WINDOWS_EXPLOITS
      - WEB_ATTACKS
      - TOR_PROXY
      - CLOUD
      - CLOUD_AWS
      - CLOUD_GCP
      - CLOUD_AZURE
      - CLOUD_ORACLE
      - CLOUD_IBM
      - CLOUD_SALESFORCE
    description:
      - 'C(IP) Repuation category. Following C(IP) Reuputation categories are allowed:'
      - '*IP_BASED - This category checks whether client C(IP) is malicious or not.'
      - '*BOTNET - This category includes Botnet C&C channels, and infected zombie
        machines controlled by Bot master.'
      - '*C(SPAM_SOURCES) - This category includes tunneling spam messages through
        a proxy, anomalous SMTP activities, and forum spam activities.'
      - '*C(SCANNERS) - This category includes all reconnaissance such as probes,
        host scan, domain scan, and password brute force attack.'
      - '*C(DOS) - This category includes C(DOS), DDOS, anomalous sync flood, and
        anomalous traffic detection.'
      - '*C(REPUTATION) - This category denies access from C(IP) addresses currently
        known to be infected with malware. This category also includes IPs with average
        low Webroot Reputation Index score. Enabling this category will prevent access
        from sources identified to contact malware distribution points.'
      - '*C(PHISHING) - This category includes C(IP) addresses hosting phishing sites
        and other kinds of fraud activities such as ad click fraud or gaming fraud.'
      - '*C(PROXY) - This category includes C(IP) addresses providing proxy services.'
      - '*C(NETWORK) - IPs providing proxy and anonymization services including The
        Onion Router aka TOR or darknet.'
      - '*C(MOBILE_THREATS) - This category checks client C(IP) with the list of IPs
        harmful for mobile devices.'
      - '*C(WINDOWS_EXPLOITS) - This category includes active C(IP) address offering
        or distributig malware, shell code, rootkits, worms or viruses.'
      - '*C(WEB_ATTACKS) - This category includes cross site scripting, iFrame injection,
        SQL injection, cross domain injection or domain password brute force attack.'
      - '*C(TOR_PROXY) - This category includes C(IP) address acting as exit nodes
        for the Tor Network.'
      - '*C(CLOUD) - This category checks client C(IP) with list of public cloud IPs.'
      - '*C(CLOUD_AWS) - This category checks client C(IP) with list of public cloud
        IPs from Amazon Web Services.'
      - '*C(CLOUD_GCP) - This category checks client C(IP) with list of public cloud
        IPs from Google Cloud Platform.'
      - '*C(CLOUD_AZURE) - This category checks client C(IP) with list of public cloud
        IPs from Azure.'
      - '*C(CLOUD_ORACLE) - This category checks client C(IP) with list of public
        cloud IPs from Oracle.'
      - '*C(CLOUD_IBM) - This category checks client C(IP) with list of public cloud
        IPs from IBM.'
      - '*C(CLOUD_SALESFORCE) - This category checks client C(IP) with list of public
        cloud IPs from Salesforce.'
  logmessage:
    type: str
    description:
      - Message to be logged for this binding.
  name:
    type: str
    description:
      - Name for the profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        (_) characters. Cannot be changed after the profile is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample botprofile_ipreputation_binding playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure botprofile_ipreputation_binding
      delegate_to: localhost
      netscaler.adc.botprofile_ipreputation_binding:
        state: present
        name: Bot_management_prof
        bot_ipreputation: true
        category: IP
        bot_iprep_enabled: 'ON'
        bot_iprep_action:
          - LOG
          - DROP
        logmessage: IP Reputation
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
