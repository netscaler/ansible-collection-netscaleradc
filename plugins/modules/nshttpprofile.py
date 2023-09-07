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
module: nshttpprofile
short_description: Configuration for HTTP profile resource.
description: Configuration for HTTP profile resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  adpttimeout:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Adapts the configured request timeout based on flow conditions. The timeout
        is increased or decreased internally and applied on the flow.
    type: str
    default: DISABLED
  allowonlywordcharactersandhyphen:
    choices:
      - ENABLED
      - DISABLED
    description:
      - When enabled allows only the word characters [A-Za-z0-9_] and hyphen [-] in
        the request/response header names and the connection will be reset for the
        other characters. When disabled allows any visible (printing) characters (%21-%7E)
        except delimiters (double quotes and "(),/:;<=>?@[]{}").
    type: str
    default: DISABLED
  altsvc:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for Alternative Services.
    type: str
    default: DISABLED
  altsvcvalue:
    description:
      - Configure a custom Alternative Services header value that should be inserted
        in the response to advertise a HTTP/SSL/HTTP_QUIC vserver.
    type: str
  apdexcltresptimethreshold:
    description:
      - This option sets the satisfactory threshold (T) for client response time in
        milliseconds to be used for APDEX calculations. This means a transaction responding
        in less than this threshold is considered satisfactory. Transaction responding
        between T and 4*T is considered tolerable. Any transaction responding in more
        than 4*T time is considered frustrating. Citrix ADC maintains stats for such
        tolerable and frustrating transcations. And client response time related apdex
        counters are only updated on a vserver which receives clients traffic.
    type: float
    default: 500
  clientiphdrexpr:
    description:
      - Name of the header that contains the real client IP address.
    type: str
  cmponpush:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Start data compression on receiving a TCP packet with PUSH flag set.
    type: str
    default: DISABLED
  conmultiplex:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Reuse server connections for requests from more than one client connections.
    type: str
    default: ENABLED
  dropextracrlf:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Drop any extra 'CR' and 'LF' characters present after the header.
    type: str
    default: ENABLED
  dropextradata:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Drop any extra data when server sends more data than the specified content-length.
    type: str
    default: DISABLED
  dropinvalreqs:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Drop invalid HTTP requests or responses.
    type: str
    default: DISABLED
  grpcholdlimit:
    description:
      - Maximum size in bytes allowed to buffer gRPC packets till trailer is received
    type: float
    default: 131072
  grpcholdtimeout:
    description:
      - Maximum time in milliseconds allowed to buffer gRPC packets till trailer is
        received. The value should be in multiples of 100
    type: float
    default: 1000
  grpclengthdelimitation:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Set to C(DISABLED) for gRPC without a length delimitation.
    type: str
    default: ENABLED
  http2:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for HTTP/2.
    type: str
    default: DISABLED
  http2altsvcframe:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for sending HTTP/2 ALTSVC frames. When enabled,
        the ADC sends HTTP/2 ALTSVC frames to HTTP/2 clients, instead of the Alt-Svc
        response header field. Not applicable to servers.
    type: str
    default: DISABLED
  http2direct:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for Direct HTTP/2.
    type: str
    default: DISABLED
  http2headertablesize:
    description:
      - Maximum size of the header compression table used to decode header blocks,
        in bytes.
    type: float
    default: 4096
  http2initialconnwindowsize:
    description:
      - Initial window size for connection level flow control, in bytes.
    type: float
    default: 65535
  http2initialwindowsize:
    description:
      - Initial window size for stream level flow control, in bytes.
    type: float
    default: 65535
  http2maxconcurrentstreams:
    description:
      - Maximum number of concurrent streams that is allowed per connection.
    type: float
    default: 100
  http2maxemptyframespermin:
    description:
      - Maximum number of empty  frames allowed in HTTP2 connection per minute
    type: float
    default: 60
  http2maxframesize:
    description:
      - Maximum size of the frame payload that the Citrix ADC is willing to receive,
        in bytes.
    type: float
    default: 16384
  http2maxheaderlistsize:
    description:
      - 'Maximum size of header list that the Citrix ADC is prepared to accept, in
        bytes. NOTE: The actual plain text header size that the Citrix ADC accepts
        is limited by maxHeaderLen. Please change maxHeaderLen parameter as well when
        modifying http2MaxHeaderListSize.'
    type: float
    default: 24576
  http2maxpingframespermin:
    description:
      - Maximum number of ping frames allowed in HTTP2 connection per minute
    type: float
    default: 60
  http2maxresetframespermin:
    description:
      - Maximum number of reset frames allowed in HTTP/2 connection per minute
    type: float
    default: 90
  http2maxsettingsframespermin:
    description:
      - Maximum number of settings frames allowed in HTTP2 connection per minute
    type: float
    default: 15
  http2minseverconn:
    description:
      - Minimum number of HTTP2 connections established to backend server, on receiving
        HTTP requests from client before multiplexing the streams into the available
        HTTP/2 connections.
    type: float
    default: 20
  http2strictcipher:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable strict HTTP/2 cipher selection
    type: str
    default: ENABLED
  http3:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for HTTP/3.
    type: str
    default: DISABLED
  http3maxheaderblockedstreams:
    description:
      - Maximum number of HTTP/3 streams that can be blocked while HTTP/3 headers
        are being decoded.
    type: float
    default: 100
  http3maxheaderfieldsectionsize:
    description:
      - Maximum size of the HTTP/3 header field section, in bytes.
    type: float
    default: 24576
  http3maxheadertablesize:
    description:
      - Maximum size of the HTTP/3 QPACK dynamic header table, in bytes.
    type: float
    default: 4096
  httppipelinebuffsize:
    description:
      - Application pipeline request buffering size, in bytes.
    type: float
    default: 131072
  incomphdrdelay:
    description:
      - Maximum time to wait, in milliseconds, between incomplete header packets.
        If the header packets take longer to arrive at Citrix ADC, the connection
        is silently dropped.
    type: float
    default: 7000
  markconnreqinval:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark CONNECT requests as invalid.
    type: str
    default: DISABLED
  markhttp09inval:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark HTTP/0.9 requests as invalid.
    type: str
    default: DISABLED
  markhttpheaderextrawserror:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark Http header with extra white space as invalid
    type: str
    default: DISABLED
  markrfc7230noncompliantinval:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark RFC7230 non-compliant transaction as invalid
    type: str
    default: DISABLED
  marktracereqinval:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark TRACE requests as invalid.
    type: str
    default: DISABLED
  maxheaderfieldlen:
    description:
      - Number of bytes allowed for header field for HTTP header. If number of bytes
        exceeds beyond configured value, then request will be marked invalid
    type: float
    default: 24820
  maxheaderlen:
    description:
      - Number of bytes to be queued to look for complete header before returning
        error. If complete header is not obtained after queuing these many bytes,
        request will be marked as invalid and no L7 processing will be done for that
        TCP connection.
    type: float
    default: 24820
  maxreq:
    description:
      - Maximum number of requests allowed on a single connection. Zero implies no
        limit on the number of requests.
    type: float
  maxreusepool:
    description:
      - Maximum limit on the number of connections, from the Citrix ADC to a particular
        server that are kept in the reuse pool. This setting is helpful for optimal
        memory utilization and for reducing the idle connections to the server just
        after the peak time. Zero implies no limit on reuse pool size. If non-zero
        value is given, it has to be greater than or equal to the number of running
        Packet Engines.
    type: float
  minreusepool:
    description:
      - Minimum limit on the number of connections, from the Citrix ADC to a particular
        server that are kept in the reuse pool. This setting is helpful for optimal
        memory utilization and for reducing the idle connections to the server just
        after the peak time. Zero implies no limit on reuse pool size.
    type: float
  name:
    description:
      - Name for an HTTP profile. Must begin with a letter, number, or the underscore
        \(_\) character. Other characters allowed, after the first character, are
        the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon
        \(:\), and equal \(=\) characters. The name of a HTTP profile cannot be changed
        after it is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks \(for example, "my http profile" or ''my http profile''\).'
    type: str
  passprotocolupgrade:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Pass protocol upgrade request to the server.
    type: str
    default: ENABLED
  persistentetag:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Generate the persistent Citrix ADC specific ETag for the HTTP response with
        ETag header.
    type: str
    default: DISABLED
  reqtimeout:
    description:
      - Time, in seconds, within which the HTTP request must complete. If the request
        does not complete within this time, the specified request timeout action is
        executed. Zero disables the timeout.
    type: float
  reqtimeoutaction:
    description:
      - 'Action to take when the HTTP request does not complete within the specified
        request timeout duration. You can configure the following actions:'
      - '* RESET - Send RST (reset) to client when timeout occurs.'
      - '* DROP - Drop silently when timeout occurs.'
      - '* Custom responder action - Name of the responder action to trigger when
        timeout occurs, used to send custom message.'
    type: str
  reusepooltimeout:
    description:
      - Idle timeout (in seconds) for server connections in re-use pool. Connections
        in the re-use pool are flushed, if they remain idle for the configured timeout.
    type: float
  rtsptunnel:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow RTSP tunnel in HTTP. Once application/x-rtsp-tunnelled is seen in Accept
        or Content-Type header, Citrix ADC does not process Layer 7 traffic on this
        connection.
    type: str
    default: DISABLED
  weblog:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable web logging.
    type: str
    default: ENABLED
  websocket:
    choices:
      - ENABLED
      - DISABLED
    description:
      - HTTP connection to be upgraded to a web socket connection. Once upgraded,
        Citrix ADC does not process Layer 7 traffic on this connection.
    type: str
    default: DISABLED
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
- name: Sample Playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Sample Task | nshttpProfile
      delegate_to: localhost
      netscaler.adc.nshttpprofile:
        state: present
        name: httpprofile-HTTP2-0
        http2: ENABLED

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
