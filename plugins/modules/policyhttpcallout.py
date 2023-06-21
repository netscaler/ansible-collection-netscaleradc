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
module: policyhttpcallout
short_description: Configuration for HTTP callout resource.
description: Configuration for HTTP callout resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bodyexpr:
    description:
      - An advanced string expression for generating the body of the request. The
        expression can contain a literal string or an expression that derives the
        value (for example, client.ip.src). Mutually exclusive with -fullReqExpr.
    type: str
  cacheforsecs:
    description:
      - Duration, in seconds, for which the callout response is cached. The cached
        responses are stored in an integrated caching content group named "calloutContentGroup".
        If no duration is configured, the callout responses will not be cached unless
        normal caching configuration is used to cache them. This parameter takes precedence
        over any normal caching configuration that would otherwise apply to these
        responses.
      - "\t   Note that the calloutContentGroup definition may not be modified or\
        \ removed nor may it be used with other cache policies."
    type: int
  comment:
    description:
      - Any comments to preserve information about this HTTP callout.
    type: str
  fullreqexpr:
    description:
      - Exact HTTP request, in the form of an expression, which the Citrix ADC sends
        to the callout agent. If you set this parameter, you must not include HTTP
        method, host expression, URL stem expression, headers, or parameters.
      - The request expression is constrained by the feature for which the callout
        is used. For example, an HTTP.RES expression cannot be used in a request-time
        policy bank or in a TCP content switching policy bank.
      - The Citrix ADC does not check the validity of this request. You must manually
        validate the request.
    type: str
  headers:
    description:
      - One or more headers to insert into the HTTP request. Each header is specified
        as "name(expr)", where expr is an expression that is evaluated at runtime
        to provide the value for the named header. You can configure a maximum of
        eight headers for an HTTP callout. Mutually exclusive with the full HTTP request
        expression.
    type: list
    elements: str
  hostexpr:
    description:
      - String expression to configure the Host header. Can contain a literal value
        (for example, 10.101.10.11) or a derived value (for example, http.req.header("Host")).
        The literal value can be an IP address or a fully qualified domain name. Mutually
        exclusive with the full HTTP request expression.
    type: str
  httpmethod:
    description:
      - Method used in the HTTP request that this callout sends.  Mutually exclusive
        with the full HTTP request expression.
    type: str
    choices:
      - GET
      - POST
  ipaddress:
    description:
      - IP Address of the server (callout agent) to which the callout is sent. Can
        be an IPv4 or IPv6 address.
      - Mutually exclusive with the Virtual Server parameter. Therefore, you cannot
        set the <IP Address, Port> and the Virtual Server in the same HTTP callout.
    type: str
  name:
    description:
      - Name for the HTTP callout. Not case sensitive. Must begin with an ASCII letter
        or underscore (_) character, and must consist only of ASCII alphanumeric or
        underscore characters. Must not begin with 're' or 'xp' or be a word reserved
        for use as an expression qualifier prefix (such as HTTP) or enumeration value
        (such as ASCII). Must not be the name of an existing named expression, pattern
        set, dataset, stringmap, or HTTP callout.
    type: str
  parameters:
    description:
      - One or more query parameters to insert into the HTTP request URL (for a GET
        request) or into the request body (for a POST request). Each parameter is
        specified as "name(expr)", where expr is an expression that is evaluated at
        run time to provide the value for the named parameter (name=value). The parameter
        values are URL encoded. Mutually exclusive with the full HTTP request expression.
    type: list
    elements: str
  port:
    description:
      - Server port to which the HTTP callout agent is mapped. Mutually exclusive
        with the Virtual Server parameter. Therefore, you cannot set the <IP Address,
        Port> and the Virtual Server in the same HTTP callout.
    type: int
  resultexpr:
    description:
      - 'Expression that extracts the callout results from the response sent by the
        HTTP callout agent. Must be a response based expression, that is, it must
        begin with HTTP.RES. The operations in this expression must match the return
        type. For example, if you configure a return type of TEXT, the result expression
        must be a text based expression. If the return type is NUM, the result expression
        (resultExpr) must return a numeric value, as in the following example: http.res.body(10000).length.'
    type: str
  returntype:
    description:
      - 'Type of data that the target callout agent returns in response to the callout. '
      - 'Available settings function as follows:'
      - '* TEXT - Treat the returned value as a text string. '
      - '* NUM - Treat the returned value as a number.'
      - '* BOOL - Treat the returned value as a Boolean value. '
      - 'Note: You cannot change the return type after it is set.'
    type: str
    choices:
      - BOOL
      - NUM
      - TEXT
  scheme:
    description:
      - Type of scheme for the callout server.
    type: str
    choices:
      - http
      - https
  urlstemexpr:
    description:
      - String expression for generating the URL stem. Can contain a literal string
        (for example, "/mysite/index.html") or an expression that derives the value
        (for example, http.req.url). Mutually exclusive with the full HTTP request
        expression.
    type: str
  vserver:
    description:
      - Name of the load balancing, content switching, or cache redirection virtual
        server (the callout agent) to which the HTTP callout is sent. The service
        type of the virtual server must be HTTP. Mutually exclusive with the IP address
        and port parameters. Therefore, you cannot set the <IP Address, Port> and
        the Virtual Server in the same HTTP callout.
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
