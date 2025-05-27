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
module: subscribergxinterface
short_description: Configuration for Gx interface Parameters resource.
description: Configuration for Gx interface Parameters resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  cerrequesttimeout:
    type: int
    description:
      - q!Healthcheck request timeout, in seconds, after which the Citrix ADC considers
        that no CCA packet received to the initiated CCR. After this time Citrix ADC
        should send again CCR to PCRF server. !
  healthcheck:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - q!Set this setting to yes if Citrix ADC should send DWR packets to PCRF server.
        When the session is idle, healthcheck timer expires and DWR packets are initiated
        in order to check that PCRF server is active. By default set to No. !
  healthcheckttl:
    type: int
    description:
      - q!Healthcheck timeout, in seconds, after which the DWR will be sent in order
        to ensure the state of the PCRF server. Any CCR, CCA, RAR or RRA message resets
        the timer. !
  holdonsubscriberabsence:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Set this setting to yes if Citrix ADC needs to Hold pakcets till subscriber
        session is fetched from PCRF. Else set to C(NO). By default set to yes. If
        this setting is set to C(NO), then till Citrix ADC fetches subscriber from
        PCRF, default subscriber profile will be applied to this subscriber if configured.
        If default subscriber profile is also not configured an undef would be raised
        to expressions which use Subscriber attributes.
  idlettl:
    type: int
    description:
      - q!Idle Time, in seconds, after which the Gx CCR-U request will be sent after
        any PCRF activity on a session. Any RAR or CCA message resets the timer.
      - Zero value disables the idle timeout. !
  negativettl:
    type: int
    description:
      - q!Negative TTL, in seconds, after which the Gx CCR-I request will be resent
        for sessions that have not been resolved by PCRF due to server being down
        or no response or failed response. Instead of polling the PCRF server constantly,
        negative-TTL makes Citrix ADC stick to un-resolved session. Meanwhile Citrix
        ADC installs a negative session to avoid going to PCRF.
      - For Negative Sessions, Netcaler inherits the attributes from default subscriber
        profile if default subscriber is configured. A default subscriber could be
        configured as 'add subscriber profile *'. Or these attributes can be inherited
        from Radius as well if Radius is configued.
      - Zero value disables the Negative Sessions. And Citrix ADC does not install
        Negative sessions even if subscriber session could not be fetched. !
  negativettllimitedsuccess:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Set this to C(YES) if Citrix ADC should create negative session for Result-Code
        DIAMETER_LIMITED_SUCCESS (2002) received in CCA-I. If set to C(NO), regular
        session is created.
  nodeid:
    type: int
    description:
      - Unique number that identifies the cluster node.
  pcrfrealm:
    type: str
    description:
      - PCRF realm is of type DiameterIdentity and contains the realm of PCRF to which
        the message is to be routed. This is the realm used in Destination-Realm AVP
        by Citrix ADC Gx client (as a Diameter node).
  purgesdbongxfailure:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Set this setting to C(YES) if needed to purge Subscriber Database in case
        of Gx failure. By default set to C(NO).
  requestretryattempts:
    type: int
    description:
      - If the request does not complete within requestTimeout time, the request is
        retransmitted for requestRetryAttempts time.
  requesttimeout:
    type: int
    description:
      - q!Time, in seconds, within which the Gx CCR request must complete. If the
        request does not complete within this time, the request is retransmitted for
        requestRetryAttempts time. If still reuqest is not complete then default subscriber
        profile will be applied to this subscriber if configured. If default subscriber
        profile is also not configured an undef would be raised to expressions which
        use Subscriber attributes.
      - Zero disables the timeout. !
  revalidationtimeout:
    type: int
    description:
      - q!Revalidation Timeout, in seconds, after which the Gx CCR-U request will
        be sent after any PCRF activity on a session. Any RAR or CCA message resets
        the timer.
      - Zero value disables the idle timeout. !
  service:
    type: str
    description:
      - Name of DIAMETER/SSL_DIAMETER service corresponding to PCRF to which the Gx
        connection is established. The service type of the service must be DIAMETER/SSL_DIAMETER.
        Mutually exclusive with vserver parameter. Therefore, you cannot set both
        Service and the Virtual Server in the Gx Interface.
  servicepathavp:
    type: list
    description:
      - The AVP code in which PCRF sends service path applicable for subscriber.
    elements: int
  servicepathvendorid:
    type: int
    description:
      - The vendorid of the AVP in which PCRF sends service path for subscriber.
  vserver:
    type: str
    description:
      - Name of the load balancing, or content switching vserver to which the Gx connections
        are established. The service type of the virtual server must be DIAMETER/SSL_DIAMETER.
        Mutually exclusive with the service parameter. Therefore, you cannot set both
        service and the Virtual Server in the Gx Interface.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample subscribergxinterface playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure subscribergxinterface
      delegate_to: localhost
      netscaler.adc.subscribergxinterface:
        state: present
        revalidationtimeout: '300'
        negativettl: '300'
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
