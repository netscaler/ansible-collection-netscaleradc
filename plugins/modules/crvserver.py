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
module: crvserver
short_description: Configuration for CR virtual server resource.
description: Configuration for CR virtual server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  appflowlog:
    description:
      - Enable logging of AppFlow information.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  arp:
    description:
      - Use ARP to determine the destination MAC address.
    type: str
    choices:
      - true
      - false
  backendssl:
    description:
      - Decides whether the backend connection made by Citrix ADC to the origin server
        will be HTTP or SSL. Applicable only for SSL type CR Forward proxy vserver.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  backupvserver:
    description:
      - Name of the backup virtual server to which traffic is forwarded if the active
        server becomes unavailable.
    type: str
  cachetype:
    description:
      - 'Mode of operation for the cache redirection virtual server. Available settings
        function as follows:'
      - '* TRANSPARENT - Intercept all traffic flowing to the appliance and apply
        cache redirection policies to determine whether content should be served from
        the cache or from the origin server.'
      - '* FORWARD - Resolve the hostname of the incoming request, by using a DNS
        server, and forward requests for non-cacheable content to the resolved origin
        servers. Cacheable requests are sent to the configured cache servers.'
      - '* REVERSE - Configure reverse proxy caches for specific origin servers. Incoming
        traffic directed to the reverse proxy can either be served from a cache server
        or be sent to the origin server with or without modification to the URL.'
      - The default value for cache type is TRANSPARENT if service is HTTP or SSL
        whereas the default cache type is FORWARD if the service is HDX.
    type: str
    choices:
      - TRANSPARENT
      - REVERSE
      - FORWARD
  cachevserver:
    description:
      - Name of the default cache virtual server to which to redirect requests (the
        default target of the cache redirection virtual server).
    type: str
  clttimeout:
    description:
      - Time-out value, in seconds, after which to terminate an idle client connection.
    type: int
  comment:
    description:
      - Comments associated with this virtual server.
    type: str
  destinationvserver:
    description:
      - Destination virtual server for a transparent or forward proxy cache redirection
        virtual server.
    type: str
  disableprimaryondown:
    description:
      - Continue sending traffic to a backup virtual server even after the primary
        virtual server comes UP from the DOWN state.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  disallowserviceaccess:
    description:
      - This is effective when a FORWARD type cr vserver is added. By default, this
        parameter is DISABLED. When it is ENABLED, backend services cannot be accessed
        through a FORWARD type cr vserver.
    type: str
    default: DISABLED
    choices:
      - ENABLED
      - DISABLED
  dnsvservername:
    description:
      - Name of the DNS virtual server that resolves domain names arriving at the
        forward proxy virtual server.
      - 'Note: This parameter applies only to forward proxy virtual servers, not reverse
        or transparent.'
    type: str
  domain:
    description:
      - Default domain for reverse proxies. Domains are configured to direct an incoming
        request from a specified source domain to a specified target domain. There
        can be several configured pairs of source and target domains. You can select
        one pair to be the default. If the host header or URL of an incoming request
        does not include a source domain, this option sends the request to the specified
        target domain.
    type: str
  downstateflush:
    description:
      - Perform delayed cleanup of connections to this virtual server.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  format:
    description:
      - '0'
    type: str
    choices:
      - true
      - false
  ghost:
    description:
      - '0'
    type: str
    choices:
      - true
      - false
  httpprofilename:
    description:
      - Name of the profile containing HTTP configuration information for cache redirection
        virtual server.
    type: str
  icmpvsrresponse:
    description:
      - Criterion for responding to PING requests sent to this virtual server. If
        ACTIVE, respond only if the virtual server is available. If PASSIVE, respond
        even if the virtual server is not available.
    type: str
    default: PASSIVE
    choices:
      - PASSIVE
      - ACTIVE
  ipset:
    description:
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening
        service on the current cr vserver
    type: str
  ipv46:
    description:
      - IPv4 or IPv6 address of the cache redirection virtual server. Usually a public
        IP address. Clients send connection requests to this IP address.
      - 'Note: For a transparent cache redirection virtual server, use an asterisk
        (*) to specify a wildcard virtual server address.'
    type: str
  l2conn:
    description:
      - Use L2 parameters, such as MAC, VLAN, and channel to identify a connection.
    type: str
    choices:
      - true
      - false
  listenpolicy:
    description:
      - String specifying the listen policy for the cache redirection virtual server.
        Can be either an in-line expression or the name of a named expression.
    type: str
    default: '"NONE"'
  listenpriority:
    description:
      - Priority of the listen policy specified by the Listen Policy parameter. The
        lower the number, higher the priority.
    type: int
    default: 101
  map:
    description:
      - Obsolete.
    type: str
    choices:
      - true
      - false
  name:
    description:
      - Name for the cache redirection virtual server. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Can be changed after the cache redirection virtual server
        is created.
      - 'The following requirement applies only to the Citrix ADC CLI:  '
      - If the name includes one or more spaces, enclose the name in double or single
        quotation marks (for example, "my server" or 'my server').
    type: str
  netprofile:
    description:
      - Name of the network profile containing network configurations for the cache
        redirection virtual server.
    type: str
  newname:
    description:
      - New name for the cache redirection virtual server. Must begin with an ASCII
        alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric,
        underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign
        (=), and hyphen (-) characters. If the name includes one or more spaces, enclose
        the name in double or single quotation marks (for example, "my name" or 'my
        name').
    type: str
  onpolicymatch:
    description:
      - Redirect requests that match the policy to either the cache or the origin
        server, as specified.
      - 'Note: For this option to work, you must set the cache redirection type to
        POLICY.'
    type: str
    default: ORIGIN
    choices:
      - CACHE
      - ORIGIN
  originusip:
    description:
      - 'Use the client''s IP address as the source IP address in requests sent to
        the origin server.  '
      - 'Note: You can enable this parameter to implement fully transparent CR deployment.'
    type: str
    choices:
      - true
      - false
  port:
    description:
      - Port number of the virtual server.
    type: int
    default: 80
  precedence:
    description:
      - 'Type of policy (URL or RULE) that takes precedence on the cache redirection
        virtual server. Applies only to cache redirection virtual servers that have
        both URL and RULE based policies. If you specify URL, URL based policies are
        applied first, in the following order:'
      - 1.   Domain and exact URL
      - 2.   Domain, prefix and suffix
      - 3.   Domain and suffix
      - 4.   Domain and prefix
      - 5.   Domain only
      - 6.   Exact URL
      - 7.   Prefix and suffix
      - 8.   Suffix only
      - 9.   Prefix only
      - 10.  Default
      - If you specify RULE, the rule based policies are applied before URL based
        policies are applied.
    type: str
    default: RULE
    choices:
      - RULE
      - URL
  probeport:
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select port for HTTP/TCP monitring
    type: int
  probeprotocol:
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select HTTP or TCP probes for healthcheck
    type: str
    choices:
      - TCP
      - HTTP
  probesuccessresponsecode:
    description:
      - HTTP code to return in SUCCESS case.
    type: str
    default: '"200 OK"'
  range:
    description:
      - Number of consecutive IP addresses, starting with the address specified by
        the IPAddress parameter, to include in a range of addresses assigned to this
        virtual server.
    type: int
    default: 1
  redirect:
    description:
      - 'Type of cache server to which to redirect HTTP requests. Available settings
        function as follows:'
      - '* CACHE - Direct all requests to the cache.'
      - '* POLICY - Apply the cache redirection policy to determine whether the request
        should be directed to the cache or to the origin.'
      - '* ORIGIN - Direct all requests to the origin server.'
    type: str
    default: POLICY
    choices:
      - CACHE
      - POLICY
      - ORIGIN
  redirecturl:
    description:
      - URL of the server to which to redirect traffic if the cache redirection virtual
        server configured on the Citrix ADC becomes unavailable.
    type: str
  reuse:
    description:
      - 'Reuse TCP connections to the origin server across client connections. Do
        not set this parameter unless the Service Type parameter is set to HTTP. If
        you set this parameter to OFF, the possible settings of the Redirect parameter
        function as follows:'
      - '* CACHE - TCP connections to the cache servers are not reused.'
      - '* ORIGIN - TCP connections to the origin servers are not reused. '
      - '* POLICY - TCP connections to the origin servers are not reused.'
      - If you set the Reuse parameter to ON, connections to origin servers and connections
        to cache servers are reused.
    type: str
    default: true
    choices:
      - true
      - false
  rhistate:
    description:
      - A host route is injected according to the setting on the virtual servers
      - '            * If set to PASSIVE on all the virtual servers that share the
        IP address, the appliance always injects the hostroute.'
      - '            * If set to ACTIVE on all the virtual servers that share the
        IP address, the appliance injects even if one virtual server is UP.'
      - '            * If set to ACTIVE on some virtual servers and PASSIVE on the
        others, the appliance, injects even if one virtual server set to ACTIVE is
        UP.'
    type: str
    default: PASSIVE
    choices:
      - PASSIVE
      - ACTIVE
  servicetype:
    description:
      - Protocol (type of service) handled by the virtual server.
    type: str
    choices:
      - HTTP
      - SSL
      - NNTP
      - HDX
  sopersistencetimeout:
    description:
      - Time-out, in minutes, for spillover persistence.
    type: int
  sothreshold:
    description:
      - For CONNECTION (or) DYNAMICCONNECTION spillover, the number of connections
        above which the virtual server enters spillover mode. For BANDWIDTH spillover,
        the amount of incoming and outgoing traffic (in Kbps) before spillover. For
        HEALTH spillover, the percentage of active services (by weight) below which
        spillover occurs.
    type: int
  srcipexpr:
    description:
      - Expression used to extract the source IP addresses from the requests originating
        from the cache. Can be either an in-line expression or the name of a named
        expression.
    type: str
  state:
    description:
      - Initial state of the cache redirection virtual server.
    type: str
    default: ENABLED
    choices:
      - ENABLED
      - DISABLED
  tcpprobeport:
    description:
      - Port number for external TCP probe. NetScaler provides support for external
        TCP health check of the vserver status over the selected port. This option
        is only supported for vservers assigned with an IPAddress or ipset.
    type: int
  tcpprofilename:
    description:
      - Name of the profile containing TCP configuration information for the cache
        redirection virtual server.
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: int
  useoriginipportforcache:
    description:
      - Use origin ip/port while forwarding request to the cache. Change the destination
        IP, destination port of the request came to CR vserver to Origin IP and Origin
        Port and forward it to Cache
    type: str
    choices:
      - true
      - false
  useportrange:
    description:
      - Use a port number from the port range (set by using the set ns param command,
        or in the Create Virtual Server (Cache Redirection) dialog box) as the source
        port in the requests sent to the origin server.
    type: str
    choices:
      - true
      - false
  via:
    description:
      - Insert a via header in each HTTP request. In the case of a cache miss, the
        request is redirected from the cache server to the origin server. This header
        indicates whether the request is being sent from a cache server.
    type: str
    default: true
    choices:
      - true
      - false
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
