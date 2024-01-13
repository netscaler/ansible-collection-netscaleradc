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
module: clusterfiles
short_description: Configuration for files resource.
description: Configuration for files resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices: []
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
    type: str
  mode:
    type: list
    choices:
      - all
      - bookmarks
      - ssl
      - imports
      - misc
      - dns
      - krb
      - AAA
      - app_catalog
      - all_plus_misc
      - all_minus_misc
    description:
      - 'The directories and files to be synchronized. The available settings function
        as follows:'
      - ' Mode    Paths'
      - ' C(all)           /nsconfig/C(ssl)/'
      - '                /var/netscaler/C(ssl)/'
      - '                /var/vpn/bookmark/'
      - '                /nsconfig/C(dns)/'
      - '                /nsconfig/monitors/'
      - '                /nsconfig/nstemplates/'
      - '                /nsconfig/ssh/'
      - '                /nsconfig/rc.netscaler'
      - '                /nsconfig/resolv.conf'
      - '                /nsconfig/inetd.conf'
      - '                /nsconfig/syslog.conf'
      - '                /nsconfig/ntp.conf'
      - '                /nsconfig/httpd.conf'
      - '                /nsconfig/sshd_config'
      - '                /nsconfig/hosts'
      - '                /nsconfig/enckey'
      - '                /var/nslw.bin/etc/krb5.conf'
      - '                /var/nslw.bin/etc/krb5.keytab'
      - '                /var/lib/likewise/db/'
      - '                /var/download/'
      - '                /var/wi/tomcat/webapps/'
      - '                /var/wi/tomcat/conf/Catalina/localhost/'
      - '                /var/wi/java_home/lib/security/cacerts'
      - '                /var/wi/java_home/jre/lib/security/cacerts'
      - '                /var/netscaler/locdb/'
      - C(ssl)            /nsconfig/C(ssl)/
      - '                 /var/netscaler/C(ssl)/'
      - C(bookmarks)     /var/vpn/bookmark/
      - C(dns)                  /nsconfig/C(dns)/
      - C(imports)          /var/download/
      - C(misc)               /nsconfig/license/
      - '                       /nsconfig/rc.conf'
      - C(all_plus_misc)    Includes *C(all)* files and /nsconfig/license/ and /nsconfig/rc.conf.
      - 'Default value: C(all)'
    elements: str
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
