#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2025 Cloud Software Group, Inc.
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
module: botprofile_ratelimit_binding
short_description: Binding Resource definition for describing association between
  botprofile and ratelimit resources
description: Binding Resource definition for describing association between botprofile
  and ratelimit resources
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  bot_bind_comment:
    type: str
    description:
      - Any comments about this binding.
  bot_rate_limit_action:
    type: list
    choices:
      - NONE
      - LOG
      - DROP
      - REDIRECT
      - RESET
      - RESPOND_STATUS_TOO_MANY_REQUESTS
    description:
      - One or more actions to be taken when the current rate becomes more than the
        configured rate. Only C(LOG) action can be combined with C(DROP), C(REDIRECT),
        C(RESPOND_STATUS_TOO_MANY_REQUESTS) or C(RESET) action.
    elements: str
  bot_rate_limit_enabled:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable or disable rate-limit binding.
  bot_rate_limit_type:
    type: str
    choices:
      - SESSION
      - SOURCE_IP
      - URL
      - GEOLOCATION
      - JA3_FINGERPRINT
    description:
      - 'Rate-limiting type Following rate-limiting types are allowed:'
      - '*C(SOURCE_IP) - Rate-limiting based on the client IP.'
      - '*C(SESSION) - Rate-limiting based on the configured cookie name.'
      - '*C(URL) - Rate-limiting based on the configured C(URL).'
      - '*C(GEOLOCATION) - Rate-limiting based on the configured country name.'
  bot_rate_limit_url:
    type: str
    description:
      - URL for the resource based rate-limiting.
  bot_ratelimit:
    type: bool
    description:
      - Rate-limit binding. Maximum 30 bindings can be configured per profile for
        rate-limit detection. For SOURCE_IP type, only one binding can be configured,
        and for URL type, only one binding is allowed per URL, and for SESSION type,
        only one binding is allowed for a cookie name. To update the values of an
        existing binding, user has to first unbind that binding, and then needs to
        bind again with new values.
  condition:
    type: str
    description:
      - Expression to be used in a rate-limiting condition. This expression result
        must be a boolean value.
  cookiename:
    type: str
    description:
      - Cookie name which is used to identify the session for session rate-limiting.
  countrycode:
    type: str
    choices:
      - AF
      - AX
      - AL
      - DZ
      - AS
      - AD
      - AO
      - AI
      - AQ
      - AG
      - AR
      - AM
      - AW
      - AU
      - AT
      - AZ
      - BS
      - BH
      - BD
      - BB
      - BY
      - BE
      - BZ
      - BJ
      - BM
      - BT
      - BO
      - BQ
      - BA
      - BW
      - BR
      - IO
      - BN
      - BG
      - BF
      - BI
      - KH
      - CM
      - CA
      - CV
      - KY
      - CF
      - TD
      - CL
      - CN
      - CX
      - CC
      - CO
      - KM
      - CG
      - CD
      - CK
      - CR
      - CI
      - HR
      - CU
      - CW
      - CY
      - CZ
      - DK
      - DJ
      - DM
      - DO
      - EC
      - EG
      - SV
      - GQ
      - ER
      - EE
      - ET
      - FK
      - FO
      - FJ
      - FI
      - FR
      - GF
      - PF
      - TF
      - GA
      - GM
      - GE
      - DE
      - GH
      - GI
      - GR
      - GL
      - GD
      - GP
      - GU
      - GT
      - GG
      - GN
      - GW
      - GY
      - HT
      - HM
      - VA
      - HN
      - HK
      - HU
      - IS
      - IN
      - ID
      - IR
      - IQ
      - IE
      - IM
      - IL
      - IT
      - JM
      - JP
      - JE
      - JO
      - KZ
      - KE
      - KI
      - XK
      - KW
      - KG
      - LA
      - LV
      - LB
      - LS
      - LR
      - LY
      - LI
      - LT
      - LU
      - MO
      - MK
      - MG
      - MW
      - MY
      - MV
      - ML
      - MT
      - MH
      - MQ
      - MR
      - MU
      - YT
      - MX
      - FM
      - MD
      - MC
      - MN
      - ME
      - MS
      - MA
      - MZ
      - MM
      - NA
      - NR
      - NP
      - NL
      - NC
      - NZ
      - NI
      - NE
      - NG
      - NU
      - NF
      - KP
      - MP
      - 'NO'
      - OM
      - PK
      - PW
      - PS
      - PA
      - PG
      - PY
      - PE
      - PH
      - PN
      - PL
      - PT
      - PR
      - QA
      - RE
      - RO
      - RU
      - RW
      - BL
      - SH
      - KN
      - LC
      - MF
      - PM
      - VC
      - WS
      - SM
      - ST
      - SA
      - SN
      - RS
      - SC
      - SL
      - SG
      - SX
      - SK
      - SI
      - SB
      - SO
      - SZA
      - GS
      - KR
      - SS
      - ES
      - LK
      - SD
      - SR
      - SJ
      - SZ
      - SE
      - CH
      - SY
      - TW
      - TJ
      - TZ
      - TH
      - TL
      - TG
      - TK
      - TO
      - TT
      - TN
      - TR
      - TM
      - TC
      - TV
      - UG
      - UA
      - AE
      - GB
      - US
      - UM
      - UY
      - UZ
      - VU
      - VE
      - VN
      - VG
      - VI
      - WF
      - EH
      - YE
      - ZM
      - ZW
    description:
      - Country name which is used for geolocation rate-limiting.
  limittype:
    type: str
    choices:
      - BURSTY
      - SMOOTH
    description:
      - Rate-Limiting traffic Type
  logmessage:
    type: str
    description:
      - Message to be logged for this binding.
  name:
    type: str
    description:
      - Name for the profile. Must begin with a letter, number, or the underscore
        character (_), and must contain only letters, numbers, and the hyphen (-),
        period (.), pound (#), space ( ), at (@), equals (=), colon (:), and underscore
        (_) characters. Cannot be changed after the profile is added.
      - ''
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my profile" or 'my profile').
  rate:
    type: float
    description:
      - Maximum number of requests that are allowed in this session in the given period
        time.
  timeslice:
    type: float
    description:
      - Time interval during which requests are tracked to check if they cross the
        given rate.
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
