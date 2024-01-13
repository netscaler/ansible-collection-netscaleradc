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
module: sslparameter
short_description: Configuration for SSL parameter resource.
description: Configuration for SSL parameter resource.
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
  crlmemorysizemb:
    type: float
    description:
      - Maximum memory size to use for certificate revocation lists (CRLs). This parameter
        reserves memory for a CRL but sets a limit to the maximum memory that the
        CRLs loaded on the appliance can consume.
  cryptodevdisablelimit:
    type: float
    description:
      - Limit to the number of disabled SSL chips after which the ADC restarts. A
        value of zero implies that the ADC does not automatically restart.
  defaultprofile:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Global parameter used to enable default profile feature.
  denysslreneg:
    type: str
    choices:
      - 'NO'
      - FRONTEND_CLIENT
      - FRONTEND_CLIENTSERVER
      - ALL
      - NONSECURE
    description:
      - 'Deny renegotiation in specified circumstances. Available settings function
        as follows:'
      - '* C(NO) - Allow SSL renegotiation.'
      - '* C(FRONTEND_CLIENT) - Deny secure and nonsecure SSL renegotiation initiated
        by the client.'
      - '* C(FRONTEND_CLIENTSERVER) - Deny secure and nonsecure SSL renegotiation
        initiated by the client or the Citrix ADC during policy-based client authentication.'
      - '* C(ALL) - Deny all secure and nonsecure SSL renegotiation.'
      - '* C(NONSECURE) - Deny nonsecure SSL renegotiation. Allows only clients that
        support RFC 5746.'
  dropreqwithnohostheader:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Host header check for SNI enabled sessions. If this check is enabled and the
        HTTP request does not contain the host header for SNI enabled sessions(i.e
        vserver or profile bound to vserver has SNI enabled and 'Client Hello' arrived
        with SNI extension), the request is dropped.
  encrypttriggerpktcount:
    type: float
    description:
      - Maximum number of queued packets after which encryption is triggered. Use
        this setting for SSL transactions that send small packets from server to Citrix
        ADC.
  heterogeneoussslhw:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - To support both cavium and coleto based platforms in cluster environment,
        this mode has to be enabled.
  hybridfipsmode:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - When this mode is enabled, system will use additional crypto hardware to accelerate
        symmetric crypto operations.
  insertcertspace:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - To insert space between lines in the certificate header of request
  insertionencoding:
    type: str
    choices:
      - Unicode
      - UTF-8
    description:
      - Encoding method used to insert the subject or issuer's name in HTTP requests
        to servers.
  ndcppcompliancecertcheck:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Applies when the Citrix ADC appliance acts as a client (back-end connection).
      - 'Settings apply as follows:'
      - C(YES) - During certificate verification, ignore the common name if SAN is
        present in the certificate.
      - C(NO) - Do not ignore common name.
  ocspcachesize:
    type: float
    description:
      - Size, per packet engine, in megabytes, of the OCSP cache. A maximum of 10%
        of the packet engine memory can be assigned. Because the maximum allowed packet
        engine memory is 4GB, the maximum value that can be assigned to the OCSP cache
        is approximately 410 MB.
  operationqueuelimit:
    type: float
    description:
      - Limit in percentage of capacity of the crypto operations queue beyond which
        new SSL connections are not accepted until the queue is reduced.
  pushenctriggertimeout:
    type: float
    description:
      - PUSH encryption trigger timeout value. The timeout value is applied only if
        you set the Push Encryption Trigger parameter to Timer in the SSL virtual
        server settings.
  pushflag:
    type: float
    description:
      - 'Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag
        is set to a value other than 0, the buffered records are forwarded on the
        basis of the value of the PUSH flag. Available settings function as follows:'
      - 0 - Auto (PUSH flag is not set.)
      - 1 - Insert PUSH flag into every decrypted record.
      - 2 -Insert PUSH flag into every encrypted record.
      - 3 - Insert PUSH flag into every decrypted and encrypted record.
  quantumsize:
    type: str
    choices:
      - '4096'
      - '8192'
      - '16384'
    description:
      - Amount of data to collect before the data is pushed to the crypto hardware
        for encryption. For large downloads, a larger quantum size better utilizes
        the crypto resources.
  sendclosenotify:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Send an SSL Close-Notify message to the client at the end of a transaction.
  sigdigesttype:
    type: list
    choices:
      - ALL
      - RSA-MD5
      - RSA-SHA1
      - RSA-SHA224
      - RSA-SHA256
      - RSA-SHA384
      - RSA-SHA512
      - DSA-SHA1
      - DSA-SHA224
      - DSA-SHA256
      - DSA-SHA384
      - DSA-SHA512
      - ECDSA-SHA1
      - ECDSA-SHA224
      - ECDSA-SHA256
      - ECDSA-SHA384
      - ECDSA-SHA512
    description:
      - Signature Digest Algorithms that are supported by appliance. Default value
        is "C(ALL)" and it will enable the following algorithms depending on the platform.
      - 'On VPX: C(ECDSA-SHA1) C(ECDSA-SHA224) C(ECDSA-SHA256) C(ECDSA-SHA384) C(ECDSA-SHA512)
        C(RSA-SHA1) C(RSA-SHA224) C(RSA-SHA256) C(RSA-SHA384) C(RSA-SHA512) C(DSA-SHA1)
        C(DSA-SHA224) C(DSA-SHA256) C(DSA-SHA384) C(DSA-SHA512)'
      - 'On MPX with Nitrox-III and coleto cards: C(RSA-SHA1) C(RSA-SHA224) C(RSA-SHA256)
        C(RSA-SHA384) C(RSA-SHA512) C(ECDSA-SHA1) C(ECDSA-SHA224) C(ECDSA-SHA256)
        C(ECDSA-SHA384) C(ECDSA-SHA512)'
      - 'Others: C(RSA-SHA1) C(RSA-SHA224) C(RSA-SHA256) C(RSA-SHA384) C(RSA-SHA512).'
      - Note:C(ALL) doesnot include C(RSA-MD5) for any platform.
    elements: str
  snihttphostmatch:
    type: str
    choices:
      - 'NO'
      - CERT
      - STRICT
    description:
      - Controls how the HTTP 'Host' header value is validated. These checks are performed
        only if the session is SNI enabled (i.e when vserver or profile bound to vserver
        has SNI enabled and 'Client Hello' arrived with SNI extension) and HTTP request
        contains 'Host' header.
      - 'Available settings function as follows:'
      - C(CERT)   - Request is forwarded if the 'Host' value is covered
      - '         by the certificate used to establish this SSL session.'
      - '         Note: ''C(CERT)'' matching mode cannot be applied in'
      - '         TLS 1.3 connections established by resuming from a'
      - '         previous TLS 1.3 session. On these connections, ''C(STRICT)'''
      - '         matching mode will be used instead.'
      - C(STRICT) - Request is forwarded only if value of 'Host' header
      - '         in HTTP is identical to the ''Server name'' value passed'
      - '         in ''Client Hello'' of the SSL connection.'
      - C(NO)     - No validation is performed on the HTTP 'Host'
      - '         header value.'
  softwarecryptothreshold:
    type: float
    description:
      - Citrix ADC CPU utilization threshold (in percentage) beyond which crypto operations
        are not done in software.
      - A value of zero implies that CPU is not utilized for doing crypto in software.
  sslierrorcache:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable dynamically learning and caching the learned information
        to make the subsequent interception or bypass decision. When enabled, NS does
        the lookup of this cached data to do early bypass.
  sslimaxerrorcachemem:
    type: float
    description:
      - Specify the maximum memory that can be used for caching the learned data.
        This memory is used as a LRU cache so that the old entries gets replaced with
        new entry once the set memory limit is fully utilised. A value of 0 decides
        the limit automatically.
  ssltriggertimeout:
    type: float
    description:
      - Time, in milliseconds, after which encryption is triggered for transactions
        that are not tracked on the Citrix ADC because their length is not known.
        There can be a delay of up to 10ms from the specified timeout value before
        the packet is pushed into the queue.
  strictcachecks:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Enable strict CA certificate checks on the appliance.
  undefactioncontrol:
    type: str
    description:
      - 'Name of the undefined built-in control action: CLIENTAUTH, NOCLIENTAUTH,
        NOOP, RESET, or DROP.'
  undefactiondata:
    type: str
    description:
      - 'Name of the undefined built-in data action: NOOP, RESET or DROP.'
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
