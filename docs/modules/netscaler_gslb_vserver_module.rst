.. __:


_ - _
+++++

.. versionadded:: 2.3.1


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* _


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
        <td><div>Enable logging appflow flow information.</div><div>Default value: ENABLED</div><div>Possible values = ENABLED, DISABLED</div>        </td></tr>
                <tr><td>backuplbmethod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ROUNDROBIN</li><li>LEASTCONNECTION</li><li>LEASTRESPONSETIME</li><li>SOURCEIPHASH</li><li>LEASTBANDWIDTH</li><li>LEASTPACKETS</li><li>STATICPROXIMITY</li><li>RTT</li><li>CUSTOMLOAD</li></ul></td>
        <td><div>Backup load balancing method. Becomes operational if the primary load balancing method fails or cannot be used. Valid only if the primary method is based on either round-trip time (RTT) or static proximity.</div><div>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD</div>        </td></tr>
                <tr><td>comment<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Any comments that you might want to associate with the GSLB virtual server.</div>        </td></tr>
                <tr><td>considereffectivestate<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>NONE</li><li>STATE_ONLY</li></ul></td>
        <td><div>If the primary state of all bound GSLB services is DOWN, consider the effective states of all the GSLB services, obtained through the Metrics Exchange Protocol (MEP), when determining the state of the GSLB virtual server. To consider the effective state, set the parameter to STATE_ONLY. To disregard the effective state, set the parameter to NONE.</div><div>The effective state of a GSLB service is the ability of the corresponding virtual server to serve traffic. The effective state of the load balancing virtual server, which is transferred to the GSLB service, is UP even if only one virtual server in the backup chain of virtual servers is in the UP state.</div><div>Default value: NONE</div><div>Possible values = NONE, STATE_ONLY</div>        </td></tr>
                <tr><td>disableprimaryondown<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Continue to direct traffic to the backup chain even after the primary GSLB virtual server returns to the UP state. Used when spillover is configured for the virtual server.</div><div>Default value: DISABLED</div><div>Possible values = ENABLED, DISABLED</div>        </td></tr>
                <tr><td>dnsrecordtype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>A</li><li>AAAA</li><li>CNAME</li><li>NAPTR</li></ul></td>
        <td><div>DNS record type to associate with the GSLB virtual server's domain name.</div><div>Default value: A</div><div>Possible values = A, AAAA, CNAME, NAPTR</div>        </td></tr>
                <tr><td>domain_bindings<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>List of bindings for domains for this glsb vserver. The following keys are valid.</div><div>domainname: Domain name for which to change the time to live (TTL) and/or backup service IP address.</div><div>cookietimeout: Timeout, in minutes, for the GSLB site cookie.</div><div>backupipflag: The IP address of the backup service for the specified domain name. Used when all the services bound to the domain are down, or when the backup chain of virtual servers is down.</div><div>ttl: Time to live (TTL) for the domain.</div><div>sitedomainttl: TTL, in seconds, for all internally created site domains (created when a site prefix is configured on a GSLB service) that are associated with this virtual server. Minimum value = 1</div>        </td></tr>
                <tr><td>dynamicweight<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>SERVICECOUNT</li><li>SERVICEWEIGHT</li><li>DISABLED</li></ul></td>
        <td><div>Specify if the appliance should consider the service count, service weights, or ignore both when using weight-based load balancing methods. The state of the number of services bound to the virtual server help the appliance to select the service.</div><div>Default value: DISABLED</div><div>Possible values = SERVICECOUNT, SERVICEWEIGHT, DISABLED</div>        </td></tr>
                <tr><td>lbmethod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ROUNDROBIN</li><li>LEASTCONNECTION</li><li>LEASTRESPONSETIME</li><li>SOURCEIPHASH</li><li>LEASTBANDWIDTH</li><li>LEASTPACKETS</li><li>STATICPROXIMITY</li><li>RTT</li><li>CUSTOMLOAD</li></ul></td>
        <td><div>Load balancing method for the GSLB virtual server.</div><div>Default value: LEASTCONNECTION</div><div>Possible values = ROUNDROBIN, LEASTCONNECTION, LEASTRESPONSETIME, SOURCEIPHASH, LEASTBANDWIDTH, LEASTPACKETS, STATICPROXIMITY, RTT, CUSTOMLOAD</div>        </td></tr>
                <tr><td>mir<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Include multiple IP addresses in the DNS responses sent to clients.</div><div>Default value: DISABLED</div><div>Possible values = ENABLED, DISABLED</div>        </td></tr>
                <tr><td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the GSLB virtual server. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Can be changed after the virtual server is created.</div><div>CLI Users:</div><div>If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my vserver" or 'my vserver').</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>netmask<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IPv4 network mask for use in the SOURCEIPHASH load balancing method.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>nitro_pass<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password with which to authenticate to the netscaler node.</div>        </td></tr>
                <tr><td>nitro_protocol<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>https</td>
        <td><ul><li>http</li><li>https</li></ul></td>
        <td><div>Which protocol to use when accessing the nitro API objects.</div>        </td></tr>
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
                <tr><td>operation<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>The operation to perform for the given netscaler module.</div><div>When present the resource will be created if needed and configured according to the module's parameters.</div><div>When absent the resource will be deleted from the netscaler node.</div>        </td></tr>
                <tr><td>persistenceid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The persistence ID for the GSLB virtual server. The ID is a positive integer that enables GSLB sites to identify the GSLB virtual server, and is required if source IP address based or spill over based persistence is enabled on the virtual server.</div><div>Minimum value = 0</div><div>Maximum value = 65535</div>        </td></tr>
                <tr><td>persistencetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>SOURCEIP</li><li>NONE</li></ul></td>
        <td><div>Use source IP address based persistence for the virtual server.</div><div>After the load balancing method selects a service for the first packet, the IP address received in response to the DNS query is used for subsequent requests from the same client.</div><div>Possible values = SOURCEIP, NONE</div>        </td></tr>
                <tr><td>persistmask<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The optional IPv4 network mask applied to IPv4 addresses to establish source IP address based persistence.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>service_bindings<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>List of bindings for gslb services bound to this gslb virtual server. The following keys are valid.</div><div>servicename: Name of the GSLB service for which to change the weight.</div><div>weight: Weight to assign to the GSLB service.</div>        </td></tr>
                <tr><td>servicetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>HTTP</li><li>FTP</li><li>TCP</li><li>UDP</li><li>SSL</li><li>SSL_BRIDGE</li><li>SSL_TCP</li><li>NNTP</li><li>ANY</li><li>SIP_UDP</li><li>SIP_TCP</li><li>SIP_SSL</li><li>RADIUS</li><li>RDP</li><li>RTSP</li><li>MYSQL</li><li>MSSQL</li><li>ORACLE</li></ul></td>
        <td><div>Protocol used by services bound to the virtual server.</div><div>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, NNTP, ANY, SIP_UDP, SIP_TCP, SIP_SSL, RADIUS, RDP, RTSP, MYSQL, MSSQL, ORACLE</div>        </td></tr>
                <tr><td>sobackupaction<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>DROP</li><li>ACCEPT</li><li>REDIRECT</li></ul></td>
        <td><div>Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.</div><div>Possible values = DROP, ACCEPT, REDIRECT</div>        </td></tr>
                <tr><td>somethod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>CONNECTION</li><li>DYNAMICCONNECTION</li><li>BANDWIDTH</li><li>HEALTH</li><li>NONE</li></ul></td>
        <td><div>Type of threshold that, when exceeded, triggers spillover. Available settings function as follows:</div><div>* CONNECTION - Spillover occurs when the number of client connections exceeds the threshold.</div><div>* DYNAMICCONNECTION - Spillover occurs when the number of client connections at the GSLB virtual server exceeds the sum of the maximum client (Max Clients) settings for bound GSLB services. Do not specify a spillover threshold for this setting, because the threshold is implied by the Max Clients settings of the bound GSLB services.</div><div>* BANDWIDTH - Spillover occurs when the bandwidth consumed by the GSLB virtual server's incoming and outgoing traffic exceeds the threshold.</div><div>* HEALTH - Spillover occurs when the percentage of weights of the GSLB services that are UP drops below the threshold. For example, if services gslbSvc1, gslbSvc2, and gslbSvc3 are bound to a virtual server, with weights 1, 2, and 3, and the spillover threshold is 50%, spillover occurs if gslbSvc1 and gslbSvc3 or gslbSvc2 and gslbSvc3 transition to DOWN.</div><div>* NONE - Spillover does not occur.</div><div>Possible values = CONNECTION, DYNAMICCONNECTION, BANDWIDTH, HEALTH, NONE</div>        </td></tr>
                <tr><td>sopersistence<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>If spillover occurs, maintain source IP address based persistence for both primary and backup GSLB virtual servers.</div><div>Default value: DISABLED</div><div>Possible values = ENABLED, DISABLED</div>        </td></tr>
                <tr><td>sopersistencetimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Timeout for spillover persistence, in minutes.</div><div>Default value: 2</div><div>Minimum value = 2</div><div>Maximum value = 1440</div>        </td></tr>
                <tr><td>sothreshold<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Threshold at which spillover occurs. Specify an integer for the CONNECTION spillover method, a bandwidth value in kilobits per second for the BANDWIDTH method (do not enter the units), or a percentage for the HEALTH method (do not enter the percentage symbol).</div><div>Minimum value = 1</div><div>Maximum value = 4294967287</div>        </td></tr>
                <tr><td>ssl_cert_validation<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>Whether to check the ssl certificate validity when using https to communicate with the netsaler node.</div>        </td></tr>
                <tr><td>timeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Idle time, in minutes, after which a persistence entry is cleared.</div><div>Default value: 2</div><div>Minimum value = 2</div><div>Maximum value = 1440</div>        </td></tr>
                <tr><td>tolerance<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Site selection tolerance, in milliseconds, for implementing the RTT load balancing method. If a site's RTT deviates from the lowest RTT by more than the specified tolerance, the site is not considered when the NetScaler appliance makes a GSLB decision. The appliance implements the round robin method of global server load balancing between sites whose RTT values are within the specified tolerance. If the tolerance is 0 (zero), the appliance always sends clients the IP address of the site with the lowest RTT.</div><div>Minimum value = 0</div><div>Maximum value = 100</div>        </td></tr>
                <tr><td>v6netmasklen<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of bits to consider, in an IPv6 source IP address, for creating the hash that is required by the SOURCEIPHASH load balancing method.</div><div>Default value: 128</div><div>Minimum value = 1</div><div>Maximum value = 128</div>        </td></tr>
                <tr><td>v6persistmasklen<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of bits to consider in an IPv6 source IP address when creating source IP address based persistence sessions.</div><div>Default value: 128</div><div>Minimum value = 1</div><div>Maximum value = 128</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    





Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/developing_test_pr` and :doc:`dev_guide/developing_modules`.