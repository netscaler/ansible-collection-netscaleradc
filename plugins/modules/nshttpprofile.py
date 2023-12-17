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
module: nshttpprofile
short_description: Configuration for HTTP profile resource.
description: Configuration for HTTP profile resource.
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
  adpttimeout:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Adapts the configured request timeout based on flow conditions. The timeout
        is increased or decreased internally and applied on the flow.
  allowonlywordcharactersandhyphen:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - When enabled allows only the word characters [A-Za-z0-9_] and hyphen [-] in
        the request/response header names and the connection will be reset for the
        other characters. When disabled allows any visible (printing) characters (%21-%7E)
        except delimiters (double quotes and "(),/:;<=>?@[]{}").
  altsvc:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for Alternative Services.
  altsvcvalue:
    type: str
    description:
      - Configure a custom Alternative Services header value that should be inserted
        in the response to advertise a HTTP/SSL/HTTP_QUIC vserver.
  apdexcltresptimethreshold:
    type: float
    description:
      - This option sets the satisfactory threshold (T) for client response time in
        milliseconds to be used for APDEX calculations. This means a transaction responding
        in less than this threshold is considered satisfactory. Transaction responding
        between T and 4*T is considered tolerable. Any transaction responding in more
        than 4*T time is considered frustrating. Citrix ADC maintains stats for such
        tolerable and frustrating transcations. And client response time related apdex
        counters are only updated on a vserver which receives clients traffic.
  clientiphdrexpr:
    type: str
    description:
      - Name of the header that contains the real client IP address.
  cmponpush:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Start data compression on receiving a TCP packet with PUSH flag set.
  conmultiplex:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Reuse server connections for requests from more than one client connections.
  dropextracrlf:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Drop any extra 'CR' and 'LF' characters present after the header.
  dropextradata:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Drop any extra data when server sends more data than the specified content-length.
  dropinvalreqs:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Drop invalid HTTP requests or responses.
  grpcholdlimit:
    type: float
    description:
      - Maximum size in bytes allowed to buffer gRPC packets till trailer is received
  grpcholdtimeout:
    type: float
    description:
      - Maximum time in milliseconds allowed to buffer gRPC packets till trailer is
        received. The value should be in multiples of 100
  grpclengthdelimitation:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Set to C(DISABLED) for gRPC without a length delimitation.
  http2:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for HTTP/2.
  http2altsvcframe:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for sending HTTP/2 ALTSVC frames. When enabled,
        the ADC sends HTTP/2 ALTSVC frames to HTTP/2 clients, instead of the Alt-Svc
        response header field. Not applicable to servers.
  http2direct:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for Direct HTTP/2.
  http2headertablesize:
    type: float
    description:
      - Maximum size of the header compression table used to decode header blocks,
        in bytes.
  http2initialconnwindowsize:
    type: float
    description:
      - Initial window size for connection level flow control, in bytes.
  http2initialwindowsize:
    type: float
    description:
      - Initial window size for stream level flow control, in bytes.
  http2maxconcurrentstreams:
    type: float
    description:
      - Maximum number of concurrent streams that is allowed per connection.
  http2maxemptyframespermin:
    type: float
    description:
      - Maximum number of empty  frames allowed in HTTP2 connection per minute
  http2maxframesize:
    type: float
    description:
      - Maximum size of the frame payload that the Citrix ADC is willing to receive,
        in bytes.
  http2maxheaderlistsize:
    type: float
    description:
      - 'Maximum size of header list that the Citrix ADC is prepared to accept, in
        bytes. NOTE: The actual plain text header size that the Citrix ADC accepts
        is limited by maxHeaderLen. Please change maxHeaderLen parameter as well when
        modifying http2MaxHeaderListSize.'
  http2maxpingframespermin:
    type: float
    description:
      - Maximum number of ping frames allowed in HTTP2 connection per minute
  http2maxresetframespermin:
    type: float
    description:
      - Maximum number of reset frames allowed in HTTP/2 connection per minute
  http2maxsettingsframespermin:
    type: float
    description:
      - Maximum number of settings frames allowed in HTTP2 connection per minute
  http2minseverconn:
    type: float
    description:
      - Minimum number of HTTP2 connections established to backend server, on receiving
        HTTP requests from client before multiplexing the streams into the available
        HTTP/2 connections.
  http2strictcipher:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable strict HTTP/2 cipher selection
  http3:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Choose whether to enable support for HTTP/3.
  http3maxheaderblockedstreams:
    type: float
    description:
      - Maximum number of HTTP/3 streams that can be blocked while HTTP/3 headers
        are being decoded.
  http3maxheaderfieldsectionsize:
    type: float
    description:
      - Maximum size of the HTTP/3 header field section, in bytes.
  http3maxheadertablesize:
    type: float
    description:
      - Maximum size of the HTTP/3 QPACK dynamic header table, in bytes.
  httppipelinebuffsize:
    type: float
    description:
      - Application pipeline request buffering size, in bytes.
  incomphdrdelay:
    type: float
    description:
      - Maximum time to wait, in milliseconds, between incomplete header packets.
        If the header packets take longer to arrive at Citrix ADC, the connection
        is silently dropped.
  markconnreqinval:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark CONNECT requests as invalid.
  markhttp09inval:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark HTTP/0.9 requests as invalid.
  markhttpheaderextrawserror:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark Http header with extra white space as invalid
  markrfc7230noncompliantinval:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark RFC7230 non-compliant transaction as invalid
  marktracereqinval:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Mark TRACE requests as invalid.
  maxheaderfieldlen:
    type: float
    description:
      - Number of bytes allowed for header field for HTTP header. If number of bytes
        exceeds beyond configured value, then request will be marked invalid
  maxheaderlen:
    type: float
    description:
      - Number of bytes to be queued to look for complete header before returning
        error. If complete header is not obtained after queuing these many bytes,
        request will be marked as invalid and no L7 processing will be done for that
        TCP connection.
  maxreq:
    type: float
    description:
      - Maximum number of requests allowed on a single connection. Zero implies no
        limit on the number of requests.
  maxreusepool:
    type: float
    description:
      - Maximum limit on the number of connections, from the Citrix ADC to a particular
        server that are kept in the reuse pool. This setting is helpful for optimal
        memory utilization and for reducing the idle connections to the server just
        after the peak time. Zero implies no limit on reuse pool size. If non-zero
        value is given, it has to be greater than or equal to the number of running
        Packet Engines.
  minreusepool:
    type: float
    description:
      - Minimum limit on the number of connections, from the Citrix ADC to a particular
        server that are kept in the reuse pool. This setting is helpful for optimal
        memory utilization and for reducing the idle connections to the server just
        after the peak time. Zero implies no limit on reuse pool size.
  name:
    type: str
    description:
      - Name for an HTTP profile. Must begin with a letter, number, or the underscore
        \(_\) character. Other characters allowed, after the first character, are
        the hyphen \(-\), period \(.\), hash \(\#\), space \( \), at \(@\), colon
        \(:\), and equal \(=\) characters. The name of a HTTP profile cannot be changed
        after it is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks \(for example, "my http profile" or ''my http profile''\).'
  passprotocolupgrade:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Pass protocol upgrade request to the server.
  persistentetag:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Generate the persistent Citrix ADC specific ETag for the HTTP response with
        ETag header.
  reqtimeout:
    type: float
    description:
      - Time, in seconds, within which the HTTP request must complete. If the request
        does not complete within this time, the specified request timeout action is
        executed. Zero disables the timeout.
  reqtimeoutaction:
    type: str
    description:
      - 'Action to take when the HTTP request does not complete within the specified
        request timeout duration. You can configure the following actions:'
      - '* RESET - Send RST (reset) to client when timeout occurs.'
      - '* DROP - Drop silently when timeout occurs.'
      - '* Custom responder action - Name of the responder action to trigger when
        timeout occurs, used to send custom message.'
  reusepooltimeout:
    type: float
    description:
      - Idle timeout (in seconds) for server connections in re-use pool. Connections
        in the re-use pool are flushed, if they remain idle for the configured timeout.
  rtsptunnel:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow RTSP tunnel in HTTP. Once application/x-rtsp-tunnelled is seen in Accept
        or Content-Type header, Citrix ADC does not process Layer 7 traffic on this
        connection.
  weblog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable web logging.
  websocket:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - HTTP connection to be upgraded to a web socket connection. Once upgraded,
        Citrix ADC does not process Layer 7 traffic on this connection.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
- name: Sample Playbook
  hosts: localhost
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
