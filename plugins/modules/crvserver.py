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
module: crvserver
short_description: Configuration for CR virtual server resource.
description: Configuration for CR virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
      - enabled
      - disabled
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
      - When C(enabled), the resource will be enabled on the NetScaler ADC node.
      - When C(disabled), the resource will be disabled on the NetScaler ADC node.
    type: str
  appflowlog:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable logging of AppFlow information.
  arp:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use ARP to determine the destination MAC address.
  backendssl:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Decides whether the backend connection made by Citrix ADC to the origin server
        will be HTTP or SSL. Applicable only for SSL type CR Forward proxy vserver.
  backupvserver:
    type: str
    description:
      - Name of the backup virtual server to which traffic is forwarded if the active
        server becomes unavailable.
  cachetype:
    type: str
    choices:
      - TRANSPARENT
      - REVERSE
      - FORWARD
    description:
      - 'Mode of operation for the cache redirection virtual server. Available settings
        function as follows:'
      - '* C(TRANSPARENT) - Intercept all traffic flowing to the appliance and apply
        cache redirection policies to determine whether content should be served from
        the cache or from the origin server.'
      - '* C(FORWARD) - Resolve the hostname of the incoming request, by using a DNS
        server, and forward requests for non-cacheable content to the resolved origin
        servers. Cacheable requests are sent to the configured cache servers.'
      - '* C(REVERSE) - Configure reverse proxy caches for specific origin servers.
        Incoming traffic directed to the reverse proxy can either be served from a
        cache server or be sent to the origin server with or without modification
        to the URL.'
      - The default value for cache type is C(TRANSPARENT) if service is HTTP or SSL
        whereas the default cache type is C(FORWARD) if the service is HDX.
  cachevserver:
    type: str
    description:
      - Name of the default cache virtual server to which to redirect requests (the
        default target of the cache redirection virtual server).
  clttimeout:
    type: float
    description:
      - Time-out value, in seconds, after which to terminate an idle client connection.
  comment:
    type: str
    description:
      - Comments associated with this virtual server.
  destinationvserver:
    type: str
    description:
      - Destination virtual server for a transparent or forward proxy cache redirection
        virtual server.
  disableprimaryondown:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Continue sending traffic to a backup virtual server even after the primary
        virtual server comes UP from the DOWN state.
  disallowserviceaccess:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - This is effective when a FORWARD type cr vserver is added. By default, this
        parameter is C(DISABLED). When it is C(ENABLED), backend services cannot be
        accessed through a FORWARD type cr vserver.
  dnsvservername:
    type: str
    description:
      - Name of the DNS virtual server that resolves domain names arriving at the
        forward proxy virtual server.
      - 'Note: This parameter applies only to forward proxy virtual servers, not reverse
        or transparent.'
  domain:
    type: str
    description:
      - Default domain for reverse proxies. Domains are configured to direct an incoming
        request from a specified source domain to a specified target domain. There
        can be several configured pairs of source and target domains. You can select
        one pair to be the default. If the host header or URL of an incoming request
        does not include a source domain, this option sends the request to the specified
        target domain.
  downstateflush:
    type: str
    choices:
      - ENABLED
      - DISABLED
    description:
      - Perform delayed cleanup of connections to this virtual server.
  format:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - '0'
  ghost:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - '0'
  httpprofilename:
    type: str
    description:
      - Name of the profile containing HTTP configuration information for cache redirection
        virtual server.
  icmpvsrresponse:
    type: str
    choices:
      - PASSIVE
      - ACTIVE
    description:
      - Criterion for responding to PING requests sent to this virtual server. If
        C(ACTIVE), respond only if the virtual server is available. If C(PASSIVE),
        respond even if the virtual server is not available.
  ipset:
    type: str
    description:
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening
        service on the current cr vserver
  ipv46:
    type: str
    description:
      - IPv4 or IPv6 address of the cache redirection virtual server. Usually a public
        IP address. Clients send connection requests to this IP address.
      - 'Note: For a transparent cache redirection virtual server, use an asterisk
        (*) to specify a wildcard virtual server address.'
  l2conn:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use L2 parameters, such as MAC, VLAN, and channel to identify a connection.
  listenpolicy:
    type: str
    description:
      - String specifying the listen policy for the cache redirection virtual server.
        Can be either an in-line expression or the name of a named expression.
  listenpriority:
    type: float
    description:
      - Priority of the listen policy specified by the Listen Policy parameter. The
        lower the number, higher the priority.
  map:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Obsolete.
  name:
    type: str
    description:
      - Name for the cache redirection virtual server. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Can be changed after the cache redirection virtual server
        is created.
      - 'The following requirement applies only to the Citrix ADC CLI:'
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my server" or 'my server').
  netprofile:
    type: str
    description:
      - Name of the network profile containing network configurations for the cache
        redirection virtual server.
  newname:
    type: str
    description:
      - New name for the cache redirection virtual server. Must begin with an ASCII
        alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric,
        underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign
        (=), and hyphen (-) characters. If the name includes one or more spaces, enclose
        the name in double or single quotation marks (for example, "my name" or 'my
        name').
  onpolicymatch:
    type: str
    choices:
      - CACHE
      - ORIGIN
    description:
      - Redirect requests that match the policy to either the cache or the origin
        server, as specified.
      - 'Note: For this option to work, you must set the cache redirection type to
        POLICY.'
  originusip:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use the client's IP address as the source IP address in requests sent to the
        origin server.
      - 'Note: You can enable this parameter to implement fully transparent CR deployment.'
  port:
    type: int
    description:
      - Port number of the virtual server.
  precedence:
    type: str
    choices:
      - RULE
      - URL
    description:
      - 'Type of policy (C(URL) or C(RULE)) that takes precedence on the cache redirection
        virtual server. Applies only to cache redirection virtual servers that have
        both C(URL) and C(RULE) based policies. If you specify C(URL), C(URL) based
        policies are applied first, in the following order:'
      - 1.   Domain and exact C(URL)
      - 2.   Domain, prefix and suffix
      - 3.   Domain and suffix
      - 4.   Domain and prefix
      - 5.   Domain only
      - 6.   Exact C(URL)
      - 7.   Prefix and suffix
      - 8.   Suffix only
      - 9.   Prefix only
      - 10.  Default
      - If you specify C(RULE), the rule based policies are applied before C(URL)
        based policies are applied.
  probeport:
    type: int
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select port for HTTP/TCP monitring
  probeprotocol:
    type: str
    choices:
      - TCP
      - HTTP
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select C(HTTP) or C(TCP) probes for healthcheck
  probesuccessresponsecode:
    type: str
    description:
      - HTTP code to return in SUCCESS case.
  range:
    type: float
    description:
      - Number of consecutive IP addresses, starting with the address specified by
        the IPAddress parameter, to include in a range of addresses assigned to this
        virtual server.
  redirect:
    type: str
    choices:
      - CACHE
      - POLICY
      - ORIGIN
    description:
      - 'Type of cache server to which to redirect HTTP requests. Available settings
        function as follows:'
      - '* C(CACHE) - Direct all requests to the cache.'
      - '* C(POLICY) - Apply the cache redirection policy to determine whether the
        request should be directed to the cache or to the origin.'
      - '* C(ORIGIN) - Direct all requests to the origin server.'
  redirecturl:
    type: str
    description:
      - URL of the server to which to redirect traffic if the cache redirection virtual
        server configured on the Citrix ADC becomes unavailable.
  reuse:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - 'Reuse TCP connections to the origin server across client connections. Do
        not set this parameter unless the Service Type parameter is set to HTTP. If
        you set this parameter to C(OFF), the possible settings of the Redirect parameter
        function as follows:'
      - '* CACHE - TCP connections to the cache servers are not reused.'
      - '* ORIGIN - TCP connections to the origin servers are not reused.'
      - '* POLICY - TCP connections to the origin servers are not reused.'
      - If you set the Reuse parameter to C(ON), connections to origin servers and
        connections to cache servers are reused.
  rhistate:
    type: str
    choices:
      - PASSIVE
      - ACTIVE
    description:
      - A host route is injected according to the setting on the virtual servers
      - '            * If set to C(PASSIVE) on all the virtual servers that share
        the IP address, the appliance always injects the hostroute.'
      - '            * If set to C(ACTIVE) on all the virtual servers that share the
        IP address, the appliance injects even if one virtual server is UP.'
      - '            * If set to C(ACTIVE) on some virtual servers and C(PASSIVE)
        on the others, the appliance, injects even if one virtual server set to C(ACTIVE)
        is UP.'
  servicetype:
    type: str
    choices:
      - HTTP
      - SSL
      - NNTP
      - HDX
    description:
      - Protocol (type of service) handled by the virtual server.
  sopersistencetimeout:
    type: float
    description:
      - Time-out, in minutes, for spillover persistence.
  sothreshold:
    type: float
    description:
      - For CONNECTION (or) DYNAMICCONNECTION spillover, the number of connections
        above which the virtual server enters spillover mode. For BANDWIDTH spillover,
        the amount of incoming and outgoing traffic (in Kbps) before spillover. For
        HEALTH spillover, the percentage of active services (by weight) below which
        spillover occurs.
  srcipexpr:
    type: str
    description:
      - Expression used to extract the source IP addresses from the requests originating
        from the cache. Can be either an in-line expression or the name of a named
        expression.
  tcpprobeport:
    type: int
    description:
      - Port number for external TCP probe. NetScaler provides support for external
        TCP health check of the vserver status over the selected port. This option
        is only supported for vservers assigned with an IPAddress or ipset.
  tcpprofilename:
    type: str
    description:
      - Name of the profile containing TCP configuration information for the cache
        redirection virtual server.
  td:
    type: float
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
  useoriginipportforcache:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Use origin ip/port while forwarding request to the cache. Change the destination
        IP, destination port of the request came to CR vserver to Origin IP and Origin
        Port and forward it to Cache
  useportrange:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use a port number from the port range (set by using the set ns param command,
        or in the Create Virtual Server (Cache Redirection) dialog box) as the source
        port in the requests sent to the origin server.
  via:
    type: str
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Insert a via header in each HTTP request. In the case of a cache miss, the
        request is redirected from the cache server to the origin server. This header
        indicates whether the request is being sent from a cache server.
  crvserver_analyticsprofile_binding:
    type: dict
    description: Bindings for crvserver_analyticsprofile_binding resource
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
  crvserver_appflowpolicy_binding:
    type: dict
    description: Bindings for crvserver_appflowpolicy_binding resource
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
  crvserver_appfwpolicy_binding:
    type: dict
    description: Bindings for crvserver_appfwpolicy_binding resource
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
  crvserver_appqoepolicy_binding:
    type: dict
    description: Bindings for crvserver_appqoepolicy_binding resource
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
  crvserver_cachepolicy_binding:
    type: dict
    description: Bindings for crvserver_cachepolicy_binding resource
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
  crvserver_cmppolicy_binding:
    type: dict
    description: Bindings for crvserver_cmppolicy_binding resource
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
  crvserver_crpolicy_binding:
    type: dict
    description: Bindings for crvserver_crpolicy_binding resource
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
  crvserver_cspolicy_binding:
    type: dict
    description: Bindings for crvserver_cspolicy_binding resource
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
  crvserver_feopolicy_binding:
    type: dict
    description: Bindings for crvserver_feopolicy_binding resource
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
  crvserver_icapolicy_binding:
    type: dict
    description: Bindings for crvserver_icapolicy_binding resource
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
  crvserver_lbvserver_binding:
    type: dict
    description: Bindings for crvserver_lbvserver_binding resource
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
  crvserver_policymap_binding:
    type: dict
    description: Bindings for crvserver_policymap_binding resource
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
  crvserver_responderpolicy_binding:
    type: dict
    description: Bindings for crvserver_responderpolicy_binding resource
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
  crvserver_rewritepolicy_binding:
    type: dict
    description: Bindings for crvserver_rewritepolicy_binding resource
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
  crvserver_spilloverpolicy_binding:
    type: dict
    description: Bindings for crvserver_spilloverpolicy_binding resource
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
