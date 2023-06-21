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
module: contentinspectionpolicy
short_description: Configuration for ContentInspection policy resource.
description: Configuration for ContentInspection policy resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  action:
    description:
      - Name of the contentInspection action to perform if the request matches this
        contentInspection policy.
      - '    There are also some built-in actions which can be used. These are:'
      - '    * NOINSPECTION - Send the request from the client to the server or response
        from the server to the client without sending it to Inspection device for
        Content Inspection.'
      - '    * RESET - Resets the client connection by closing it. The client program,
        such as a browser, will handle this and may inform the user. The client may
        then resend the request if desired.'
      - '    * DROP - Drop the request without sending a response to the user.'
    type: str
  comment:
    description:
      - Any type of information about this contentInspection policy.
    type: str
  logaction:
    description:
      - Name of the messagelog action to use for requests that match this policy.
    type: str
  name:
    description:
      - Name for the contentInspection policy.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) pound (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed
        after the contentInspection policy is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my contentInspection policy" or 'my contentInspection
        policy').
    type: str
  newname:
    description:
      - New name for the contentInspection policy. Must begin with a letter, number,
        or the underscore character (_), and must contain only letters, numbers, and
        the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon
        (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my contentInspection policy" or 'my contentInspection
        policy').
    type: str
  rule:
    description:
      - Expression that the policy uses to determine whether to execute the specified
        action.
    type: str
  undefaction:
    description:
      - Action to perform if the result of policy evaluation is undefined (UNDEF).
        An UNDEF event indicates an internal error condition. Only the above built-in
        actions can be used.
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
