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
module: analyticsprofile
short_description: Configuration for Analytics profile resource.
description: Configuration for Analytics profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  allhttpheaders:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log all the request and response
        headers.
    type: str
    default: DISABLED
  auditlogs:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option indicates the whether auditlog should be sent to the REST collector.
    type: str
    default: DISABLED
  collectors:
    description:
      - The collector can be an IP, an appflow collector name, a service or a vserver.
        If IP is specified, the transport is considered as logstream and default port
        of 5557 is taken. If collector name is specified, the collector properties
        are taken from the configured collector. If service is specified, the configured
        service is assumed as the collector. If vserver is specified, the services
        bound to it are considered as collectors and the records are load balanced.
    type: str
  cqareporting:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log TCP CQA parameters.
    type: str
    default: DISABLED
  events:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option indicates the whether events should be sent to the REST collector.
    type: str
    default: DISABLED
  grpcstatus:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the gRPC status headers
    type: str
    default: DISABLED
  httpauthentication:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log Authentication header.
    type: str
    default: DISABLED
  httpclientsidemeasurements:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will insert a javascript into the
        HTTP response to collect the client side page-timings and will send the same
        to the configured collectors.
    type: str
    default: DISABLED
  httpcontenttype:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log content-length header.
    type: str
    default: DISABLED
  httpcookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log cookie header.
    type: str
    default: DISABLED
  httpdomainname:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log domain name.
    type: str
    default: DISABLED
  httphost:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the Host header in appflow
        records
    type: str
    default: DISABLED
  httplocation:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log location header.
    type: str
    default: DISABLED
  httpmethod:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the method header in appflow
        records
    type: str
    default: DISABLED
  httppagetracking:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will link the embedded objects of
        a page together.
    type: str
    default: DISABLED
  httpreferer:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the referer header in appflow
        records
    type: str
    default: DISABLED
  httpsetcookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log set-cookie header.
    type: str
    default: DISABLED
  httpsetcookie2:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log set-cookie2 header.
    type: str
    default: DISABLED
  httpurl:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the URL in appflow records
    type: str
    default: DISABLED
  httpurlquery:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log URL Query.
    type: str
    default: DISABLED
  httpuseragent:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log User-Agent header.
    type: str
    default: DISABLED
  httpvia:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will Via header.
    type: str
    default: DISABLED
  httpxforwardedforheader:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log X-Forwarded-For header.
    type: str
    default: DISABLED
  integratedcache:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the Integrated Caching appflow
        records
    type: str
    default: DISABLED
  metrics:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option indicates the whether metrics should be sent to the REST collector.
    type: str
    default: DISABLED
  name:
    description:
      - Name for the analytics profile. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at
      - (@), equals (=), and hyphen (-) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my appflow profile" or 'my appflow profile').
    type: str
  outputmode:
    choices:
      - avro
      - prometheus
      - influx
    description:
      - This option indicates the format of REST API POST body. It depends on the
        consumer of the analytics data.
    type: str
    default: avro
  schemafile:
    description:
      - This option is for configuring json schema file containing a list of counters
        to be exported by metricscollector
    type: str
  servemode:
    choices:
      - Push
      - Pull
    description:
      - This option is for setting the mode of how data is provided
    type: str
    default: Push
  tcpburstreporting:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log TCP burst parameters.
    type: str
    default: ENABLED
  type:
    choices:
      - global
      - webinsight
      - tcpinsight
      - securityinsight
      - videoinsight
      - hdxinsight
      - gatewayinsight
      - timeseries
      - lsninsight
      - botinsight
      - CIinsight
    description:
      - This option indicates what information needs to be collected and exported.
    type: str
  urlcategory:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the URL category record.
    type: str
    default: DISABLED
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
