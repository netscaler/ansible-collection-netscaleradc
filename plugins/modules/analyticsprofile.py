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
---
module: analyticsprofile
short_description: Configuration for Analytics profile resource.
description: Configuration for Analytics profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  allhttpheaders:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log all the request and response
        headers.
  analyticsauthtoken:
    type: str
    description:
      - Token for authenticating with the endpoint. If the endpoint requires the Authorization
        header in a particular format, specify the complete format as the value to
        this parameter. For eg., in case of splunk, the Authorizaiton header is required
        to be of the form - Splunk <auth-token>.
  analyticsendpointcontenttype:
    type: str
    description:
      - By default, application/json content-type is used. If this needs to be overridden,
        specify the value.
  analyticsendpointmetadata:
    type: str
    description:
      - If the endpoint requires some metadata to be present before the actual json
        data, specify the same.
  analyticsendpointurl:
    type: str
    description:
      - The URL at which to upload the analytics data on the endpoint
  auditlogs:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option indicates the whether auditlog should be sent to the REST collector.
  collectors:
    type: str
    description:
      - The collector can be an IP, an appflow collector name, a service or a vserver.
        If IP is specified, the transport is considered as logstream and default port
        of 5557 is taken. If collector name is specified, the collector properties
        are taken from the configured collector. If service is specified, the configured
        service is assumed as the collector. If vserver is specified, the services
        bound to it are considered as collectors and the records are load balanced.
  cqareporting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log TCP CQA parameters.
  dataformatfile:
    type: str
    description:
      - This option is for configuring the file containing the data format and metadata
        required by the analytics endpoint.
  events:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option indicates the whether events should be sent to the REST collector.
  grpcstatus:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the gRPC status headers
  httpauthentication:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log Authentication header.
  httpclientsidemeasurements:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will insert a javascript into the
        HTTP response to collect the client side page-timings and will send the same
        to the configured collectors.
  httpcontenttype:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log content-length header.
  httpcookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log cookie header.
  httpdomainname:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log domain name.
  httphost:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the Host header in appflow
        records
  httplocation:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log location header.
  httpmethod:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the method header in appflow
        records
  httppagetracking:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will link the embedded objects of
        a page together.
  httpreferer:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the referer header in appflow
        records
  httpsetcookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log set-cookie header.
  httpsetcookie2:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log set-cookie2 header.
  httpurl:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the URL in appflow records
  httpurlquery:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log URL Query.
  httpuseragent:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log User-Agent header.
  httpvia:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will Via header.
  httpxforwardedforheader:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log X-Forwarded-For header.
  integratedcache:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log the Integrated Caching appflow
        records
  managementlog:
    type: list
    choices:
      - ALL
      - SHELL
      - ACCESS
      - NSMGMT
      - NONE
    description:
      - This option indicates the whether managementlog should be sent to the REST
        collector.
    elements: str
  metrics:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option indicates the whether metrics should be sent to the REST collector.
  metricsexportfrequency:
    type: float
    description:
      - This option is for configuring the metrics export frequency in seconds, frequency
        value must be in [30,300] seconds range
  name:
    type: str
    description:
      - Name for the analytics profile. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at
      - (@), equals (=), and hyphen (-) characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my appflow profile" or 'my appflow profile').
  outputmode:
    type: str
    choices:
      - avro
      - prometheus
      - influx
      - json
    description:
      - This option indicates the format of REST API POST body. It depends on the
        consumer of the analytics data.
  schemafile:
    type: str
    description:
      - This option is for configuring json schema file containing a list of counters
        to be exported by metricscollector
  servemode:
    type: str
    choices:
      - Push
      - Pull
    description:
      - This option is for setting the mode of how data is provided
  tcpburstreporting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will log TCP burst parameters.
  topn:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this topn support, the topn information of the stream identifier
        this profile is bound to will be exported to the analytics endpoint.
  type:
    type: str
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
      - udpinsight
      - ngsinsight
      - streaminsight
    description:
      - This option indicates what information needs to be collected and exported.
  urlcategory:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the URL category record.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample analyticsprofile playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure analyticsprofile
      delegate_to: localhost
      netscaler.adc.analyticsprofile:
        state: present
        name: telemetry_metrics_profile
        type: timeseries
        outputmode: prometheus
        metrics: ENABLED
        servemode: Pull
        schemafile: ./telemetry_collect_ns_metrics_schema.json
        metricsexportfrequency: '300'
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
