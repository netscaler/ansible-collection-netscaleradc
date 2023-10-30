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
module: appflowparam
short_description: Configuration for AppFlow parameter resource.
description: Configuration for AppFlow parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present) the resource will be created if needed and configured according
        to the module's parameters.
    type: str
  aaausername:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow AAA Username logging.
    default: DISABLED
  analyticsauthtoken:
    type: str
    description:
      - Authentication token to be set by the agent.
  appnamerefresh:
    type: float
    description:
      - Interval, in seconds, at which to send Appnames to the configured collectors.
        Appname refers to the name of an entity (virtual server, service, or service
        group) in the Citrix ADC.
    default: 600
  auditlogs:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable Auditlogs to be sent to the Telemetry Agent
    default: DISABLED
  cacheinsight:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flag to determine whether cache records need to be exported or not. If this
        flag is true and IC is enabled, cache records are exported instead of L7 HTTP
        records
    default: DISABLED
  clienttrafficonly:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Generate AppFlow records for only the traffic from the client.
    default: 'NO'
  connectionchaining:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable connection chaining so that the client server flows of a connection
        are linked. Also the connection chain ID is propagated across Citrix ADCs,
        so that in a multi-hop environment the flows belonging to the same logical
        connection are linked. This id is also logged as part of appflow record
    default: DISABLED
  cqareporting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - TCP CQA reporting enable/disable knob.
    default: DISABLED
  distributedtracing:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable generation of the distributed tracing templates in the Appflow records
    default: DISABLED
  disttracingsamplingrate:
    type: float
    description:
      - Sampling rate for Distributed Tracing
  emailaddress:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable AppFlow user email-id logging.
    default: DISABLED
  events:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable Events to be sent to the Telemetry Agent
    default: DISABLED
  flowrecordinterval:
    type: float
    description:
      - Interval, in seconds, at which to send flow records to the configured collectors.
    default: 60
  gxsessionreporting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable this option for Gx session reporting
    default: DISABLED
  httpauthorization:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HTTP Authorization header information.
    default: DISABLED
  httpcontenttype:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HTTP Content-Type header sent from the server to the client to
        determine the type of the content sent.
    default: DISABLED
  httpcookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the cookie that was in the HTTP request the appliance received from
        the client.
    default: DISABLED
  httpdomain:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the http domain request to be exported.
    default: DISABLED
  httphost:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the host identified in the HTTP request that the appliance received
        from the client.
    default: DISABLED
  httplocation:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HTTP location headers returned from the HTTP responses.
    default: DISABLED
  httpmethod:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the method that was specified in the HTTP request that the appliance
        received from the client.
    default: DISABLED
  httpquerywithurl:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HTTP query segment along with the URL that the Citrix ADC received
        from the client.
    default: DISABLED
  httpreferer:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the web page that was last visited by the client.
    default: DISABLED
  httpsetcookie:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the Set-cookie header sent from the server to the client in response
        to a HTTP request.
    default: DISABLED
  httpsetcookie2:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the Set-cookie header sent from the server to the client in response
        to a HTTP request.
    default: DISABLED
  httpurl:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the http URL that the Citrix ADC received from the client.
    default: DISABLED
  httpuseragent:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the client application through which the HTTP request was received
        by the Citrix ADC.
    default: DISABLED
  httpvia:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the httpVia header which contains the IP address of proxy server through
        which the client accessed the server.
    default: DISABLED
  httpxforwardedfor:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the httpXForwardedFor header, which contains the original IP Address
        of the client using a proxy server to access the server.
    default: DISABLED
  identifiername:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the stream identifier name to be exported.
    default: DISABLED
  identifiersessionname:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the stream identifier session name to be exported.
    default: DISABLED
  logstreamovernsip:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - To use the Citrix ADC IP to send Logstream records instead of the SNIP
    default: DISABLED
  lsnlogging:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, the Citrix ADC will send the Large Scale Nat(LSN)
        records to the configured collectors.
    default: DISABLED
  metrics:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable Citrix ADC Stats to be sent to the Telemetry Agent
    default: DISABLED
  observationdomainid:
    type: float
    description:
      - 'An observation domain groups a set of Citrix ADCs based on deployment: cluster,
        HA etc. A unique Observation Domain ID is required to be assigned to each
        such group.'
  observationdomainname:
    type: str
    description:
      - Name of the Observation Domain defined by the observation domain ID.
  observationpointid:
    type: float
    description:
      - An observation point ID is identifier for the NetScaler from which appflow
        records are being exported. By default, the NetScaler IP is the observation
        point ID.
  securityinsightrecordinterval:
    type: float
    description:
      - Interval, in seconds, at which to send security insight flow records to the
        configured collectors.
    default: 600
  securityinsighttraffic:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/disable the feature individually on appflow action.
    default: DISABLED
  skipcacheredirectionhttptransaction:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Skip Cache http transaction. This HTTP transaction is specific to Cache Redirection
        module. In Case of Cache Miss there will be another HTTP transaction initiated
        by the cache server.
    default: DISABLED
  subscriberawareness:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable this option for logging end user MSISDN in L4/L7 appflow records
    default: DISABLED
  subscriberidobfuscation:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable this option for obfuscating MSISDN in L4/L7 appflow records
    default: DISABLED
  subscriberidobfuscationalgo:
    type: str
    choices:
      - MD5
      - SHA256
    description:
      - Algorithm(C(MD5) or C(SHA256)) to be used for obfuscating MSISDN
    default: MD5
  tcpattackcounterinterval:
    type: float
    description:
      - Interval, in seconds, at which to send tcp attack counters to the configured
        collectors. If 0 is configured, the record is not sent.
  templaterefresh:
    type: float
    description:
      - Refresh interval, in seconds, at which to export the template data. Because
        data transmission is in UDP, the templates must be resent at regular intervals.
    default: 600
  timeseriesovernsip:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - To use the Citrix ADC IP to send Time series data such as metrics and events,
        instead of the SNIP
    default: DISABLED
  udppmtu:
    type: float
    description:
      - MTU, in bytes, for IPFIX UDP packets.
    default: 1472
  urlcategory:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the URL category record.
    default: DISABLED
  usagerecordinterval:
    type: float
    description:
      - On enabling this option, the NGS will send bandwidth usage record to configured
        collectors.
  videoinsight:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable/disable the feature individually on appflow action.
    default: DISABLED
  websaasappusagereporting:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - On enabling this option, NGS will send data used by Web/saas app at the end
        of every HTTP transaction to configured collectors.
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
