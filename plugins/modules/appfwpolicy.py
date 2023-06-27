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
module: appfwpolicy
short_description: Configuration for application firewall policy resource.
description: Configuration for application firewall policy resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  comment:
    description:
      - Any comments to preserve information about the policy for later reference.
    type: str
  logaction:
    description:
      - Where to log information for connections that match this policy.
    type: str
  name:
    description:
      - 'Name for the policy. '
      - Must begin with a letter, number, or the underscore character \(_\), and must
        contain only letters, numbers, and the hyphen \(-\), period \(.\) pound \(\#\),
        space \( \), at (@), equals \(=\), colon \(:\), and underscore characters.
        Can be changed after the policy is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks \(for example, "my policy" or 'my policy'\).
    type: str
  newname:
    description:
      - New name for the policy. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my policy" or 'my policy').
    type: str
  profilename:
    description:
      - Name of the application firewall profile to use if the policy matches.
    type: str
  rule:
    description:
      - Name of the Citrix ADC named rule, or a Citrix ADC expression, that the policy
        uses to determine whether to filter the connection through the application
        firewall with the designated profile.
    type: str
  appfwpolicylabel_appfwpolicy_binding:
    type: dict
    description: Bindings for appfwpolicylabel_appfwpolicy_binding resource
    suboptions:
      mode:
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
