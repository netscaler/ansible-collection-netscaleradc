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
module: sslparameter
short_description: Configuration for SSL parameter resource.
description: Configuration for SSL parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  crlmemorysizemb:
    description:
      - Maximum memory size to use for certificate revocation lists (CRLs). This parameter
        reserves memory for a CRL but sets a limit to the maximum memory that the
        CRLs loaded on the appliance can consume.
    type: int
    default: 256
  cryptodevdisablelimit:
    description:
      - Limit to the number of disabled SSL chips after which the ADC restarts. A
        value of zero implies that the ADC does not automatically restart.
    type: int
  defaultprofile:
    description:
      - Global parameter used to enable default profile feature.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  denysslreneg:
    description:
      - 'Deny renegotiation in specified circumstances. Available settings function
        as follows:'
      - '* NO - Allow SSL renegotiation.'
      - '* FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated
        by the client.'
      - '* FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated
        by the client or the Citrix ADC during policy-based client authentication.'
      - '* ALL - Deny all secure and nonsecure SSL renegotiation.'
      - '* NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that
        support RFC 5746.'
    type: str
    default: ALL
    choices:
      - false
      - FRONTEND_CLIENT
      - FRONTEND_CLIENTSERVER
      - ALL
      - NONSECURE
  dropreqwithnohostheader:
    description:
      - Host header check for SNI enabled sessions. If this check is enabled and the
        HTTP request does not contain the host header for SNI enabled sessions(i.e
        vserver or profile bound to vserver has SNI enabled and 'Client Hello' arrived
        with SNI extension), the request is dropped.
    type: str
    choices:
      - true
      - false
  encrypttriggerpktcount:
    description:
      - Maximum number of queued packets after which encryption is triggered. Use
        this setting for SSL transactions that send small packets from server to Citrix
        ADC.
    type: int
    default: 45
  heterogeneoussslhw:
    description:
      - To support both cavium and coleto based platforms in cluster environment,
        this mode has to be enabled.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  hybridfipsmode:
    description:
      - When this mode is enabled, system will use additional crypto hardware to accelerate
        symmetric crypto operations.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  insertcertspace:
    description:
      - To insert space between lines in the certificate header of request
    type: str
    default: true
    choices:
      - true
      - false
  insertionencoding:
    description:
      - Encoding method used to insert the subject or issuer's name in HTTP requests
        to servers.
    type: str
    default: Unicode
    choices:
      - Unicode
      - UTF-8
  ndcppcompliancecertcheck:
    description:
      - Applies when the Citrix ADC appliance acts as a client (back-end connection).
      - 'Settings apply as follows:'
      - YES - During certificate verification, ignore the common name if SAN is present
        in the certificate.
      - NO - Do not ignore common name.
    type: str
    choices:
      - true
      - false
  ocspcachesize:
    description:
      - Size, per packet engine, in megabytes, of the OCSP cache. A maximum of 10%
        of the packet engine memory can be assigned. Because the maximum allowed packet
        engine memory is 4GB, the maximum value that can be assigned to the OCSP cache
        is approximately 410 MB.
    type: int
    default: 10
  operationqueuelimit:
    description:
      - Limit in percentage of capacity of the crypto operations queue beyond which
        new SSL connections are not accepted until the queue is reduced.
    type: int
    default: 150
  pushenctriggertimeout:
    description:
      - PUSH encryption trigger timeout value. The timeout value is applied only if
        you set the Push Encryption Trigger parameter to Timer in the SSL virtual
        server settings.
    type: int
    default: 1
  pushflag:
    description:
      - 'Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag
        is set to a value other than 0, the buffered records are forwarded on the
        basis of the value of the PUSH flag. Available settings function as follows:'
      - 0 - Auto (PUSH flag is not set.)
      - 1 - Insert PUSH flag into every decrypted record.
      - 2 -Insert PUSH flag into every encrypted record.
      - 3 - Insert PUSH flag into every decrypted and encrypted record.
    type: int
  quantumsize:
    description:
      - Amount of data to collect before the data is pushed to the crypto hardware
        for encryption. For large downloads, a larger quantum size better utilizes
        the crypto resources.
    type: str
    default: 8192
    choices:
      - 4096
      - 8192
      - 16384
  sendclosenotify:
    description:
      - Send an SSL Close-Notify message to the client at the end of a transaction.
    type: str
    default: true
    choices:
      - true
      - false
  sigdigesttype:
    description:
      - Signature Digest Algorithms that are supported by appliance. Default value
        is "ALL" and it will enable the following algorithms depending on the platform.
      - 'On VPX: ECDSA-SHA1 ECDSA-SHA224 ECDSA-SHA256 ECDSA-SHA384 ECDSA-SHA512 RSA-SHA1
        RSA-SHA224 RSA-SHA256 RSA-SHA384 RSA-SHA512 DSA-SHA1 DSA-SHA224 DSA-SHA256
        DSA-SHA384 DSA-SHA512'
      - 'On MPX with Nitrox-III and coleto cards: RSA-SHA1 RSA-SHA224 RSA-SHA256 RSA-SHA384
        RSA-SHA512 ECDSA-SHA1 ECDSA-SHA224 ECDSA-SHA256 ECDSA-SHA384 ECDSA-SHA512'
      - 'Others: RSA-SHA1 RSA-SHA224 RSA-SHA256 RSA-SHA384 RSA-SHA512.'
      - Note:ALL doesnot include RSA-MD5 for any platform.
    type: list
    elements: str
    default: ALL
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
  snihttphostmatch:
    description:
      - Controls how the HTTP 'Host' header value is validated. These checks are performed
        only if the session is SNI enabled (i.e when vserver or profile bound to vserver
        has SNI enabled and 'Client Hello' arrived with SNI extension) and HTTP request
        contains 'Host' header.
      - 'Available settings function as follows:'
      - CERT   - Request is forwarded if the 'Host' value is covered
      - '         by the certificate used to establish this SSL session.'
      - '         Note: ''CERT'' matching mode cannot be applied in'
      - '         TLS 1.3 connections established by resuming from a'
      - '         previous TLS 1.3 session. On these connections, ''STRICT'''
      - '         matching mode will be used instead.'
      - STRICT - Request is forwarded only if value of 'Host' header
      - '         in HTTP is identical to the ''Server name'' value passed'
      - '         in ''Client Hello'' of the SSL connection.'
      - NO     - No validation is performed on the HTTP 'Host'
      - '         header value.'
    type: str
    default: CERT
    choices:
      - false
      - CERT
      - STRICT
  softwarecryptothreshold:
    description:
      - Citrix ADC CPU utilization threshold (in percentage) beyond which crypto operations
        are not done in software.
      - A value of zero implies that CPU is not utilized for doing crypto in software.
    type: int
  sslierrorcache:
    description:
      - Enable or disable dynamically learning and caching the learned information
        to make the subsequent interception or bypass decision. When enabled, NS does
        the lookup of this cached data to do early bypass.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  sslimaxerrorcachemem:
    description:
      - Specify the maximum memory that can be used for caching the learned data.
        This memory is used as a LRU cache so that the old entries gets replaced with
        new entry once the set memory limit is fully utilised. A value of 0 decides
        the limit automatically.
    type: int
  ssltriggertimeout:
    description:
      - Time, in milliseconds, after which encryption is triggered for transactions
        that are not tracked on the Citrix ADC because their length is not known.
        There can be a delay of up to 10ms from the specified timeout value before
        the packet is pushed into the queue.
    type: int
    default: 100
  strictcachecks:
    description:
      - Enable strict CA certificate checks on the appliance.
    type: str
    choices:
      - true
      - false
  undefactioncontrol:
    description:
      - 'Name of the undefined built-in control action: CLIENTAUTH, NOCLIENTAUTH,
        NOOP, RESET, or DROP.'
    type: str
    default: '"CLIENTAUTH"'
  undefactiondata:
    description:
      - 'Name of the undefined built-in data action: NOOP, RESET or DROP.'
    type: str
    default: '"NOOP"'
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
