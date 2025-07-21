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
module: appfwlearningsettings
short_description: Configuration for learning settings resource.
description: Configuration for learning settings resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
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
  contenttypeautodeploygraceperiod:
    type: int
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  contenttypeminthreshold:
    type: int
    description:
      - Minimum threshold to learn Content Type information.
  contenttypepercentthreshold:
    type: int
    description:
      - Minimum threshold in percent to learn Content Type information.
  cookieconsistencyautodeploygraceperiod:
    type: int
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  cookieconsistencyminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn cookies.
  cookieconsistencypercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        cookie pattern for the learning engine to learn that cookie.
  creditcardnumberminthreshold:
    type: int
    description:
      - Minimum threshold to learn Credit Card information.
  creditcardnumberpercentthreshold:
    type: int
    description:
      - Minimum threshold in percent to learn Credit Card information.
  crosssitescriptingautodeploygraceperiod:
    type: int
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  crosssitescriptingminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn HTML cross-site scripting patterns.
  crosssitescriptingpercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        cross-site scripting pattern for the learning engine to learn that cross-site
        scripting pattern.
  csrftagautodeploygraceperiod:
    type: int
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  csrftagminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn cross-site request forgery (CSRF) tags.
  csrftagpercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        CSRF tag for the learning engine to learn that CSRF tag.
  fieldconsistencyautodeploygraceperiod:
    type: int
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  fieldconsistencyminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn field consistency information.
  fieldconsistencypercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        field consistency pattern for the learning engine to learn that field consistency
        pattern.
  fieldformatautodeploygraceperiod:
    type: int
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  fieldformatminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn field formats.
  fieldformatpercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        web form field pattern for the learning engine to recommend a field format
        for that form field.
  profilename:
    type: str
    description:
      - Name of the profile.
  sqlinjectionautodeploygraceperiod:
    type: int
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  sqlinjectionminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn HTML SQL injection patterns.
  sqlinjectionpercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        HTML SQL injection pattern for the learning engine to learn that HTML SQL
        injection pattern.
  starturlautodeploygraceperiod:
    type: int
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  starturlminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn start URLs.
  starturlpercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        start URL pattern for the learning engine to learn that start URL.
  xmlattachmentminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn XML attachment patterns.
  xmlattachmentpercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        XML attachment pattern for the learning engine to learn that XML attachment
        pattern.
  xmlwsiminthreshold:
    type: int
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn web services interoperability (WSI) information.
  xmlwsipercentthreshold:
    type: int
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        pattern for the learning engine to learn a web services interoperability (WSI)
        pattern.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
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
