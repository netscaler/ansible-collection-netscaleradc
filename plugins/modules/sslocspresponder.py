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
module: sslocspresponder
short_description: Configuration for OCSP responser resource.
description: Configuration for OCSP responser resource.
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
  batchingdelay:
    type: float
    description:
      - Maximum time, in milliseconds, to wait to accumulate OCSP requests to batch.  Does
        not apply if the Batching Depth is 1.
  batchingdepth:
    type: float
    description:
      - Number of client certificates to batch together into one OCSP request. Batching
        avoids overloading the OCSP responder. A value of 1 signifies that each request
        is queried independently. For a value greater than 1, specify a timeout (batching
        delay) to avoid inordinately delaying the processing of a single certificate.
  cache:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable caching of responses. Caching of responses received from the OCSP responder
        enables faster responses to the clients and reduces the load on the OCSP responder.
  cachetimeout:
    type: float
    description:
      - Timeout for caching the OCSP response. After the timeout, the Citrix ADC sends
        a fresh request to the OCSP responder for the certificate status. If a timeout
        is not specified, the timeout provided in the OCSP response applies.
  httpmethod:
    type: str
    choices:
      - GET
      - POST
    description:
      - HTTP method used to send ocsp request. C(POST) is the default httpmethod.
        If request length is > 255, C(POST) wil be used even if C(GET) is set as httpMethod
  insertclientcert:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Include the complete client certificate in the OCSP request.
  name:
    type: str
    description:
      - Name for the OCSP responder. Cannot begin with a hash (#) or space character
        and must contain only ASCII alphanumeric, underscore (_), hash (#), period
        (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot
        be changed after the responder is created.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my responder" or 'my responder').
  ocspurlresolvetimeout:
    type: float
    description:
      - Time, in milliseconds, to wait for an OCSP URL Resolution. When this time
        elapses, an error message appears or the transaction is forwarded, depending
        on the settings on the virtual server.
  producedattimeskew:
    type: float
    description:
      - Time, in seconds, for which the Citrix ADC waits before considering the response
        as invalid. The response is considered invalid if the Produced At time stamp
        in the OCSP response exceeds or precedes the current Citrix ADC clock time
        by the amount of time specified.
  respondercert:
    type: str
    description:
      - '0'
  resptimeout:
    type: float
    description:
      - Time, in milliseconds, to wait for an OCSP response. When this time elapses,
        an error message appears or the transaction is forwarded, depending on the
        settings on the virtual server. Includes Batching Delay time.
  signingcert:
    type: str
    description:
      - Certificate-key pair that is used to sign OCSP requests. If this parameter
        is not set, the requests are not signed.
  trustresponder:
    type: bool
    description:
      - A certificate to use to validate OCSP responses.  Alternatively, if -trustResponder
        is specified, no verification will be done on the reponse.  If both are omitted,
        only the response times (producedAt, lastUpdate, nextUpdate) will be verified.
  url:
    type: str
    description:
      - URL of the OCSP responder.
  usenonce:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable the OCSP nonce extension, which is designed to prevent replay attacks.
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
