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
module: sslcertkeybundle
short_description: Configuration for certkey bundle resource.
description: Configuration for certkey bundle resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bundlefile:
    description:
      - Name of and, optionally, path to the X509 certificate bundle file that is
        used to form the certificate-key bundle. The certificate bundle file should
        be present on the appliance's hard-disk drive or solid-state drive. /nsconfig/ssl/
        is the default path. The certificate bundle file consists of list of certificates
        and one key in PEM format.
    type: str
  certkeybundlename:
    description:
      - 'Name given to the cerKeyBundle. The name will be used to bind/unbind certkey
        bundle to vip. Must begin with an ASCII alphanumeric or underscore (_) character,
        and must contain only ASCII alphanumeric, underscore, hash (#), period (.),
        space, colon (:), at (@), equals (=), and hyphen (-) characters. The following
        requirement applies only to the Citrix ADC CLI: If the name includes one or
        more spaces, enclose the name in double or single quotation marks (for example,
        "my file" or ''my file'').'
    type: str
  passplain:
    description:
      - Pass phrase used to encrypt the private-key. Required when certificate bundle
        file contains encrypted private-key in PEM format.
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
