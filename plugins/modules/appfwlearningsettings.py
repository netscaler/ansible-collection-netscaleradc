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
module: appfwlearningsettings
short_description: Configuration for learning settings resource.
description: Configuration for learning settings resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
      - When C(absent) the resource will be deleted from the NetScaler ADC node.
    type: str
  contenttypeautodeploygraceperiod:
    type: float
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  contenttypeminthreshold:
    type: float
    description:
      - Minimum threshold to learn Content Type information.
  contenttypepercentthreshold:
    type: float
    description:
      - Minimum threshold in percent to learn Content Type information.
  cookieconsistencyautodeploygraceperiod:
    type: float
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  cookieconsistencyminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn cookies.
  cookieconsistencypercentthreshold:
    type: float
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        cookie pattern for the learning engine to learn that cookie.
  creditcardnumberminthreshold:
    type: float
    description:
      - Minimum threshold to learn Credit Card information.
  creditcardnumberpercentthreshold:
    type: float
    description:
      - Minimum threshold in percent to learn Credit Card information.
  crosssitescriptingautodeploygraceperiod:
    type: float
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  crosssitescriptingminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn HTML cross-site scripting patterns.
  crosssitescriptingpercentthreshold:
    type: float
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        cross-site scripting pattern for the learning engine to learn that cross-site
        scripting pattern.
  csrftagautodeploygraceperiod:
    type: float
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  csrftagminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn cross-site request forgery (CSRF) tags.
  csrftagpercentthreshold:
    type: float
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        CSRF tag for the learning engine to learn that CSRF tag.
  fieldconsistencyautodeploygraceperiod:
    type: float
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  fieldconsistencyminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn field consistency information.
  fieldconsistencypercentthreshold:
    type: float
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        field consistency pattern for the learning engine to learn that field consistency
        pattern.
  fieldformatautodeploygraceperiod:
    type: float
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  fieldformatminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn field formats.
  fieldformatpercentthreshold:
    type: float
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        web form field pattern for the learning engine to recommend a field format
        for that form field.
  profilename:
    type: str
    description:
      - Name of the profile.
  sqlinjectionautodeploygraceperiod:
    type: float
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  sqlinjectionminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn HTML SQL injection patterns.
  sqlinjectionpercentthreshold:
    type: float
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        HTML SQL injection pattern for the learning engine to learn that HTML SQL
        injection pattern.
  starturlautodeploygraceperiod:
    type: float
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
  starturlminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn start URLs.
  starturlpercentthreshold:
    type: float
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        start URL pattern for the learning engine to learn that start URL.
  xmlattachmentminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn XML attachment patterns.
  xmlattachmentpercentthreshold:
    type: float
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        XML attachment pattern for the learning engine to learn that XML attachment
        pattern.
  xmlwsiminthreshold:
    type: float
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn web services interoperability (WSI) information.
  xmlwsipercentthreshold:
    type: float
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
