.. _netscaler_lb_monitor:


netscaler_lb_monitor - Manage load balancing monitors
+++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4.0


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage load balancing monitors.
* This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.


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
                <tr><td>Snmpoid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>SNMP OID for <code>SNMP</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>acctapplicationid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>4294967295</code></div>        </td></tr>
                <tr><td>action<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>NONE</li><li>LOG</li><li>DOWN</li></ul></td>
        <td><div>Action to perform when the response to an inline monitor (a monitor of type <code>HTTP-INLINE</code>) indicates that the service is down. A service monitored by an inline monitor is considered <code>DOWN</code> if the response code is not one of the codes that have been specified for the Response Code parameter.</div><div>Available settings function as follows:</div><div>* <code>NONE</code> - Do not take any action. However, the show service command and the show lb monitor command indicate the total number of responses that were checked and the number of consecutive error responses received after the last successful probe.</div><div>* <code>LOG</code> - Log the event in NSLOG or SYSLOG.</div><div>* <code>DOWN</code> - Mark the service as being down, and then do not direct any traffic to the service until the configured down time has expired. Persistent connections to the service are terminated as soon as the service is marked as <code>DOWN</code>. Also, log the event in NSLOG or SYSLOG.</div>        </td></tr>
                <tr><td>alertretries<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>32</code></div>        </td></tr>
                <tr><td>application<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the application used to determine the state of the service. Applicable to monitors of type <code>CITRIX-XML-SERVICE</code>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>attribute<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Attribute to evaluate when the LDAP server responds to the query. Success or failure of the monitoring probe depends on whether the attribute exists in the response. Optional.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>authapplicationid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring CER message.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>4294967295</code></div>        </td></tr>
                <tr><td>basedn<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The base distinguished name of the LDAP service, from where the LDAP server can begin the search for the attributes in the monitoring query. Required for <code>LDAP</code> service monitoring.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>binddn<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to <code>LDAP</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>customheaders<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Custom header string to include in the monitoring probes.</div>        </td></tr>
                <tr><td>database<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the database to connect to during authentication.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>destip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP address of the service to which to send probes. If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.</div>        </td></tr>
                <tr><td>destport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>TCP or UDP port to which to send the probe. If the parameter is set to 0, the port number of the service to which the monitor is bound is considered the destination port. For a monitor of type <code>USER</code>, however, the destination port is the port number that is included in the HTTP request sent to the dispatcher. Does not apply to monitors of type <code>PING</code>.</div>        </td></tr>
                <tr><td>deviation<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time value added to the learned average response time in dynamic response time monitoring (DRTM). When a deviation is specified, the appliance learns the average response time of bound services and adds the deviation to the average. The final value is then continually adjusted to accommodate response time variations over time. Specified in milliseconds, seconds, or minutes.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>20939</code></div>        </td></tr>
                <tr><td>dispatcherip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP address of the dispatcher to which to send the probe.</div>        </td></tr>
                <tr><td>dispatcherport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Port number on which the dispatcher listens for the monitoring probe.</div>        </td></tr>
                <tr><td>domain<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or Web Interface servers are present. Required by <code>CITRIX-XD-DDC</code> and <code>CITRIX-WI-EXTENDED</code> monitors for logging on to the DDC servers and Web Interface servers, respectively.</div>        </td></tr>
                <tr><td>downtime<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>20939</code></div>        </td></tr>
                <tr><td>evalrule<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Default syntax expression that evaluates the database server's response to a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines the state of the server. If the expression returns TRUE, the probe succeeds.</div><div>For example, if you want the appliance to evaluate the error message to determine the state of the server, use the rule <code>MYSQL.RES.ROW(10</code> .TEXT_ELE<span class='module'>2</span>.EQ("MySQL")).</div>        </td></tr>
                <tr><td>failureretries<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of retries that must fail, out of the number specified for the Retries parameter, for a service to be marked as DOWN. For example, if the Retries parameter is set to 10 and the Failure Retries parameter is set to 6, out of the ten probes sent, at least six probes must fail if the service is to be marked as DOWN. The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>32</code></div>        </td></tr>
                <tr><td>filename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of a file on the FTP server. The appliance monitors the FTP service by periodically checking the existence of the file on the server. Applicable to <code>FTP-EXTENDED</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>filter<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Filter criteria for the LDAP query. Optional.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>firmwarerevision<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>        </td></tr>
                <tr><td>group<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of a newsgroup available on the NNTP service that is to be monitored. The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response. If the newsgroup is found on the server, the service is marked as UP. If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>hostipaddress<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. If Host-IP-Address is not specified, the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address from which the CER request (the monitoring probe) is sent.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>hostname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Hostname in the FQDN format (Example: <code>porche.cars.org</code>). Applicable to <code>STOREFRONT</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>httprequest<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>HTTP request to send to the server (for example, <code>"HEAD /file.html"</code>).</div>        </td></tr>
                <tr><td>inbandsecurityid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>NO_INBAND_SECURITY</li><li>TLS</li></ul></td>
        <td><div>Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>        </td></tr>
                <tr><td>interval<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time interval between two successive probes. Must be greater than the value of Response Time-out.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>20940</code></div>        </td></tr>
                <tr><td>ipaddress<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to <code>DNS</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>iptunnel<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.</div>        </td></tr>
                <tr><td>kcdaccount<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>KCD Account used by <code>MSSQL</code> monitor.</div><div>Minimum length = 1</div><div>Maximum length = 32</div>        </td></tr>
                <tr><td>lasversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Version number of the Citrix Advanced Access Control Logon Agent. Required by the <code>CITRIX-AAC-LAS</code> monitor.</div>        </td></tr>
                <tr><td>logonpointname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software. Required if you want to monitor the associated login page or Logon Agent. Applicable to <code>CITRIX-AAC-LAS</code> and <code>CITRIX-AAC-LOGINPAGE</code> monitors.</div>        </td></tr>
                <tr><td>lrtm<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Calculate the least response times for bound services. If this parameter is not enabled, the appliance does not learn the response times of the bound services. Also used for LRTM load balancing.</div>        </td></tr>
                <tr><td>maxforwards<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type <code>SIP-UDP</code>.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>255</code></div>        </td></tr>
                <tr><td>metrictable<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Metric table to which to bind metrics.</div><div>Minimum length = 1</div><div>Maximum length = 99</div>        </td></tr>
                <tr><td>monitorname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the monitor. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore, hash <code>#</code>, period <code>.</code>, space <code> </code>, colon <code>:</code>, at <code>@</code>, equals <code>=</code>, and hyphen <code>-</code> characters.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>mssqlprotocolversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>70</li><li>2000</li><li>2000SP1</li><li>2005</li><li>2008</li><li>2008R2</li><li>2012</li><li>2014</li></ul></td>
        <td><div>Version of MSSQL server that is to be monitored.</div>        </td></tr>
                <tr><td>netprofile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the network profile.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
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
                <tr><td>oraclesid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the service identifier that is used to connect to the Oracle database during authentication.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>originhost<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>originrealm<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Password that is required for logging on to the <code>RADIUS</code>, <code>NNTP</code>, <code>FTP</code>, <code>FTP-EXTENDED</code>, <code>MYSQL</code>, <code>MSSQL</code>, <code>POP3</code>, <code>CITRIX-AG</code>, <code>CITRIX-XD-DDC</code>, <code>CITRIX-WI-EXTENDED</code>, <code>CITRIX-XNC-ECV</code> or <code>CITRIX-XDM</code> server. Used in conjunction with the user name specified for the <code>username</code> parameter.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>productname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>query<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Domain name to resolve as part of monitoring the DNS service (for example, <code>example.com</code>).</div>        </td></tr>
                <tr><td>querytype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>Address</li><li>Zone</li><li>AAAA</li></ul></td>
        <td><div>Type of DNS record for which to send monitoring queries. Set to <code>Address</code> for querying A records, <code>AAAA</code> for querying AAAA records, and <code>Zone</code> for querying the SOA record.</div>        </td></tr>
                <tr><td>radaccountsession<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Account Session ID to be used in Account Request Packet. Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>radaccounttype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Account Type to be used in Account Request Packet. Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div><div>Minimum value = 0</div><div>Maximum value = 15</div>        </td></tr>
                <tr><td>radapn<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Called Station Id to be used in Account Request Packet. Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>radframedip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Source ip with which the packet will go out . Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div>        </td></tr>
                <tr><td>radkey<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Authentication key (shared secret text string) for RADIUS clients and servers to exchange. Applicable to monitors of type <code>RADIUS</code> and <code>RADIUS_ACCOUNTING</code>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>radmsisdn<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>radnasid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type <code>RADIUS</code>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>radnasip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server. Applicable to monitors of type <code>RADIUS</code> and <code>RADIUS_ACCOUNTING</code>.</div>        </td></tr>
                <tr><td>recv<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>String expected from the server for the service to be marked as UP. Applicable to <code>TCP-ECV</code>, <code>HTTP-ECV</code>, and <code>UDP-ECV</code> monitors.</div>        </td></tr>
                <tr><td>respcode<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Response codes for which to mark the service as UP. For any other response code, the action performed depends on the monitor type. <code>HTTP</code> monitors and <code>RADIUS</code> monitors mark the service as <code>DOWN</code>, while <code>HTTP-INLINE</code> monitors perform the action indicated by the Action parameter.</div>        </td></tr>
                <tr><td>resptimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Amount of time for which the appliance must wait before it marks a probe as FAILED. Must be less than the value specified for the Interval parameter.</div><div>Note: For <code>UDP-ECV</code> monitors for which a receive string is not configured, response timeout does not apply. For <code>UDP-ECV</code> monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>20939</code></div>        </td></tr>
                <tr><td>resptimeoutthresh<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Response time threshold, specified as a percentage of the Response Time-out parameter. If the response to a monitor probe has not arrived when the threshold is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh. After the response time returns to a value below the threshold, the appliance generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated, the "MONITOR-RTO-THRESHOLD" alarm must also be enabled.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>100</code></div>        </td></tr>
                <tr><td>retries<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>127</code></div>        </td></tr>
                <tr><td>reverse<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.</div>        </td></tr>
                <tr><td>rtsprequest<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>RTSP request to send to the server (for example, <code>"OPTIONS *"</code>).</div>        </td></tr>
                <tr><td>save_config<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If true the module will save the configuration on the netscaler node if it makes any changes.</div><div>The module will not save the configuration on the netscaler node if it made no changes.</div>        </td></tr>
                <tr><td>scriptargs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>String of arguments for the script. The string is copied verbatim into the request.</div>        </td></tr>
                <tr><td>scriptname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Path and name of the script to execute. The script must be available on the NetScaler appliance, in the /nsconfig/monitors/ directory.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>secondarypassword<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to <code>CITRIX-AG</code> monitors.</div>        </td></tr>
                <tr><td>secure<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Use a secure SSL connection when monitoring a service. Applicable only to TCP based monitors. The secure option cannot be used with a <code>CITRIX-AG</code> monitor, because a CITRIX-AG monitor uses a secure connection by default.</div>        </td></tr>
                <tr><td>send<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>String to send to the service. Applicable to <code>TCP-ECV</code>, <code>HTTP-ECV</code>, and <code>UDP-ECV</code> monitors.</div>        </td></tr>
                <tr><td>sipmethod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>OPTIONS</li><li>INVITE</li><li>REGISTER</li></ul></td>
        <td><div>SIP method to use for the query. Applicable only to monitors of type <code>SIP-UDP</code>.</div>        </td></tr>
                <tr><td>sipreguri<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>SIP user to be registered. Applicable only if the monitor is of type <code>SIP-UDP</code> and the SIP Method parameter is set to <code>REGISTER</code>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>sipuri<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>SIP URI string to send to the service (for example, <code>sip:sip.test</code>). Applicable only to monitors of type <code>SIP-UDP</code>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>sitepath<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>URL of the logon page. For monitors of type <code>CITRIX-WEB-INTERFACE</code>, to monitor a dynamic page under the site path, terminate the site path with a slash <code>/</code>. Applicable to <code>CITRIX-WEB-INTERFACE</code>, <code>CITRIX-WI-EXTENDED</code> and <code>CITRIX-XDM</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>snmpcommunity<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Community name for <code>SNMP</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>snmpthreshold<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Threshold for <code>SNMP</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>snmpversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>V1</li><li>V2</li></ul></td>
        <td><div>SNMP version to be used for <code>SNMP</code> monitors.</div>        </td></tr>
                <tr><td>sqlquery<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>SQL query for a <code>MYSQL-ECV</code> or <code>MSSQL-ECV</code> monitor. Sent to the database server after the server authenticates the connection.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>State of the monitor. The <code>DISABLED</code> setting disables not only the monitor being configured, but all monitors of the same type, until the parameter is set to <code>ENABLED</code>. If the monitor is bound to a service, the state of the monitor is not taken into account when the state of the service is determined.</div>        </td></tr>
                <tr><td>storedb<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Store the database list populated with the responses to monitor probes. Used in database specific load balancing if <code>MSSQL-ECV</code>/<code>MYSQL-ECV</code> monitor is configured.</div>        </td></tr>
                <tr><td>storefrontacctservice<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Enable/Disable probing for Account Service. Applicable only to Store Front monitors. For multi-tenancy configuration users my skip account service.</div>        </td></tr>
                <tr><td>storefrontcheckbackendservices<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>This option will enable monitoring of services running on storefront server. Storefront services are monitored by probing to a Windows service that runs on the Storefront server and exposes details of which storefront services are running.</div>        </td></tr>
                <tr><td>storename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Store Name. For monitors of type <code>STOREFRONT</code>, <code>storename</code> is an optional argument defining storefront service store name. Applicable to <code>STOREFRONT</code> monitors.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>successretries<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of consecutive successful probes required to transition a service's state from DOWN to UP.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>32</code></div>        </td></tr>
                <tr><td>supportedvendorids<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>4294967295</code></div>        </td></tr>
                <tr><td>tos<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Probe the service by encoding the destination IP address in the IP TOS (6) bits.</div>        </td></tr>
                <tr><td>tosid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>63</code></div>        </td></tr>
                <tr><td>transparent<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>The monitor is bound to a transparent device such as a firewall or router. The state of a transparent device depends on the responsiveness of the services behind it. If a transparent device is being monitored, a destination IP address must be specified. The probe is sent to the specified IP address by using the MAC address of the transparent device.</div>        </td></tr>
                <tr><td>trofscode<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Code expected when the server is under maintenance.</div>        </td></tr>
                <tr><td>trofsstring<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>String expected from the server for the service to be marked as trofs. Applicable to HTTP-ECV/TCP-ECV monitors.</div>        </td></tr>
                <tr><td>type<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>PING</li><li>TCP</li><li>HTTP</li><li>TCP-ECV</li><li>HTTP-ECV</li><li>UDP-ECV</li><li>DNS</li><li>FTP</li><li>LDNS-PING</li><li>LDNS-TCP</li><li>LDNS-DNS</li><li>RADIUS</li><li>USER</li><li>HTTP-INLINE</li><li>SIP-UDP</li><li>SIP-TCP</li><li>LOAD</li><li>FTP-EXTENDED</li><li>SMTP</li><li>SNMP</li><li>NNTP</li><li>MYSQL</li><li>MYSQL-ECV</li><li>MSSQL-ECV</li><li>ORACLE-ECV</li><li>LDAP</li><li>POP3</li><li>CITRIX-XML-SERVICE</li><li>CITRIX-WEB-INTERFACE</li><li>DNS-TCP</li><li>RTSP</li><li>ARP</li><li>CITRIX-AG</li><li>CITRIX-AAC-LOGINPAGE</li><li>CITRIX-AAC-LAS</li><li>CITRIX-XD-DDC</li><li>ND6</li><li>CITRIX-WI-EXTENDED</li><li>DIAMETER</li><li>RADIUS_ACCOUNTING</li><li>STOREFRONT</li><li>APPC</li><li>SMPP</li><li>CITRIX-XNC-ECV</li><li>CITRIX-XDM</li><li>CITRIX-STA-SERVICE</li><li>CITRIX-STA-SERVICE-NHOP</li></ul></td>
        <td><div>Type of monitor that you want to create.</div>        </td></tr>
                <tr><td>units1<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>SEC</li><li>MSEC</li><li>MIN</li></ul></td>
        <td><div>Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.</div>        </td></tr>
                <tr><td>units2<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>SEC</li><li>MSEC</li><li>MIN</li></ul></td>
        <td><div>Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.</div>        </td></tr>
                <tr><td>units3<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>SEC</li><li>MSEC</li><li>MIN</li></ul></td>
        <td><div>monitor interval units.</div>        </td></tr>
                <tr><td>units4<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>SEC</li><li>MSEC</li><li>MIN</li></ul></td>
        <td><div>monitor response timeout units.</div>        </td></tr>
                <tr><td>username<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>User name with which to probe the <code>RADIUS</code>, <code>NNTP</code>, <code>FTP</code>, <code>FTP-EXTENDED</code>, <code>MYSQL</code>, <code>MSSQL</code>, <code>POP3</code>, <code>CITRIX-AG</code>, <code>CITRIX-XD-DDC</code>, <code>CITRIX-WI-EXTENDED</code>, <code>CITRIX-XNC</code> or <code>CITRIX-XDM</code> server.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td></td>
        <td><div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>        </td></tr>
                <tr><td>validatecred<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type <code>CITRIX-XD-DDC</code>.</div>        </td></tr>
                <tr><td>vendorid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>        </td></tr>
                <tr><td>vendorspecificacctapplicationids<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>4294967295</code></div>        </td></tr>
                <tr><td>vendorspecificauthapplicationids<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>4294967295</code></div>        </td></tr>
                <tr><td>vendorspecificvendorid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.</div><div>Minimum value = 1</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    - name: Set lb monitor
      local_action:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no
    
    
        module: netscaler_lb_monitor
        state: present
    
        monitorname: monitor_1
        type: HTTP-INLINE
        action: DOWN
        respcode: ['400']

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
        <td> loglines </td>
        <td> list of logged messages by the module </td>
        <td align=center> always </td>
        <td align=center> list </td>
        <td align=center> ['message 1', 'message 2'] </td>
    </tr>
            <tr>
        <td> diff </td>
        <td> List of differences between the actual configured object and the configuration specified in the module </td>
        <td align=center> failure </td>
        <td align=center> dict </td>
        <td align=center> {'targetlbvserver': 'difference. ours: (str) server1 other: (str) server2'} </td>
    </tr>
        
    </table>
    </br></br>




Status
~~~~~~

This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.


Support
~~~~~~~

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/developing_test_pr` and :doc:`dev_guide/developing_modules`.