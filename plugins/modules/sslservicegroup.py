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
module: sslservicegroup
short_description: Configuration for SSL service group resource.
description: Configuration for SSL service group resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
    type: str
  commonname:
    type: str
    description:
      - Name to be checked against the CommonName (CN) field in the server certificate
        bound to the SSL server
  ocspstapling:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - 'State of OCSP stapling support on the SSL virtual server. Supported only
        if the protocol used is higher than SSLv3. Possible values:'
      - 'C(ENABLED): The appliance sends a request to the OCSP responder to check
        the status of the server certificate and caches the response for the specified
        time. If the response is valid at the time of SSL handshake with the client,
        the OCSP-based server certificate status is sent to the client during the
        handshake.'
      - 'C(DISABLED): The appliance does not check the status of the server certificate.'
    default: DISABLED
  sendclosenotify:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable sending SSL Close-Notify at the end of a transaction
    default: 'YES'
  serverauth:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of server authentication support for the SSL service group.
    default: DISABLED
  servicegroupname:
    type: str
    description:
      - Name of the SSL service group for which to set advanced configuration.
  sessreuse:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of session reuse. Establishing the initial handshake requires CPU-intensive
        public key encryption operations. With the C(ENABLED) setting, session key
        exchange is avoided for session resumption requests received from the client.
    default: ENABLED
  sesstimeout:
    type: float
    description:
      - Time, in seconds, for which to keep the session active. Any session resumption
        request received after the timeout period will require a fresh SSL handshake
        and establishment of a new SSL session.
    default: 300
  snienable:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of the Server Name Indication (SNI) feature on the service. SNI helps
        to enable SSL encryption on multiple domains on a single virtual server or
        service if the domains are controlled by the same organization and share the
        same second-level domain name. For example, *.sports.net can be used to secure
        domains such as login.sports.net and help.sports.net.
    default: DISABLED
  ssl3:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of SSLv3 protocol support for the SSL service group.
      - 'Note: On platforms with SSL acceleration chips, if the SSL chip does not
        support SSLv3, this parameter cannot be set to C(ENABLED).'
    default: ENABLED
  sslprofile:
    type: str
    description:
      - Name of the SSL profile that contains SSL settings for the Service Group.
  strictsigdigestcheck:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Parameter indicating to check whether peer's certificate is signed with one
        of signature-hash combination supported by Citrix ADC
    default: DISABLED
  tls1:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.0 protocol support for the SSL service group.
    default: ENABLED
  tls11:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.1 protocol support for the SSL service group.
    default: ENABLED
  tls12:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.2 protocol support for the SSL service group.
    default: ENABLED
  tls13:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of TLSv1.3 protocol support for the SSL service group.
    default: DISABLED
  sslservicegroup_ecccurve_binding:
    type: dict
    description: Bindings for sslservicegroup_ecccurve_binding resource
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
  sslservicegroup_sslcertkey_binding:
    type: dict
    description: Bindings for sslservicegroup_sslcertkey_binding resource
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
  sslservicegroup_sslcipher_binding:
    type: dict
    description: Bindings for sslservicegroup_sslcipher_binding resource
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
  sslservicegroup_sslciphersuite_binding:
    type: dict
    description: Bindings for sslservicegroup_sslciphersuite_binding resource
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
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
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
