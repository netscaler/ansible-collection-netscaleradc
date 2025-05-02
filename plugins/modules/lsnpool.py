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
---
module: lsnpool
short_description: Configuration for LSN pool resource.
description: Configuration for LSN pool resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
  - Shiva Shankar Vaddepally (@shivashankar-vaddepally)
options:
  state:
    choices:
      - present
      - absent
      - unset
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(unset), the resource will be unset on the NetScaler ADC node.
    type: str
  consider_non_updatable_arguments:
    choices:
      - 'yes'
      - 'no'
    default: 'no'
    description:
      - Whether to consider non-updatable arguments in the resource.
    type: str
  maxportrealloctmq:
    type: float
    description:
      - Maximum number of ports for which the port reallocation timeout applies for
        each NAT IP address. In other words, the maximum deallocated-port queue size
        for which the reallocation timeout applies for each NAT IP address.
      - ''
      - When the queue size is full, the next port deallocated is reallocated immediately
        for a new LSN session.
  nattype:
    type: str
    choices:
      - DYNAMIC
      - DETERMINISTIC
    description:
      - 'Type of NAT IP address and port allocation (from the LSN pools bound to an
        LSN group) for subscribers (of the LSN client entity bound to the LSN group):'
      - ''
      - 'Available options function as follows:'
      - ''
      - '* Deterministic - Allocate a NAT IP address and a block of ports to each
        subscriber (of the LSN client bound to the LSN group). The Citrix ADC sequentially
        allocates NAT resources to these subscribers. The Citrix ADC ADC assigns the
        first block of ports (block size determined by the port block size parameter
        of the LSN group) on the beginning NAT IP address to the beginning subscriber
        IP address. The next range of ports is assigned to the next subscriber, and
        so on, until the NAT address does not have enough ports for the next subscriber.
        In this case, the first port block on the next NAT address is used for the
        subscriber, and so on.  Because each subscriber now receives a deterministic
        NAT IP address and a block of ports, a subscriber can be identified without
        any need for logging. For a connection, a subscriber can be identified based
        only on the NAT IP address and port, and the destination IP address and port.'
      - ' '
      - '* Dynamic - Allocate a random NAT IP address and a port from the LSN NAT
        pool for a subscriber''s connection. If port block allocation is enabled (in
        LSN pool) and a port block size is specified (in the LSN group), the Citrix
        ADC allocates a random NAT IP address and a block of ports for a subscriber
        when it initiates a connection for the first time. The ADC allocates this
        NAT IP address and a port (from the allocated block of ports) for different
        connections from this subscriber. If all the ports are allocated (for different
        subscriber''s connections) from the subscriber''s allocated port block, the
        ADC allocates a new random port block for the subscriber.'
      - Only LSN Pools and LSN groups with the same NAT type settings can be bound
        together. Multiples LSN pools can be bound to an LSN group. A maximum of 16
        LSN pools can be bound to an LSN group.
  poolname:
    type: str
    description:
      - 'Name for the LSN pool. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Cannot be changed after the LSN pool is created. The following requirement
        applies only to the Citrix ADC CLI: If the name includes one or more spaces,
        enclose the name in double or single quotation marks (for example, "lsn pool1"
        or ''lsn pool1'').'
  portblockallocation:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allocate a random NAT port block, from the available NAT port pool of an NAT
        IP address, for each subscriber when the NAT allocation is set as Dynamic
        NAT. For any connection initiated from a subscriber, the Citrix ADC allocates
        a NAT port from the subscriber's allocated NAT port block to create the LSN
        session.
      - ''
      - You must set the port block size in the bound LSN group. For a subscriber,
        if all the ports are allocated from the subscriber's allocated port block,
        the Citrix ADC allocates a new random port block for the subscriber.
      - ''
      - For Deterministic NAT, this parameter is enabled by default, and you cannot
        disable it.
  portrealloctimeout:
    type: float
    description:
      - 'The waiting time, in seconds, between deallocating LSN NAT ports (when an
        LSN mapping is removed) and reallocating them for a new LSN session. This
        parameter is necessary in order to prevent collisions between old and new
        mappings and sessions. It ensures that all established sessions are broken
        instead of redirected to a different subscriber. This is not applicable for
        ports used in:'
      - '* Deterministic NAT'
      - '* Address-Dependent filtering and Address-Port-Dependent filtering'
      - '* Dynamic NAT with port block allocation'
      - In these cases, ports are immediately reallocated.
  lsnpool_lsnip_binding:
    type: dict
    description: Bindings for lsnpool_lsnip_binding resource
    suboptions:
      mode:
        type: str
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
---
- name: Sample lsnpool playbook
  hosts: demo_netscalers
  gather_facts: false
  tasks:
    - name: Configure lsnpool
      delegate_to: localhost
      netscaler.adc.lsnpool:
        state: present
        poolname: pool4
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
