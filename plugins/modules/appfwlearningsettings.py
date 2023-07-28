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
module: appfwlearningsettings
short_description: Configuration for learning settings resource.
description: Configuration for learning settings resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  contenttypeautodeploygraceperiod:
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
    type: int
    default: 10080
  contenttypeminthreshold:
    description:
      - Minimum threshold to learn Content Type information.
    type: int
    default: 1
  contenttypepercentthreshold:
    description:
      - Minimum threshold in percent to learn Content Type information.
    type: int
  cookieconsistencyautodeploygraceperiod:
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
    type: int
    default: 10080
  cookieconsistencyminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn cookies.
    type: int
    default: 1
  cookieconsistencypercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        cookie pattern for the learning engine to learn that cookie.
    type: int
  creditcardnumberminthreshold:
    description:
      - Minimum threshold to learn Credit Card information.
    type: int
    default: 1
  creditcardnumberpercentthreshold:
    description:
      - Minimum threshold in percent to learn Credit Card information.
    type: int
  crosssitescriptingautodeploygraceperiod:
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
    type: int
    default: 10080
  crosssitescriptingminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn HTML cross-site scripting patterns.
    type: int
    default: 1
  crosssitescriptingpercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        cross-site scripting pattern for the learning engine to learn that cross-site
        scripting pattern.
    type: int
  csrftagautodeploygraceperiod:
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
    type: int
    default: 10080
  csrftagminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn cross-site request forgery (CSRF) tags.
    type: int
    default: 1
  csrftagpercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        CSRF tag for the learning engine to learn that CSRF tag.
    type: int
  fieldconsistencyautodeploygraceperiod:
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
    type: int
    default: 10080
  fieldconsistencyminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn field consistency information.
    type: int
    default: 1
  fieldconsistencypercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        field consistency pattern for the learning engine to learn that field consistency
        pattern.
    type: int
  fieldformatautodeploygraceperiod:
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
    type: int
    default: 10080
  fieldformatminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn field formats.
    type: int
    default: 1
  fieldformatpercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        web form field pattern for the learning engine to recommend a field format
        for that form field.
    type: int
  profilename:
    description:
      - Name of the profile.
    type: str
  sqlinjectionautodeploygraceperiod:
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
    type: int
    default: 10080
  sqlinjectionminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn HTML SQL injection patterns.
    type: int
    default: 1
  sqlinjectionpercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        HTML SQL injection pattern for the learning engine to learn that HTML SQL
        injection pattern.
    type: int
  starturlautodeploygraceperiod:
    description:
      - The number of minutes after the threshold hit alert the learned rule will
        be deployed
    type: int
    default: 10080
  starturlminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn start URLs.
    type: int
    default: 1
  starturlpercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        start URL pattern for the learning engine to learn that start URL.
    type: int
  xmlattachmentminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn XML attachment patterns.
    type: int
    default: 1
  xmlattachmentpercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        XML attachment pattern for the learning engine to learn that XML attachment
        pattern.
    type: int
  xmlwsiminthreshold:
    description:
      - Minimum number of application firewall sessions that the learning engine must
        observe to learn web services interoperability (WSI) information.
    type: int
    default: 1
  xmlwsipercentthreshold:
    description:
      - Minimum percentage of application firewall sessions that must contain a particular
        pattern for the learning engine to learn a web services interoperability (WSI)
        pattern.
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
