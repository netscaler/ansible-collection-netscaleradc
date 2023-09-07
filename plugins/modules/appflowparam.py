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
module: appflowparam
short_description: Configuration for AppFlow parameter resource.
description: Configuration for AppFlow parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  aaausername:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow AAA Username logging.
    type: str
    default: DISABLED
  analyticsauthtoken:
    description:
      - Authentication token to be set by the agent.
    type: str
  appnamerefresh:
    description:
      - Interval, in seconds, at which to send Appnames to the configured collectors.
        Appname refers to the name of an entity (virtual server, service, or service
        group) in the Citrix ADC.
    type: float
    default: 600
  auditlogs:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable Auditlogs to be sent to the Telemetry Agent
    type: str
    default: DISABLED
  cacheinsight:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flag to determine whether cache records need to be exported or not. If this
        flag is true and IC is enabled, cache records are exported instead of L7 HTTP
        records
    type: str
    default: DISABLED
  clienttrafficonly:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Generate AppFlow records for only the traffic from the client.
    type: str
    default: 'NO'
  connectionchaining:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable connection chaining so that the client server flows of a connection
        are linked. Also the connection chain ID is propagated across Citrix ADCs,
        so that in a multi-hop environment the flows belonging to the same logical
        connection are linked. This id is also logged as part of appflow record
    type: str
    default: DISABLED
  cqareporting:
    choices:
      - ENABLED
      - DISABLED
    description:
      - TCP CQA reporting enable/disable knob.
    type: str
    default: DISABLED
  distributedtracing:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable generation of the distributed tracing templates in the Appflow records
    type: str
    default: DISABLED
  disttracingsamplingrate:
    description:
      - Sampling rate for Distributed Tracing
    type: float
  emailaddress:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow user email-id logging.
    type: str
    default: DISABLED
  events:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable Events to be sent to the Telemetry Agent
    type: str
    default: DISABLED
  flowrecordinterval:
    description:
      - Interval, in seconds, at which to send flow records to the configured collectors.
    type: float
    default: 60
  gxsessionreporting:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable this option for Gx session reporting
    type: str
    default: DISABLED
  httpauthorization:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HTTP Authorization header information.
    type: str
    default: DISABLED
  httpcontenttype:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HTTP Content-Type header sent from the server to the client to
        determine the type of the content sent.
    type: str
    default: DISABLED
  httpcookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the cookie that was in the HTTP request the appliance received from
        the client.
    type: str
    default: DISABLED
  httpdomain:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the http domain request to be exported.
    type: str
    default: DISABLED
  httphost:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the host identified in the HTTP request that the appliance received
        from the client.
    type: str
    default: DISABLED
  httplocation:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HTTP location headers returned from the HTTP responses.
    type: str
    default: DISABLED
  httpmethod:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the method that was specified in the HTTP request that the appliance
        received from the client.
    type: str
    default: DISABLED
  httpquerywithurl:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HTTP query segment along with the URL that the Citrix ADC received
        from the client.
    type: str
    default: DISABLED
  httpreferer:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the web page that was last visited by the client.
    type: str
    default: DISABLED
  httpsetcookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the Set-cookie header sent from the server to the client in response
        to a HTTP request.
    type: str
    default: DISABLED
  httpsetcookie2:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the Set-cookie header sent from the server to the client in response
        to a HTTP request.
    type: str
    default: DISABLED
  httpurl:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the http URL that the Citrix ADC received from the client.
    type: str
    default: DISABLED
  httpuseragent:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the client application through which the HTTP request was received
        by the Citrix ADC.
    type: str
    default: DISABLED
  httpvia:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the httpVia header which contains the IP address of proxy server through
        which the client accessed the server.
    type: str
    default: DISABLED
  httpxforwardedfor:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the httpXForwardedFor header, which contains the original IP Address
        of the client using a proxy server to access the server.
    type: str
    default: DISABLED
  identifiername:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the stream identifier name to be exported.
    type: str
    default: DISABLED
  identifiersessionname:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the stream identifier session name to be exported.
    type: str
    default: DISABLED
  logstreamovernsip:
    choices:
      - ENABLED
      - DISABLED
    description:
      - To use the Citrix ADC IP to send Logstream records instead of the SNIP
    type: str
    default: DISABLED
  lsnlogging:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the Large Scale Nat(LSN)
        records to the configured collectors.
    type: str
    default: DISABLED
  metrics:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable Citrix ADC Stats to be sent to the Telemetry Agent
    type: str
    default: DISABLED
  observationdomainid:
    description:
      - 'An observation domain groups a set of Citrix ADCs based on deployment: cluster,
        HA etc. A unique Observation Domain ID is required to be assigned to each
        such group.'
    type: float
  observationdomainname:
    description:
      - Name of the Observation Domain defined by the observation domain ID.
    type: str
  observationpointid:
    description:
      - An observation point ID is identifier for the NetScaler from which appflow
        records are being exported. By default, the NetScaler IP is the observation
        point ID.
    type: float
  securityinsightrecordinterval:
    description:
      - Interval, in seconds, at which to send security insight flow records to the
        configured collectors.
    type: float
    default: 600
  securityinsighttraffic:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/disable the feature individually on appflow action.
    type: str
    default: DISABLED
  skipcacheredirectionhttptransaction:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Skip Cache http transaction. This HTTP transaction is specific to Cache Redirection
        module. In Case of Cache Miss there will be another HTTP transaction initiated
        by the cache server.
    type: str
    default: DISABLED
  subscriberawareness:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable this option for logging end user MSISDN in L4/L7 appflow records
    type: str
    default: DISABLED
  subscriberidobfuscation:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable this option for obfuscating MSISDN in L4/L7 appflow records
    type: str
    default: DISABLED
  subscriberidobfuscationalgo:
    choices:
      - MD5
      - SHA256
    description:
      - Algorithm(C(MD5) or C(SHA256)) to be used for obfuscating MSISDN
    type: str
    default: MD5
  tcpattackcounterinterval:
    description:
      - Interval, in seconds, at which to send tcp attack counters to the configured
        collectors. If 0 is configured, the record is not sent.
    type: float
  templaterefresh:
    description:
      - Refresh interval, in seconds, at which to export the template data. Because
        data transmission is in UDP, the templates must be resent at regular intervals.
    type: float
    default: 600
  timeseriesovernsip:
    choices:
      - ENABLED
      - DISABLED
    description:
      - To use the Citrix ADC IP to send Time series data such as metrics and events,
        instead of the SNIP
    type: str
    default: DISABLED
  udppmtu:
    description:
      - MTU, in bytes, for IPFIX UDP packets.
    type: float
    default: 1472
  urlcategory:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the URL category record.
    type: str
    default: DISABLED
  usagerecordinterval:
    description:
      - On enabling this option, the NGS will send bandwidth usage record to configured
        collectors.
    type: float
  videoinsight:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/disable the feature individually on appflow action.
    type: str
    default: DISABLED
  websaasappusagereporting:
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, NGS will send data used by Web/saas app at the end
        of every HTTP transaction to configured collectors.
    type: str
    default: DISABLED
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | appflowparam
      delegate_to: localhost
      netscaler.adc.appflowparam:
        state: present
        observationpointid: '2370493962'

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
