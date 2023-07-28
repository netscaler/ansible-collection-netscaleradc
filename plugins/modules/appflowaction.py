#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: appflowaction
short_description: Configuration for AppFlow action resource.
description: Configuration for AppFlow action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  botinsight:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the bot insight records
        to the configured collectors.
    type: str
    default: DISABLED
  ciinsight:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the ContentInspection Insight
        records to the configured collectors.
    type: str
    default: DISABLED
  clientsidemeasurements:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will collect the time required to
        load and render the mainpage on the client.
    type: str
    default: DISABLED
  collectors:
    description:
      - Name(s) of collector(s) to be associated with the AppFlow action.
    type: list
    elements: str
  comment:
    description:
      - Any comments about this action.  In the CLI, if including spaces between words,
        enclose the comment in quotation marks. (The quotation marks are not required
        in the configuration utility.)
    type: str
  distributionalgorithm:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will distribute records among the
        collectors. Else, all records will be sent to all the collectors.
    type: str
    default: DISABLED
  metricslog:
    description:
      - If only the stats records are to be exported, turn on this option.
    type: bool
  name:
    description:
      - Name for the action. Must begin with an ASCII alphabetic or underscore (_)
        character, and must contain only ASCII alphanumeric, underscore, hash (#),
        period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my appflow action" or 'my appflow action').
    type: str
  newname:
    description:
      - New name for the AppFlow action. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at
      - '(@), equals (=), and hyphen (-) characters. '
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my appflow action" or 'my appflow action').
    type: str
  pagetracking:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will start tracking the page for waterfall
        chart by inserting a NS_ESNS cookie in the response.
    type: str
    default: DISABLED
  securityinsight:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the security insight records
        to the configured collectors.
    type: str
    default: DISABLED
  transactionlog:
    choices:
      - ALL
      - ANOMALOUS
    description:
      - Log C(ANOMALOUS) or C(ALL) transactions
    type: str
    default: ALL
  videoanalytics:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the videoinsight records
        to the configured collectors.
    type: str
    default: DISABLED
  webinsight:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the webinsight records to
        the configured collectors.
    type: str
    default: ENABLED
  appflowaction_analyticsprofile_binding:
    type: dict
    description: Bindings for appflowaction_analyticsprofile_binding resource
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
