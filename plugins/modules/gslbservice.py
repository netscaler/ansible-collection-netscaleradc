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
module: gslbservice
short_description: Configuration for GSLB service resource.
description: Configuration for GSLB service resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  appflowlog:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable logging appflow flow information
    type: str
    default: ENABLED
  cip:
    choices:
      - ENABLED
      - DISABLED
    description:
      - In the request that is forwarded to the GSLB service, insert a header that
        stores the client's IP address. Client IP header insertion is used in connection-proxy
        based site persistence.
    type: str
    default: DISABLED
  cipheader:
    description:
      - Name for the HTTP header that stores the client's IP address. Used with the
        Client IP option. If client IP header insertion is enabled on the service
        and a name is not specified for the header, the Citrix ADC uses the name specified
        by the cipHeader parameter in the set ns param command or, in the GUI, the
        Client IP Header parameter in the Configure HTTP Parameters dialog box.
    type: str
  clttimeout:
    description:
      - Idle time, in seconds, after which a client connection is terminated. Applicable
        if connection proxy based site persistence is used.
    type: int
  cnameentry:
    description:
      - Canonical name of the GSLB service. Used in CNAME-based GSLB.
    type: str
  comment:
    description:
      - Any comments that you might want to associate with the GSLB service.
    type: str
  cookietimeout:
    description:
      - Timeout value, in minutes, for the cookie, when cookie based site persistence
        is enabled.
    type: int
  downstateflush:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flush all active transactions associated with the GSLB service when its state
        transitions from UP to DOWN. Do not enable this option for services that must
        complete their transactions. Applicable if connection proxy based site persistence
        is used.
    type: str
  hashid:
    description:
      - Unique hash identifier for the GSLB service, used by hash based load balancing
        methods.
    type: int
  healthmonitor:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Monitor the health of the GSLB service.
    type: str
    default: 'YES'
  ip:
    description:
      - IP address for the GSLB service. Should represent a load balancing, content
        switching, or VPN virtual server on the Citrix ADC, or the IP address of another
        load balancing device.
    type: str
  ipaddress:
    description:
      - The new IP address of the service.
    type: str
  maxaaausers:
    description:
      - Maximum number of SSL VPN users that can be logged on concurrently to the
        VPN virtual server that is represented by this GSLB service. A GSLB service
        whose user count reaches the maximum is not considered when a GSLB decision
        is made, until the count drops below the maximum.
    type: int
  maxbandwidth:
    description:
      - Integer specifying the maximum bandwidth allowed for the service. A GSLB service
        whose bandwidth reaches the maximum is not considered when a GSLB decision
        is made, until its bandwidth consumption drops below the maximum.
    type: int
  maxclient:
    description:
      - The maximum number of open connections that the service can support at any
        given time. A GSLB service whose connection count reaches the maximum is not
        considered when a GSLB decision is made, until the connection count drops
        below the maximum.
    type: int
  monitor_name_svc:
    description:
      - Name of the monitor to bind to the service.
    type: str
  monthreshold:
    description:
      - Monitoring threshold value for the GSLB service. If the sum of the weights
        of the monitors that are bound to this GSLB service and are in the UP state
        is not equal to or greater than this threshold value, the service is marked
        as DOWN.
    type: int
  naptrdomainttl:
    description:
      - Modify the TTL of the internally created naptr domain
    type: int
    default: 3600
  naptrorder:
    description:
      - An integer specifying the order in which the NAPTR records MUST be processed
        in order to accurately represent the ordered list of Rules. The ordering is
        from lowest to highest
    type: int
    default: 1
  naptrpreference:
    description:
      - An integer specifying the preference of this NAPTR among NAPTR records having
        same order. lower the number, higher the preference.
    type: int
    default: 1
  naptrreplacement:
    description:
      - The replacement domain name for this NAPTR.
    type: str
  naptrservices:
    description:
      - Service Parameters applicable to this delegation path.
    type: str
  newname:
    description:
      - New name for the GSLB service.
    type: str
  port:
    description:
      - Port on which the load balancing entity represented by this GSLB service listens.
    type: int
  publicip:
    description:
      - The public IP address that a NAT device translates to the GSLB service's private
        IP address. Optional.
    type: str
  publicport:
    description:
      - The public port associated with the GSLB service's public IP address. The
        port is mapped to the service's private port number. Applicable to the local
        GSLB service. Optional.
    type: int
  servername:
    description:
      - Name of the server hosting the GSLB service.
    type: str
  servicename:
    description:
      - Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Can be changed after the GSLB service is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my gslbsvc" or ''my gslbsvc'').'
    type: str
  servicetype:
    choices:
      - HTTP
      - FTP
      - TCP
      - UDP
      - SSL
      - SSL_BRIDGE
      - SSL_TCP
      - NNTP
      - ANY
      - SIP_UDP
      - SIP_TCP
      - SIP_SSL
      - RADIUS
      - RDP
      - RTSP
      - MYSQL
      - MSSQL
      - ORACLE
    description:
      - Type of service to create.
    type: str
    default: NSSVC_SERVICE_UNKNOWN
  sitename:
    description:
      - Name of the GSLB site to which the service belongs.
    type: str
  sitepersistence:
    choices:
      - ConnectionProxy
      - HTTPRedirect
      - NONE
    description:
      - Use cookie-based site persistence. Applicable only to HTTP and SSL GSLB services.
    type: str
  siteprefix:
    description:
      - The site's prefix string. When the service is bound to a GSLB virtual server,
        a GSLB site domain is generated internally for each bound service-domain pair
        by concatenating the site prefix of the service and the name of the domain.
        If the special string NONE is specified, the site-prefix string is unset.
        When implementing HTTP redirect site persistence, the Citrix ADC redirects
        GSLB requests to GSLB services by using their site domains.
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable or disable the service.
    type: str
    default: ENABLED
  svrtimeout:
    description:
      - Idle time, in seconds, after which a server connection is terminated. Applicable
        if connection proxy based site persistence is used.
    type: int
  viewip:
    description:
      - IP address to be used for the given view
    type: str
  viewname:
    description:
      - Name of the DNS view of the service. A DNS view is used in global server load
        balancing (GSLB) to return a predetermined IP address to a specific group
        of clients, which are identified by using a DNS policy.
    type: str
  weight:
    description:
      - Weight to assign to the monitor-service binding. A larger number specifies
        a greater weight. Contributes to the monitoring threshold, which determines
        the state of the service.
    type: int
  gslbservice_dnsview_binding:
    type: dict
    description: Bindings for gslbservice_dnsview_binding resource
    suboptions:
      mode:
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
  gslbservice_lbmonitor_binding:
    type: dict
    description: Bindings for gslbservice_lbmonitor_binding resource
    suboptions:
      mode:
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
  gslbservicegroup_gslbservicegroupmember_binding:
    type: dict
    description: Bindings for gslbservicegroup_gslbservicegroupmember_binding resource
    suboptions:
      mode:
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
  gslbservicegroup_lbmonitor_binding:
    type: dict
    description: Bindings for gslbservicegroup_lbmonitor_binding resource
    suboptions:
      mode:
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
