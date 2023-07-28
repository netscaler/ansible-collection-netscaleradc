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
module: responderaction
short_description: Configuration for responder action resource.
description: Configuration for responder action resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bypasssafetycheck:
    choices:
      - true
      - false
    description:
      - Bypass the safety check, allowing potentially unsafe expressions. An unsafe
        expression in a response is one that contains references to request elements
        that might not be present in all requests. If a response refers to a missing
        request element, an empty string is used instead.
    type: str
  comment:
    description:
      - Comment. Any type of information about this responder action.
    type: str
  headers:
    description:
      - One or more headers to insert into the HTTP response. Each header is specified
        as "name(expr)", where expr is an expression that is evaluated at runtime
        to provide the value for the named header. You can configure a maximum of
        eight headers for a responder action.
    type: list
    elements: str
  htmlpage:
    description:
      - For respondwithhtmlpage policies, name of the HTML page object to use as the
        response. You must first import the page object.
    type: str
  name:
    description:
      - Name for the responder action. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore
        characters. Can be changed after the responder policy is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my responder action" or 'my responder action').
    type: str
  newname:
    description:
      - New name for the responder action.
      - Must begin with a letter, number, or the underscore character (_), and must
        contain only letters, numbers, and the hyphen (-), period (.) hash (#), space
        ( ), at (@), equals (=), colon (:), and underscore characters.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my responder action" or my responder action').
    type: str
  reasonphrase:
    description:
      - 'Expression specifying the reason phrase of the HTTP response. The reason
        phrase may be a string literal with quotes or a PI expression. For example:
        "Invalid URL: " + HTTP.REQ.URL'
    type: str
  responsestatuscode:
    description:
      - HTTP response status code, for example 200, 302, 404, etc. The default value
        for the redirect action type is 302 and for respondwithhtmlpage is 200
    type: int
  target:
    description:
      - 'Expression specifying what to respond with. Typically a URL for redirect
        policies or a default-syntax expression.  In addition to Citrix ADC default-syntax
        expressions that refer to information in the request, a stringbuilder expression
        can contain text and HTML, and simple escape codes that define new lines and
        paragraphs. Enclose each stringbuilder expression element (either a Citrix
        ADC default-syntax expression or a string) in double quotation marks. Use
        the plus (+) character to join the elements. '
      - ''
      - 'Examples:'
      - '1) Respondwith expression that sends an HTTP 1.1 200 OK response:'
      - '"HTTP/1.1 200 OK\r\n\r\n"'
      - ''
      - 2) Redirect expression that redirects user to the specified web host and appends
        the request URL to the redirect.
      - '"http://backupsite2.com" + HTTP.REQ.URL'
      - ''
      - '3) Respondwith expression that sends an HTTP 1.1 404 Not Found response with
        the request URL included in the response:'
      - '"HTTP/1.1 404 Not Found\r\n\r\n"+ "HTTP.REQ.URL.HTTP_URL_SAFE" + "does not
        exist on the web server."'
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - Enclose the entire expression in single quotation marks. (Citrix ADC expression
        elements should be included inside the single quotation marks for the entire
        expression, but do not need to be enclosed in double quotation marks.)
    type: str
  type:
    choices:
      - noop
      - respondwith
      - redirect
      - respondwithhtmlpage
      - sqlresponse_ok
      - sqlresponse_error
    description:
      - 'Type of responder action. Available settings function as follows:'
      - '* C(respondwith) <target> - Respond to the request with the expression specified
        as the target.'
      - '* C(respondwithhtmlpage) - Respond to the request with the uploaded HTML
        page object specified as the target.'
      - '* C(redirect) - Redirect the request to the URL specified as the target.'
      - '* C(sqlresponse_ok) - Send an SQL OK response.'
      - '* C(sqlresponse_error) - Send an SQL ERROR response.'
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
