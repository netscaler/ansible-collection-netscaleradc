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
module: rdpclientprofile
short_description: Configuration for RDP clientprofile resource.
description: Configuration for RDP clientprofile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  addusernameinrdpfile:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Add username in rdp file.
  audiocapturemode:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting corresponds to the selections in the Remote audio area on the
        Local Resources tab under Options in RDC.
  keyboardhook:
    type: str
    choices:
      - OnLocal
      - OnRemote
      - InFullScreenMode
    description:
      - This setting corresponds to the selection in the Keyboard drop-down list on
        the Local Resources tab under Options in RDC.
  multimonitorsupport:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - Enable/Disable Multiple Monitor Support for Remote Desktop Connection (RDC).
  name:
    type: str
    description:
      - The name of the rdp profile
  psk:
    type: str
    description:
      - Pre shared key value
  randomizerdpfilename:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Will generate unique filename everytime rdp file is downloaded by appending
        output of time() function in the format <rdpfileName>_<time>.rdp. This tries
        to avoid the pop-up for replacement of existing rdp file during each rdp connection
        launch, hence providing better end-user experience.
  rdpcookievalidity:
    type: float
    description:
      - RDP cookie validity period. RDP cookie validity time is applicable for new
        connection and also for any re-connection that might happen, mostly due to
        network disruption or during fail-over.
  rdpcustomparams:
    type: str
    description:
      - Option for RDP custom parameters settings (if any). Custom params needs to
        be separated by '&'
  rdpfilename:
    type: str
    description:
      - RDP file name to be sent to End User
  rdphost:
    type: str
    description:
      - Fully-qualified domain name (FQDN) of the RDP Listener.
  rdplinkattribute:
    type: str
    description:
      - 'Citrix Gateway allows the configuration of rdpLinkAttribute parameter which
        can be used to fetch a list of RDP servers(IP/FQDN) that a user can access,
        from an Authentication server attribute(Example: LDAP, SAML). Based on the
        list received, the RDP links will be generated and displayed to the user.'
      - '            Note: The Attribute mentioned in the rdpLinkAttribute should
        be fetched through corresponding authentication method.'
  rdplistener:
    type: str
    description:
      - IP address (or) Fully-qualified domain name(FQDN) of the RDP Listener with
        the port in the format IP:Port (or) FQDN:Port
  rdpurloverride:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting determines whether the RDP parameters supplied in the vpn url
        override those specified in the RDP profile.
  rdpvalidateclientip:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting determines whether RDC launch is initiated by the valid client
        IP
  redirectclipboard:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting corresponds to the Clipboard check box on the Local Resources
        tab under Options in RDC.
  redirectcomports:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting corresponds to the selections for comports under More on the
        Local Resources tab under Options in RDC.
  redirectdrives:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting corresponds to the selections for Drives under More on the Local
        Resources tab under Options in RDC.
  redirectpnpdevices:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting corresponds to the selections for pnpdevices under More on the
        Local Resources tab under Options in RDC.
  redirectprinters:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting corresponds to the selection in the Printers check box on the
        Local Resources tab under Options in RDC.
  videoplaybackmode:
    type: str
    choices:
      - ENABLE
      - DISABLE
    description:
      - This setting determines if Remote Desktop Connection (RDC) will use RDP efficient
        multimedia streaming for video playback.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample rdpclientprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure rdpclientprofile
      delegate_to: localhost
      netscaler.adc.rdpclientprofile:

        state: present
        name: rdpc2
        rdpurloverride: DISABLE
        audiocapturemode: ENABLE
        rdpfilename: mstsc.rdp
        rdpcustomparams: span monitors:i:1
        psk: test!@3
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
