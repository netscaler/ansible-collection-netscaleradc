.. _netscaler_lb_vserver:


netscaler_lb_vserver - Manage load balancing vserver configuration
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.2.3


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage load balancing vserver configuration
* This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance


Requirements (on host that executes module)
-------------------------------------------

  * nitro python sdk


Options
-------

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
                <tr><td>appflowlog<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Apply AppFlow logging to the virtual server.</div><div>Default value = ENABLED</div><div>Possible values = ENABLED, DISABLED</div>        </td></tr>
                <tr><td>authentication<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>Enable or disable user authentication.</div><div>Default value = OFF</div>        </td></tr>
                <tr><td>authenticationhost<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Fully qualified domain name (FQDN) of the authentication virtual server to which the user must be redirected for authentication. Make sure that the Authentication parameter is set to ENABLED.</div><div>Minimum length = 3</div><div>Maximum length = 252</div>        </td></tr>
                <tr><td>authn401<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>Enable or disable user authentication with HTTP 401 responses.</div><div>Default value = OFF</div>        </td></tr>
                <tr><td>authnprofile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the authentication profile to be used when authentication is turned on.</div>        </td></tr>
                <tr><td>authnvsname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of an authentication virtual server with which to authenticate users.</div><div>Minimum length = 1</div><div>Maximum length = 252</div>        </td></tr>
                <tr><td>backuplbmethod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ROUNDROBIN</li><li>LEASTCONNECTION</li><li>LEASTRESPONSETIME</li><li>SOURCEIPHASH</li><li>LEASTBANDWIDTH</li><li>LEASTPACKETS</li><li>CUSTOMLOAD</li></ul></td>
        <td><div>Backup load balancing method. Becomes operational if the primary load balancing me</div><div>thod fails or cannot be used.</div><div>Valid only if the primary method is based on static proximity.</div><div>Default value = ROUNDROBIN</div>        </td></tr>
                <tr><td>backuppersistencetimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time period for which backup persistence is in effect.</div><div>Default value = 2</div><div>Minimum value = 2</div><div>Maximum value = 1440</div>        </td></tr>
                <tr><td>bypassaaaa<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>If this option is enabled while resolving DNS64 query AAAA queries are not sent to back end dns server.</div><div>Default value = NO</div>        </td></tr>
                <tr><td>cacheable<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Route cacheable requests to a cache redirection virtual server. The load balancing virtual server can forward requests only to a transparent cache redirection virtual server that has an IP address and port combination of *:80, so such a cache redirection virtual server must be configured on the appliance.</div><div>Default value = NO</div>        </td></tr>
                <tr><td>clttimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Idle time, in seconds, after which a client connection is terminated.</div><div>Minimum value = 0</div><div>Maximum value = 31536000</div>        </td></tr>
                <tr><td>comment<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Any comments that you might want to associate with the virtual server.</div>        </td></tr>
                <tr><td>connfailover<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>DISABLED</li><li>STATEFUL</li><li>STATELESS</li></ul></td>
        <td><div>Mode in which the connection failover feature must operate for the virtual server. After a failover, established TCP connections and UDP packet flows are kept active and resumed on the secondary appliance. Clients remain connected to the same servers. Available settings function as follows.</div><div>STATEFUL - The primary appliance shares state information with the secondary appliance, in real time, resulting in some runtime processing overhead.</div><div>STATELESS - State information is not shared, and the new primary appliance tries to re-create the packet flow on the basis of the information contained in the packets it receives.</div><div>DISABLED - Connection failover does not occur.</div><div>Default value = DISABLED</div>        </td></tr>
                <tr><td>cookiename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Use this parameter to specify the cookie name for COOKIE peristence type. It specifies the name of cookie with a maximum of 32 characters. If not specified, cookie name is internally generated.</div>        </td></tr>
                <tr><td>datalength<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Length of the token to be extracted from the data segment of an incoming packet, for use in the token method of load balancing. The length of the token, specified in bytes, must not be greater than 24 KB. Applicable to virtual servers of type TCP.</div><div>Minimum value = 1</div><div>Maximum value = 100</div>        </td></tr>
                <tr><td>dataoffset<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Offset to be considered when extracting a token from the TCP payload. Applicable to virtual servers, of type TCP, using the token method of load balancing. Must be within the first 24 KB of the TCP payload.</div><div>Minimum value = 0</div><div>Maximum value = 25400</div>        </td></tr>
                <tr><td>dbprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the DB profile whose settings are to be applied to the virtual server.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>dbslb<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Enable database specific load balancing for MySQL and MSSQL service types.</div><div>Default value = DISABLED</div>        </td></tr>
                <tr><td>disableprimaryondown<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>If the primary virtual server goes down, do not allow it to return to primary status until manually enabled.</div><div>Default value = DISABLED</div>        </td></tr>
                <tr><td>dns64<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>This argument is for enabling/disabling the dns64 on lbvserver.</div>        </td></tr>
                <tr><td>dnsprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the DNS profile to be associated with the VServer. DNS profile properties will be applied to the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>downstateflush<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.</div><div>Default value = ENABLED</div>        </td></tr>
                <tr><td>hashlength<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH load balancing methods.</div><div>Default value = 80</div><div>Minimum value = 1</div><div>Maximum value = 4096</div>        </td></tr>
                <tr><td>healththreshold<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Threshold in percent of active services below which vserver state is made down. If this threshold is 0, vserver state will be up even if one bound service is up.</div><div>Default value = 0</div><div>Minimum value = 0</div><div>Maximum value = 100</div>        </td></tr>
                <tr><td>httpprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the HTTP profile whose settings are to be applied to the virtual server.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>icmpvsrresponse<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>PASSIVE</li><li>ACTIVE</li></ul></td>
        <td><div>How the NetScaler appliance responds to ping requests received for an IP address that is common to one or more virtual servers. Available settings function as follows</div><div>If set to PASSIVE on all the virtual servers that share the IP address, the appliance always responds to the ping requests.</div><div>If set to ACTIVE on all the virtual servers that share the IP address, the appliance responds to the ping requests if at least one of the virtual servers is UP. Otherwise, the appliance does not respond.</div><div>If set to ACTIVE on some virtual servers and PASSIVE on the others, the appliance responds if at least one virtual server with the ACTIVE setting is UP. Otherwise, the appliance does not respond.</div><div>Note. This parameter is available at the virtual server level. A similar parameter, ICMP Response, is available at the IP address level, for IPv4 addresses of type VIP. To set that parameter, use the add ip command in the CLI or the Create IP dialog box in the GUI.</div><div>Default value = PASSIVE</div>        </td></tr>
                <tr><td>insertvserveripport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>OFF</li><li>VIPADDR</li><li>V6TOV4MAPPING</li></ul></td>
        <td><div>Insert an HTTP header, whose value is the IP address and port number of the virtual server, before forwarding a request to the server. The format of the header is &lt;vipHeader&gt;: &lt;virtual server IP address&gt;_&lt;port number &gt;, where vipHeader is the name that you specify for the header. If the virtual server has an IPv6 address, the address in the header is enclosed in brackets ([ and ]) to separate it from the port number. If you have mapped an IPv4 address to a virtual server's IPv6 address, the value of this parameter determines which IP address is inserted in the header, as follows</div><div>VIPADDR - Insert the IP address of the virtual server in the HTTP header regardless of whether the virtual server has an IPv4 address or an IPv6 address. A mapped IPv4 address, if configured, is ignored.</div><div>V6TOV4MAPPING - Insert the IPv4 address that is mapped to the virtual server's IPv6 address. If a mapped IPv4 address is not configured, insert the IPv6 address.</div><div>OFF - Disable header insertion.</div><div>Possible values = OFF, VIPADDR, V6TOV4MAPPING</div>        </td></tr>
                <tr><td>ipmask<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.</div>        </td></tr>
                <tr><td>ippattern<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern. Mutually exclusive with the IP Address parameter.</div><div>For example, if the IP pattern assigned to the virtual server is 198.51.100.0 and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254. You can also use a pattern such as 0.0.2.2 and a mask such as 0.0.255.255 (a reverse mask).</div><div>If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if virtual servers vs1 and vs2 have the same IP pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of vs1. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.</div>        </td></tr>
                <tr><td>ipv46<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IPv4 or IPv6 address to assign to the virtual server.</div>        </td></tr>
                <tr><td>l2conn<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition to the 4-tuple (&lt;source IP&gt;:&lt;source port&gt;::&lt;destination IP&gt;:&lt;destination port&gt;) that is used to identify a connection. Allows multiple TCP and non-TCP connections with the same 4-tuple to co-exist on the NetScaler appliance.</div><div>Possible values = ON, OFF</div>        </td></tr>
                <tr><td>lbmethod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ROUNDROBIN</li><li>LEASTCONNECTION</li><li>LEASTRESPONSETIME</li><li>URLHASH</li><li>DOMAINHASH</li><li>DESTINATIONIPHASH</li><li>SOURCEIPHASH</li><li>SRCIPDESTIPHASH</li><li>LEASTBANDWIDTH</li><li>LEASTPACKETS</li><li>TOKEN</li><li>SRCIPSRCPORTHASH</li><li>LRTM</li><li>CALLIDHASH</li><li>CUSTOMLOAD</li><li>LEASTREQUEST</li><li>AUDITLOGHASH</li><li>STATICPROXIMITY</li></ul></td>
        <td><div>Load balancing method. The available settings function as follows</div><div>ROUNDROBIN - Distribute requests in rotation, regardless of the load. Weights can be assigned to services to enforce weighted round robin distribution.</div><div>LEASTCONNECTION (default) - Select the service with the fewest connections.</div><div>LEASTRESPONSETIME - Select the service with the lowest average response time.</div><div>LEASTBANDWIDTH - Select the service currently handling the least traffic.</div><div>LEASTPACKETS - Select the service currently serving the lowest number of packets per second.</div><div>CUSTOMLOAD - Base service selection on the SNMP metrics obtained by custom load monitors.</div><div>LRTM - Select the service with the lowest response time. Response times are learned through monitoring probes. This method also takes the number of active connections into account.</div><div>Also available are a number of hashing methods, in which the appliance extracts a predetermined portion of the request, creates a hash of the portion, and then checks whether any previous requests had the same hash value. If it finds a match, it forwards the request to the service that served those previous requests. Following are the hashing methods</div><div>URLHASH - Create a hash of the request URL (or part of the URL).</div><div>DOMAINHASH - Create a hash of the domain name in the request (or part of the domain name). The domain name is taken from either the URL or the Host header. If the domain name appears in both locations, the URL is preferred. If the request does not contain a domain name, the load balancing method defaults to LEASTCONNECTION.</div><div>DESTINATIONIPHASH - Create a hash of the destination IP address in the IP header.</div><div>SOURCEIPHASH - Create a hash of the source IP address in the IP header.</div><div>TOKEN - Extract a token from the request, create a hash of the token, and then select the service to which any previous requests with the same token hash value were sent.</div><div>SRCIPDESTIPHASH - Create a hash of the string obtained by concatenating the source IP address and destination IP address in the IP header.</div><div>SRCIPSRCPORTHASH - Create a hash of the source IP address and source port in the IP header.</div><div>CALLIDHASH - Create a hash of the SIP Call-ID header.</div><div>Default value = LEASTCONNECTION</div>        </td></tr>
                <tr><td>listenpolicy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Default syntax expression identifying traffic accepted by the virtual server. Can be either an expression (for example, CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24) or the name of a named expression. In the above example, the virtual server accepts all requests whose destination IP address is in the 192.0.2.0/24 subnet.</div><div>Default value = "NONE"</div>        </td></tr>
                <tr><td>listenpriority<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Integer specifying the priority of the listen policy. A higher number specifies a lower priority. If a request matches the listen policies of more than one virtual server the virtual server whose listen policy has the highest priority (the lowest priority number) accepts the request.</div><div>Default value = 101</div><div>Minimum value = 0</div><div>Maximum value = 101</div>        </td></tr>
                <tr><td>m<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>IP</li><li>MAC</li><li>IPTUNNEL</li><li>TOS</li></ul></td>
        <td><div>Redirection mode for load balancing. Available settings function as follows</div><div>IP - Before forwarding a request to a server, change the destination IP address to the server's IP address.</div><div>MAC - Before forwarding a request to a server, change the destination MAC address to the server's MAC address. The destination IP address is not changed. MAC-based redirection mode is used mostly in firewall load balancing deployments.</div><div>IPTUNNEL - Perform IP-in-IP encapsulation for client IP packets. In the outer IP headers, set the destination IP address to the IP address of the server and the source IP address to the subnet IP (SNIP). The client IP packets are not modified. Applicable to both IPv4 and IPv6 packets.</div><div>TOS - Encode the virtual server's TOS ID in the TOS field of the IP header.</div><div>You can use either the IPTUNNEL or the TOS option to implement Direct Server Return (DSR).</div><div>Default value = IP</div>        </td></tr>
                <tr><td>macmoderetainvlan<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>This option is used to retain vlan information of incoming packet when macmode is enabled.</div><div>Default value = DISABLED</div>        </td></tr>
                <tr><td>maxautoscalemembers<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum number of members expected to be present when vserver is used in Autoscale.</div><div>Default value = 0</div><div>Minimum value = 0</div><div>Maximum value = 5000</div>        </td></tr>
                <tr><td>minautoscalemembers<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Minimum number of members expected to be present when vserver is used in Autoscale.</div><div>Default value = 0</div><div>Minimum value = 0</div><div>Maximum value = 5000</div>        </td></tr>
                <tr><td>mssqlserverversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>70</li><li>2000</li><li>2000SP1</li><li>2005</li><li>2008</li><li>2008R2</li><li>2012</li><li>2014</li></ul></td>
        <td><div>For a load balancing virtual server of type MSSQL, the Microsoft SQL Server version. Set this parameter if you expect some clients to run a version different from the version of the database. This setting provides compatibility between the client-side and server-side connections by ensuring that all communication conforms to the server's version.</div><div>Default value = 2008R2</div>        </td></tr>
                <tr><td>mysqlcharacterset<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Character set that the virtual server advertises to clients.</div>        </td></tr>
                <tr><td>mysqlprotocolversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>MySQL protocol version that the virtual server advertises to clients.</div>        </td></tr>
                <tr><td>mysqlservercapabilities<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Server capabilities that the virtual server advertises to clients.</div>        </td></tr>
                <tr><td>mysqlserverversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>MySQL server version string that the virtual server advertises to clients.</div><div>Minimum length = 1</div><div>Maximum length = 31</div>        </td></tr>
                <tr><td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen (-) characters. Can be changed after the virtual server is created.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>netmask<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IPv4 subnet mask to apply to the destination IP address or source IP address when the load balancing method is DESTINATIONIPHASH or SOURCEIPHASH.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>netprofile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the network profile to associate with the virtual server. If you set this parameter, the virtual server uses only the IP addresses in the network profile as source IP addresses when initiating connections with servers.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>newservicerequest<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of requests, or percentage of the load on existing services, by which to increase the load on a new service at each interval in slow-start mode. A non-zero value indicates that slow-start is applicable. A zero value indicates that the global RR startup parameter is applied. Changing the value to zero will cause services currently in slow start to take the full traffic as determined by the LB method. Subsequently, any new services added will use the global RR factor.</div><div>Default value = 0</div>        </td></tr>
                <tr><td>newservicerequestincrementinterval<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Interval, in seconds, between successive increments in the load on a new service or a service whose state has just changed from DOWN to UP. A value of 0 (zero) specifies manual slow start.</div><div>Default value = 0</div><div>Minimum value = 0</div><div>Maximum value = 3600</div>        </td></tr>
                <tr><td>newservicerequestunit<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>PER_SECOND</li><li>PERCENT</li></ul></td>
        <td><div>Units in which to increment load at each interval in slow-start mode.</div><div>Default value = PER_SECOND</div>        </td></tr>
                <tr><td>nitro_pass<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password with which to authenticate to the netscaler node.</div>        </td></tr>
                <tr><td>nitro_protocol<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>http</td>
        <td><ul><li>http</li><li>https</li></ul></td>
        <td><div>Which protocol to use when accessing the nitro API objects.</div>        </td></tr>
                <tr><td>nitro_timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>310</td>
        <td></td>
        <td><div>Time in seconds until a timeout error is thrown when establishing a new session with Netscaler</div>        </td></tr>
                <tr><td>nitro_user<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The username with which to authenticate to the netscaler node.</div>        </td></tr>
                <tr><td>nsip<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The ip address of the netscaler appliance where the nitro API calls will be made.</div><div>The port can be specified with the colon (:). E.g. 192.168.1.1:555.</div>        </td></tr>
                <tr><td>oracleserverversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>10G</li><li>11G</li></ul></td>
        <td><div>Oracle server version.</div><div>Default value = 10G</div>        </td></tr>
                <tr><td>persistencebackup<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>SOURCEIP</li><li>NONE</li></ul></td>
        <td><div>Backup persistence type for the virtual server. Becomes operational if the primary persistence mechanism fails.</div><div>Possible values = SOURCEIP, NONE</div>        </td></tr>
                <tr><td>persistencetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>SOURCEIP</li><li>COOKIEINSERT</li><li>SSLSESSION</li><li>RULE</li><li>URLPASSIVE</li><li>CUSTOMSERVERID</li><li>DESTIP</li><li>SRCIPDESTIP</li><li>CALLID</li><li>RTSPSID</li><li>DIAMETER</li><li>FIXSESSION</li><li>NONE</li></ul></td>
        <td><div>Type of persistence for the virtual server. Available settings function as follows</div><div>SOURCEIP - Connections from the same client IP address belong to the same persistence session.</div><div>COOKIEINSERT - Connections that have the same HTTP Cookie, inserted by a Set-Cookie directive from a server, belong to the same persistence session.</div><div>SSLSESSION - Connections that have the same SSL Session ID belong to the same persistence session.</div><div>CUSTOMSERVERID - Connections with the same server ID form part of the same session. For this persistence type, set the Server ID (CustomServerID) parameter for each service and configure the Rule parameter to identify the server ID in a request.</div><div>RULE - All connections that match a user defined rule belong to the same persistence session.</div><div>URLPASSIVE - Requests that have the same server ID in the URL query belong to the same persistence session. The server ID is the hexadecimal representation of the IP address and port of the service to which the request must be forwarded. This persistence type requires a rule to identify the server ID in the request.</div><div>DESTIP - Connections to the same destination IP address belong to the same persistence session.</div><div>SRCIPDESTIP - Connections that have the same source IP address and destination IP address belong to the same persistence session.</div><div>CALLID - Connections that have the same CALL-ID SIP header belong to the same persistence session.</div><div>RTSPSID - Connections that have the same RTSP Session ID belong to the same persistence session.</div><div>FIXSESSION - Connections that have the same SenderCompID and TargetCompID values belong to the same persistence session.</div>        </td></tr>
                <tr><td>persistmask<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Persistence mask for IP based persistence types, for IPv4 virtual servers.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Port number for the virtual server.</div><div>Range 1 - 65535</div><div>in CLI is represented as 65535 in NITRO API</div>        </td></tr>
                <tr><td>pq<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>Use priority queuing on the virtual server. based persistence types, for IPv6 virtual servers.</div><div>Default value = OFF</div>        </td></tr>
                <tr><td>processlocal<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>By turning on this option packets destined to a vserver in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.</div><div>Default value = DISABLED</div><div>Possible values = ENABLED, DISABLED</div>        </td></tr>
                <tr><td>push<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Process traffic with the push virtual server that is bound to this load balancing virtual server.</div><div>Default value = DISABLED</div>        </td></tr>
                <tr><td>pushlabel<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Expression for extracting a label from the server's response. Can be either an expression or the name of a named expression.</div><div>Default value = "none"</div>        </td></tr>
                <tr><td>pushmulticlients<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.</div><div>Default value = NO</div>        </td></tr>
                <tr><td>pushvserver<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which the server pushes updates received on the load balancing virtual server that you are configuring.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>range<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of IP addresses that the appliance must generate and assign to the virtual server. The virtual server then functions as a network virtual server, accepting traffic on any of the generated IP addresses. The IP addresses are generated automatically, as follows</div><div>For a range of n, the last octet of the address specified by the IP Address parameter increments n-1 times.</div><div>If the last octet exceeds 255, it rolls over to 0 and the third octet increments by 1.</div><div>Note. The Range parameter assigns multiple IP addresses to one virtual server. To generate an array of virtual servers, each of which owns only one IP address, use brackets in the IP Address and Name parameters to specify the range. For example</div><div>add lb vserver my_vserver[1-3] HTTP 192.0.2.[1-3] 80.</div><div>Default value. 1</div><div>Minimum value = 1</div><div>Maximum value = 254</div>        </td></tr>
                <tr><td>recursionavailable<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>When set to YES, this option causes the DNS replies from this vserver to have the RA bit turned on. Typically one would set this option to YES, when the vserver is load balancing a set of DNS servers thatsupport recursive queries.</div><div>Default value = NO</div>        </td></tr>
                <tr><td>redirectportrewrite<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Rewrite the port and change the protocol to ensure successful HTTP redirects from services.</div><div>Default value = DISABLED</div>        </td></tr>
                <tr><td>redirurl<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>URL to which to redirect traffic if the virtual server becomes unavailable.</div><div>WARNING! Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>rhistate<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>PASSIVE</li><li>ACTIVE</li></ul></td>
        <td><div>Route Health Injection (RHI) functionality of the NetSaler appliance for advertising the route of the VIP address associated with the virtual server. When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following are different RHI behaviors for the VIP address on the basis of RHIstate (RHI STATE) settings on the virtual servers associated with the VIP address.</div><div>If you set RHI STATE to PASSIVE on all virtual servers, the NetScaler ADC always advertises the route for the VIP address.</div><div>If you set RHI STATE to ACTIVE on all virtual servers, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers is in UP state.</div><div>If you set RHI STATE to ACTIVE on some and PASSIVE on others, the NetScaler ADC advertises the route for the VIP address if at least one of the associated virtual servers, whose RHI STATE set to ACTIVE, is in UP state.</div><div>Default value = PASSIVE</div>        </td></tr>
                <tr><td>rtspnat<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>Use network address translation (NAT) for RTSP data connections.</div><div>Default value = OFF</div>        </td></tr>
                <tr><td>save_config<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If true the module will save the configuration on the netscaler node if it makes any changes.</div><div>The module will not save the configuration on the netscaler node if it made no changes.</div>        </td></tr>
                <tr><td>sc<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>Use SureConnect on the virtual server.</div><div>Default value = OFF</div>        </td></tr>
                <tr><td>servicetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>HTTP</li><li>FTP</li><li>TCP</li><li>UDP</li><li>SSL</li><li>SSL_BRIDGE</li><li>SSL_TCP</li><li>DTLS</li><li>NNTP</li><li>DNS</li><li>DHCPRA</li><li>ANY</li><li>SIP_UDP</li><li>SIP_TCP</li><li>SIP_SSL</li><li>DNS_TCP</li><li>RTSP</li><li>PUSH</li><li>SSL_PUSH</li><li>RADIUS</li><li>RDP</li><li>MYSQL</li><li>MSSQL</li><li>DIAMETER</li><li>SSL_DIAMETER</li><li>TFTP</li><li>ORACLE</li><li>SMPP</li><li>SYSLOGTCP</li><li>SYSLOGUDP</li><li>FIX</li><li>SSL_FIX</li></ul></td>
        <td><div>Protocol used by the service (also called the service type).</div>        </td></tr>
                <tr><td>sessionless<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Perform load balancing on a per-packet basis, without establishing sessions. Recommended for load balancing of intrusion detection system (IDS) servers and scenarios involving direct server return (DSR), where session information is unnecessary.</div><div>Default value = DISABLED</div><div>Possible values = ENABLED, DISABLED</div>        </td></tr>
                <tr><td>skippersistency<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>Bypass</li><li>ReLb</li><li>None</li></ul></td>
        <td><div>This argument decides the behavior incase the service which is selected from an existing persistence session has reached threshold.</div><div>Default value = None</div>        </td></tr>
                <tr><td>sobackupaction<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>DROP</li><li>ACCEPT</li><li>REDIRECT</li></ul></td>
        <td><div>Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.</div>        </td></tr>
                <tr><td>somethod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>CONNECTION</li><li>DYNAMICCONNECTION</li><li>BANDWIDTH</li><li>HEALTH</li><li>NONE</li></ul></td>
        <td><div>Type of threshold that, when exceeded, triggers spillover. Available settings function as follows</div><div>CONNECTION - Spillover occurs when the number of client connections exceeds the threshold.</div><div>DYNAMICCONNECTION - Spillover occurs when the number of client connections at the virtual server exceeds the sum of the maximum client (Max Clients) settings for bound services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of bound services.</div><div>BANDWIDTH - Spillover occurs when the bandwidth consumed by the virtual server's incoming and outgoing traffic exceeds the threshold.</div><div>HEALTH - Spillover occurs when the percentage of weights of the services that are UP drops below the threshold. For example, if services svc1, svc2, and svc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2 and svc3 transition to DOWN.</div><div>NONE - Spillover does not occur.</div>        </td></tr>
                <tr><td>sopersistence<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>If spillover occurs, maintain source IP address based persistence for both primary and backup virtual servers.</div><div>Default value = DISABLED</div>        </td></tr>
                <tr><td>sopersistencetimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Timeout for spillover persistence, in minutes.</div><div>Default value = 2</div><div>Minimum value = 2</div><div>Maximum value = 1440</div>        </td></tr>
                <tr><td>sothreshold<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).</div><div>Minimum value = 1</div><div>Maximum value = 4294967287</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>The state of the resource being configured by the module on the netscaler node.</div><div>When present the resource will be created if needed and configured according to the module's parameters.</div><div>When absent the resource will be deleted from the netscaler node.</div>        </td></tr>
                <tr><td>tcpprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the TCP profile whose settings are to be applied to the virtual server.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time period for which a persistence session is in effect.</div><div>Default value = 2</div><div>Minimum value = 0</div><div>Maximum value = 1440</div>        </td></tr>
                <tr><td>tosid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>TOS ID of the virtual server. Applicable only when the load balancing redirection mode is set to TOS.</div><div>Minimum value = 1</div><div>Maximum value = 63</div>        </td></tr>
                <tr><td>v6netmasklen<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of bits to consider in an IPv6 destination or source IP address, for creating the hash that is required by the DESTINATIONIPHASH and SOURCEIPHASH load balancing methods.</div><div>Default value = 128</div><div>Minimum value = 1</div><div>Maximum value = 128</div>        </td></tr>
                <tr><td>v6persistmasklen<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Persistence mask for IP based persistence types, for IPv6 virtual servers.</div><div>Default value = 128</div><div>Minimum value = 1</div><div>Maximum value = 128</div>        </td></tr>
                <tr><td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td></td>
        <td><div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>        </td></tr>
                <tr><td>vipheader<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the inserted header. The default name is vip-header.</div><div>Minimum length = 1</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    # Netscaler services service-http-1, service-http-2 must have been already created with the netscaler_service module
    
    - name: Create a load balancing vserver bound to services
      local_action:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no
    
        module: netscaler_lb_vserver
        state: present
    
        name: lb_vserver_1
        servicetype: HTTP
        timeout: 12
        ipv46: 6.93.3.3
        port: 80
        servicebindings:
            -
                servicename: service-http-1
                weight: 80
            -
                servicename: service-http-2
                weight: 20
    
    # Service group service-group-1 must have been already created with the netscaler_servicegroup module
    
    - name: Create load balancing vserver bound to servicegroup
      local_action:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no
    
        module: netscaler_lb_vserver
        state: present
    
        name: lb_vserver_2
        servicetype: HTTP
        ipv46: 6.92.2.2
        port: 80
        timeout: 10
        servicegroupbindings:
            -
                servicegroupname: service-group-1

Return Values
-------------

Common return values are documented here :doc:`common_return_values`, the following are the fields unique to this module:

.. raw:: html

    <table border=1 cellpadding=4>
    <tr>
    <th class="head">name</th>
    <th class="head">description</th>
    <th class="head">returned</th>
    <th class="head">type</th>
    <th class="head">sample</th>
    </tr>

        <tr>
        <td> msg </td>
        <td> Message detailing the failure reason </td>
        <td align=center> failure </td>
        <td align=center> str </td>
        <td align=center> Action does not exist </td>
    </tr>
            <tr>
        <td> diff </td>
        <td> List of differences between the actual configured object and the configuration specified in the module </td>
        <td align=center> failure </td>
        <td align=center> dict </td>
        <td align=center> {'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0'} </td>
    </tr>
            <tr>
        <td> loglines </td>
        <td> list of logged messages by the module </td>
        <td align=center> always </td>
        <td align=center> list </td>
        <td align=center> ['message 1', 'message 2'] </td>
    </tr>
        
    </table>
    </br></br>




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~



For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/developing_test_pr` and :doc:`dev_guide/developing_modules`.