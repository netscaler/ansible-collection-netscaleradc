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
module: authenticationtacacsaction
short_description: Configuration for TACACS action resource.
description: Configuration for TACACS action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  accounting:
    description:
      - Whether the TACACS+ server is currently accepting accounting messages.
    type: str
    choices:
      - true
      - false
  attribute1:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '1' (where '1' changes for each attribute)
    type: str
  attribute10:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '10' (where '10' changes for each attribute)
    type: str
  attribute11:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '11' (where '11' changes for each attribute)
    type: str
  attribute12:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '12' (where '12' changes for each attribute)
    type: str
  attribute13:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '13' (where '13' changes for each attribute)
    type: str
  attribute14:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '14' (where '14' changes for each attribute)
    type: str
  attribute15:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '15' (where '15' changes for each attribute)
    type: str
  attribute16:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '16' (where '16' changes for each attribute)
    type: str
  attribute2:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '2' (where '2' changes for each attribute)
    type: str
  attribute3:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '3' (where '3' changes for each attribute)
    type: str
  attribute4:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '4' (where '4' changes for each attribute)
    type: str
  attribute5:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '5' (where '5' changes for each attribute)
    type: str
  attribute6:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '6' (where '6' changes for each attribute)
    type: str
  attribute7:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '7' (where '7' changes for each attribute)
    type: str
  attribute8:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '8' (where '8' changes for each attribute)
    type: str
  attribute9:
    description:
      - Name of the custom attribute to be extracted from server and stored at index
        '9' (where '9' changes for each attribute)
    type: str
  attributes:
    description:
      - 'List of attribute names separated by '','' which needs to be fetched from
        tacacs server. '
      - 'Note that preceeding and trailing spaces will be removed. '
      - Attribute name can be 127 bytes and total length of this string should not
        cross 2047 bytes.
      - These attributes have multi-value support separated by ',' and stored as key-value
        pair in AAA session
    type: str
  auditfailedcmds:
    description:
      - The state of the TACACS+ server that will receive accounting messages.
    type: str
    choices:
      - true
      - false
  authorization:
    description:
      - Use streaming authorization on the TACACS+ server.
    type: str
    choices:
      - true
      - false
  authtimeout:
    description:
      - Number of seconds the Citrix ADC waits for a response from the TACACS+ server.
    type: int
    default: 3
  defaultauthenticationgroup:
    description:
      - This is the default group that is chosen when the authentication succeeds
        in addition to extracted groups.
    type: str
  groupattrname:
    description:
      - TACACS+ group attribute name.
      - Used for group extraction on the TACACS+ server.
    type: str
  name:
    description:
      - 'Name for the TACACS+ profile (action). '
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed
        after TACACS profile is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my authentication action" or 'y authentication
        action').
    type: str
  serverip:
    description:
      - IP address assigned to the TACACS+ server.
    type: str
  serverport:
    description:
      - Port number on which the TACACS+ server listens for connections.
    type: int
    default: 49
  tacacssecret:
    description:
      - 'Key shared between the TACACS+ server and the Citrix ADC. '
      - Required for allowing the Citrix ADC to communicate with the TACACS+ server.
    type: str
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
