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
module: lbparameter
short_description: Configuration for LB parameter resource.
description: Configuration for LB parameter resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  allowboundsvcremoval:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This is used, to enable/disable the option of svc/svcgroup removal, if it
        is bound to one or more vserver. If it is enabled, the svc/svcgroup can be
        removed, even if it bound to vservers. If disabled, an error will be thrown,
        when the user tries to remove a svc/svcgroup without unbinding from its vservers.
    type: str
    default: ENABLED
  computedadccookieattribute:
    description:
      - 'ComputedADCCookieAttribute accepts ns variable as input in form of string
        starting with $ (to understand how to configure ns variable, please check
        man add ns variable). policies can be configured to modify this variable for
        every transaction and the final value of the variable after policy evaluation
        will be appended as attribute to Citrix ADC cookie (for example: LB cookie
        persistence , GSLB sitepersistence, CS cookie persistence, LB group cookie
        persistence). Only one of ComputedADCCookieAttribute, LiteralADCCookieAttribute
        can be set.'
      - ''
      - Sample usage -
      - '             add ns variable lbvar -type TEXT(100) -scope Transaction'
      - '             add ns assignment lbassign -variable $lbvar -set "\\";SameSite=Strict\\""'
      - '             add rewrite policy lbpol <valid policy expression> lbassign'
      - '             bind rewrite global lbpol 100 next -type RES_OVERRIDE'
      - '             set lb param -ComputedADCCookieAttribute "$lbvar"'
      - '             For incoming client request, if above policy evaluates TRUE,
        then SameSite=Strict will be appended to ADC generated cookie'
    type: str
  consolidatedlconn:
    choices:
      - 'YES'
      - 'NO'
    description:
      - To find the service with the fewest connections, the virtual server uses the
        consolidated connection statistics from all the packet engines. The C(NO)
        setting allows consideration of only the number of connections on the packet
        engine that received the new connection.
    type: str
    default: 'YES'
  cookiepassphrase:
    description:
      - Use this parameter to specify the passphrase used to generate secured persistence
        cookie value. It specifies the passphrase with a maximum of 31 characters.
    type: str
  dbsttl:
    description:
      - Specify the TTL for DNS record for domain based service. The default value
        of ttl is 0 which indicates to use the TTL received in DNS response for monitors
    type: int
  dropmqttjumbomessage:
    choices:
      - 'YES'
      - 'NO'
    description:
      - When this option is enabled, MQTT messages of length greater than 64k will
        be dropped and the client/server connections will be reset.
    type: str
    default: 'YES'
  httponlycookieflag:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Include the HttpOnly attribute in persistence cookies. The HttpOnly attribute
        limits the scope of a cookie to HTTP requests and helps mitigate the risk
        of cross-site scripting attacks.
    type: str
    default: ENABLED
  lbhashalgorithm:
    choices:
      - DEFAULT
      - PRAC
      - JARH
    description:
      - This option dictates the hashing algorithm used for hash based LB methods
        (URLHASH, DOMAINHASH, SOURCEIPHASH, DESTINATIONIPHASH, SRCIPDESTIPHASH, SRCIPSRCPORTHASH,
        TOKEN, USER_TOKEN, CALLIDHASH).
    type: str
    default: DEFAULT
  lbhashfingers:
    description:
      - This option is used to specify the number of fingers to be used in PRAC and
        JARH algorithms for hash based LB methods. Increasing the number of fingers
        might give better distribution of traffic at the expense of additional memory
    type: int
    default: 256
  literaladccookieattribute:
    description:
      - 'String configured as LiteralADCCookieAttribute will be appended as attribute
        for Citrix ADC cookie (for example: LB cookie persistence , GSLB site persistence,
        CS cookie persistence, LB group cookie persistence).'
      - ''
      - Sample usage -
      - '             set lb parameter -LiteralADCCookieAttribute ";SameSite=None"'
    type: str
  maxpipelinenat:
    description:
      - Maximum number of concurrent requests to allow on a single client connection,
        which is identified by the <clientip:port>-<vserver ip:port> tuple. This parameter
        is applicable to ANY service type and all UDP service types (except DNS) and
        only when "svrTimeout" is set to zero. A value of 0 (zero) applies no limit
        to the number of concurrent requests allowed on a single client connection
    type: int
  monitorconnectionclose:
    choices:
      - RESET
      - FIN
    description:
      - Close monitoring connections by sending the service a connection termination
        message with the specified bit set.
    type: str
    default: FIN
  monitorskipmaxclient:
    choices:
      - ENABLED
      - DISABLED
    description:
      - When a monitor initiates a connection to a service, do not check to determine
        whether the number of connections to the service has reached the limit specified
        by the service's Max Clients setting. Enables monitoring to continue even
        if the service has reached its connection limit.
    type: str
    default: DISABLED
  preferdirectroute:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Perform route lookup for traffic received by the Citrix ADC, and forward the
        traffic according to configured routes. Do not set this parameter if you want
        a wildcard virtual server to direct packets received by the appliance to an
        intermediary device, such as a firewall, even if their destination is directly
        connected to the appliance. Route lookup is performed after the packets have
        been processed and returned by the intermediary device.
    type: str
    default: 'YES'
  retainservicestate:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - This option is used to retain the original state of service or servicegroup
        member when an enable server command is issued.
    type: str
    default: 'OFF'
  startuprrfactor:
    description:
      - 'Number of requests, per service, for which to apply the round robin load
        balancing method before switching to the configured load balancing method,
        thus allowing services to ramp up gradually to full load. Until the specified
        number of requests is distributed, the Citrix ADC is said to be implementing
        the slow start mode (or startup round robin). Implemented for a virtual server
        when one of the following is true:'
      - '* The virtual server is newly created.'
      - '* One or more services are newly bound to the virtual server. '
      - '* One or more services bound to the virtual server are enabled.'
      - '* The load balancing method is changed.'
      - 'This parameter applies to all the load balancing virtual servers configured
        on the Citrix ADC, except for those virtual servers for which the virtual
        server-level slow start parameters (New Service Startup Request Rate and Increment
        Interval) are configured. If the global slow start parameter and the slow
        start parameters for a given virtual server are not set, the appliance implements
        a default slow start for the virtual server, as follows:'
      - '* For a newly configured virtual server, the appliance implements slow start
        for the first 100 requests received by the virtual server.'
      - '* For an existing virtual server, if one or more services are newly bound
        or newly enabled, or if the load balancing method is changed, the appliance
        dynamically computes the number of requests for which to implement startup
        round robin. It obtains this number by multiplying the request rate by the
        number of bound services (it includes services that are marked as DOWN). For
        example, if the current request rate is 20 requests/s and ten services are
        bound to the virtual server, the appliance performs startup round robin for
        200 requests.'
      - Not applicable to a virtual server for which a hash based load balancing method
        is configured.
    type: int
  storemqttclientidandusername:
    choices:
      - 'YES'
      - 'NO'
    description:
      - This option allows to store the MQTT clientid and username in transactional
        logs
    type: str
    default: 'NO'
  undefaction:
    description:
      - 'Action to perform when policy evaluation creates an UNDEF condition. Available
        settings function as follows:'
      - '* NOLBACTION - Does not consider LB action in making LB decision.'
      - '* RESET - Reset the request and notify the user, so that the user can resend
        the request.'
      - '* DROP - Drop the request without sending a response to the user.'
    type: str
    default: '"NOLBACTION"'
  useencryptedpersistencecookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Encode persistence cookie values using SHA2 hash.
    type: str
    default: DISABLED
  useportforhashlb:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Include the port number of the service when creating a hash for hash based
        load balancing methods. With the C(NO) setting, only the IP address of the
        service is considered when creating a hash.
    type: str
    default: 'YES'
  usesecuredpersistencecookie:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Encode persistence cookie values using SHA2 hash.
    type: str
    default: DISABLED
  vserverspecificmac:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Allow a MAC-mode virtual server to accept traffic returned by an intermediary
        device, such as a firewall, to which the traffic was previously forwarded
        by another MAC-mode virtual server. The second virtual server can then distribute
        that traffic across the destination server farm. Also useful when load balancing
        Branch Repeater appliances.
      - 'Note: The second virtual server can also send the traffic to another set
        of intermediary devices, such as another set of firewalls. If necessary, you
        can configure multiple MAC-mode virtual servers to pass traffic successively
        through multiple sets of intermediary devices.'
    type: str
    default: DISABLED
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
