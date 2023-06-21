#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: authenticationvserver
short_description: Configuration for authentication virtual server resource.
description: Configuration for authentication virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  appflowlog:
    description:
      - Log AppFlow flow information.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  authentication:
    description:
      - Require users to be authenticated before sending traffic through this virtual
        server.
    type: str
    default: true
    choices:
      - true
      - false
  authenticationdomain:
    description:
      - The domain of the authentication cookie set by Authentication vserver
    type: str
  certkeynames:
    description:
      - Name of the certificate key that was bound to the corresponding SSL virtual
        server as the Certificate Authority for the device certificate
    type: str
  comment:
    description:
      - Any comments associated with this virtual server.
    type: str
  failedlogintimeout:
    description:
      - Number of minutes an account will be locked if user exceeds maximum permissible
        attempts
    type: int
  ipv46:
    description:
      - IP address of the authentication virtual server, if a single IP address is
        assigned to the virtual server.
    type: str
  maxloginattempts:
    description:
      - Maximum Number of login Attempts
    type: int
  name:
    description:
      - 'Name for the new authentication virtual server. '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed
        after the authentication virtual server is added by using the rename authentication
        vserver command.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication policy" or 'my authentication
        policy').
    type: str
  newname:
    description:
      - 'New name of the authentication virtual server. '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, 'my authentication policy' or "my authentication
        policy").
    type: str
  port:
    description:
      - TCP port on which the virtual server accepts connections.
    type: int
  range:
    description:
      - 'If you are creating a series of virtual servers with a range of IP addresses
        assigned to them, the length of the range. '
      - The new range of authentication virtual servers will have IP addresses consecutively
        numbered, starting with the primary address specified with the IP Address
        parameter.
    type: int
    default: 1
  samesite:
    description:
      - SameSite attribute value for Cookies generated in AAATM context. This attribute
        value will be appended only for the cookies which are specified in the builtin
        patset ns_cookies_samesite
    type: str
    choices:
      - None
      - LAX
      - STRICT
  servicetype:
    description:
      - Protocol type of the authentication virtual server. Always SSL.
    type: str
    default: SSL
    choices:
      - SSL
  state:
    description:
      - Initial state of the new virtual server.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
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
