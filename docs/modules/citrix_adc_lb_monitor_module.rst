:source: citrix_adc_lb_monitor.py

:orphan:

.. _citrix_adc_lb_monitor_module:


citrix_adc_lb_monitor - Manage load balancing monitors
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Manage load balancing monitors.
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- nitro python sdk


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="1">
                    <b>acctapplicationid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of Acct-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>4294967295</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>action</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>NONE</li>
                                                                                                                                                                                                <li>LOG</li>
                                                                                                                                                                                                <li>DOWN</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Action to perform when the response to an inline monitor (a monitor of type <code>HTTP-INLINE</code>) indicates that the service is down. A service monitored by an inline monitor is considered <code>DOWN</code> if the response code is not one of the codes that have been specified for the Response Code parameter.</div>
                                                    <div>Available settings function as follows:</div>
                                                    <div>* <code>NONE</code> - Do not take any action. However, the show service command and the show lb monitor command indicate the total number of responses that were checked and the number of consecutive error responses received after the last successful probe.</div>
                                                    <div>* <code>LOG</code> - Log the event in NSLOG or SYSLOG.</div>
                                                    <div>* <code>DOWN</code> - Mark the service as being down, and then do not direct any traffic to the service until the configured down time has expired. Persistent connections to the service are terminated as soon as the service is marked as <code>DOWN</code>. Also, log the event in NSLOG or SYSLOG.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>alertretries</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Number of consecutive probe failures after which the appliance generates an SNMP trap called monProbeFailed.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>32</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>application</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the application used to determine the state of the service. Applicable to monitors of type <code>CITRIX-XML-SERVICE</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>attribute</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Attribute to evaluate when the LDAP server responds to the query. Success or failure of the monitoring probe depends on whether the attribute exists in the response. Optional.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>authapplicationid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring CER message.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>4294967295</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>basedn</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The base distinguished name of the LDAP service, from where the LDAP server can begin the search for the attributes in the monitoring query. Required for <code>LDAP</code> service monitoring.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>binddn</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The distinguished name with which an LDAP monitor can perform the Bind operation on the LDAP server. Optional. Applicable to <code>LDAP</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>customheaders</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Custom header string to include in the monitoring probes.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>database</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the database to connect to during authentication.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>destip</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>IP address of the service to which to send probes. If the parameter is set to 0, the IP address of the server to which the monitor is bound is considered the destination IP address.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>destport</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>TCP or UDP port to which to send the probe. If the parameter is set to 0, the port number of the service to which the monitor is bound is considered the destination port. For a monitor of type <code>USER</code>, however, the destination port is the port number that is included in the HTTP request sent to the dispatcher. Does not apply to monitors of type <code>PING</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>deviation</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Time value added to the learned average response time in dynamic response time monitoring (DRTM). When a deviation is specified, the appliance learns the average response time of bound services and adds the deviation to the average. The final value is then continually adjusted to accommodate response time variations over time. Specified in milliseconds, seconds, or minutes.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>20939</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>dispatcherip</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>IP address of the dispatcher to which to send the probe.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>dispatcherport</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Port number on which the dispatcher listens for the monitoring probe.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>domain</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Domain in which the XenDesktop Desktop Delivery Controller (DDC) servers or Web Interface servers are present. Required by <code>CITRIX-XD-DDC</code> and <code>CITRIX-WI-EXTENDED</code> monitors for logging on to the DDC servers and Web Interface servers, respectively.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>downtime</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Time duration for which to wait before probing a service that has been marked as DOWN. Expressed in milliseconds, seconds, or minutes.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>20939</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>evalrule</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Default syntax expression that evaluates the database server&#x27;s response to a MYSQL-ECV or MSSQL-ECV monitoring query. Must produce a Boolean result. The result determines the state of the server. If the expression returns TRUE, the probe succeeds.</div>
                                                    <div>For example, if you want the appliance to evaluate the error message to determine the state of the server, use the rule <code>MYSQL.RES.ROW(10</code> .TEXT_ELE<span class='module'>2</span>.EQ(&quot;MySQL&quot;)).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>failureretries</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Number of retries that must fail, out of the number specified for the Retries parameter, for a service to be marked as DOWN. For example, if the Retries parameter is set to 10 and the Failure Retries parameter is set to 6, out of the ten probes sent, at least six probes must fail if the service is to be marked as DOWN. The default value of 0 means that all the retries must fail if the service is to be marked as DOWN.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>32</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>filename</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of a file on the FTP server. The appliance monitors the FTP service by periodically checking the existence of the file on the server. Applicable to <code>FTP-EXTENDED</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>filter</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Filter criteria for the LDAP query. Optional.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>firmwarerevision</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Firmware-Revision value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>group</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of a newsgroup available on the NNTP service that is to be monitored. The appliance periodically generates an NNTP query for the name of the newsgroup and evaluates the response. If the newsgroup is found on the server, the service is marked as UP. If the newsgroup does not exist or if the search fails, the service is marked as DOWN. Applicable to NNTP monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>hostipaddress</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Host-IP-Address value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. If Host-IP-Address is not specified, the appliance inserts the mapped IP (MIP) address or subnet IP (SNIP) address from which the CER request (the monitoring probe) is sent.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>hostname</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Hostname in the FQDN format (Example: <code>porche.cars.org</code>). Applicable to <code>STOREFRONT</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>httprequest</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>HTTP request to send to the server (for example, <code>&quot;HEAD /file.html&quot;</code>).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>inbandsecurityid</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>NO_INBAND_SECURITY</li>
                                                                                                                                                                                                <li>TLS</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Inband-Security-Id for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>instance_ip</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.6.0)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.</div>
                                                    <div>It is meaningful only when having set <code>mas_proxy_call</code> to <code>true</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>interval</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Time interval between two successive probes. Must be greater than the value of Response Time-out.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>20940</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ipaddress</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Set of IP addresses expected in the monitoring response from the DNS server, if the record type is A or AAAA. Applicable to <code>DNS</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>iptunnel</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Send the monitoring probe to the service through an IP tunnel. A destination IP address must be specified.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>kcdaccount</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>KCD Account used by <code>MSSQL</code> monitor.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 32</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>lasversion</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Version number of the Citrix Advanced Access Control Logon Agent. Required by the <code>CITRIX-AAC-LAS</code> monitor.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>logonpointname</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the logon point that is configured for the Citrix Access Gateway Advanced Access Control software. Required if you want to monitor the associated login page or Logon Agent. Applicable to <code>CITRIX-AAC-LAS</code> and <code>CITRIX-AAC-LOGINPAGE</code> monitors.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>lrtm</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Calculate the least response times for bound services. If this parameter is not enabled, the appliance does not learn the response times of the bound services. Also used for LRTM load balancing.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mas_proxy_call</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                        <br/><div style="font-size: small; color: darkgreen">(added in 2.6.0)</div>                </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.</div>
                                                    <div>{&#x27;When true you must also define the following options&#x27;: &#x27;<em>nitro_auth_token</em>, <em>instance_ip</em>.&#x27;}</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>maxforwards</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum number of hops that the SIP request used for monitoring can traverse to reach the server. Applicable only to monitors of type <code>SIP-UDP</code>.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>255</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>metrictable</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Metric table to which to bind metrics.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 99</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>monitorname</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name for the monitor. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore, hash <code>#</code>, period <code>.</code>, space <code> </code>, colon <code>:</code>, at <code>@</code>, equals <code>=</code>, and hyphen <code>-</code> characters.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mssqlprotocolversion</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>70</li>
                                                                                                                                                                                                <li>2000</li>
                                                                                                                                                                                                <li>2000SP1</li>
                                                                                                                                                                                                <li>2005</li>
                                                                                                                                                                                                <li>2008</li>
                                                                                                                                                                                                <li>2008R2</li>
                                                                                                                                                                                                <li>2012</li>
                                                                                                                                                                                                <li>2014</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Version of MSSQL server that is to be monitored.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>netprofile</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the network profile.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 127</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nitro_auth_token</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.6.0)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The authentication token provided by a login operation.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: m, a, s, _, a, u, t, h, _, t, o, k, e, n</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nitro_pass</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The password with which to authenticate to the netscaler node.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: m, a, s, _, p, a, s, s</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nitro_protocol</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>http</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>https</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Which protocol to use when accessing the nitro API objects.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nitro_timeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">310</div>
                                    </td>
                                                                <td>
                                                                        <div>Time in seconds until a timeout error is thrown when establishing a new session with Netscaler</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nitro_user</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The username with which to authenticate to the netscaler node.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: m, a, s, _, u, s, e, r</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nsip</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The ip address of the netscaler appliance where the nitro API calls will be made.</div>
                                                    <div>The port can be specified with the colon (:). E.g. 192.168.1.1:555.</div>
                                                                                        <div style="font-size: small; color: darkgreen"><br/>aliases: m, a, s, _, i, p</div>
                                    </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>oraclesid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the service identifier that is used to connect to the Oracle database during authentication.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>originhost</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Origin-Host value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>originrealm</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Origin-Realm value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>password</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Password that is required for logging on to the <code>RADIUS</code>, <code>NNTP</code>, <code>FTP</code>, <code>FTP-EXTENDED</code>, <code>MYSQL</code>, <code>MSSQL</code>, <code>POP3</code>, <code>CITRIX-AG</code>, <code>CITRIX-XD-DDC</code>, <code>CITRIX-WI-EXTENDED</code>, <code>CITRIX-XNC-ECV</code> or <code>CITRIX-XDM</code> server. Used in conjunction with the user name specified for the <code>username</code> parameter.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>productname</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Product-Name value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>query</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Domain name to resolve as part of monitoring the DNS service (for example, <code>example.com</code>).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>querytype</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>Address</li>
                                                                                                                                                                                                <li>Zone</li>
                                                                                                                                                                                                <li>AAAA</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Type of DNS record for which to send monitoring queries. Set to <code>Address</code> for querying A records, <code>AAAA</code> for querying AAAA records, and <code>Zone</code> for querying the SOA record.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>radaccountsession</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Account Session ID to be used in Account Request Packet. Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>radaccounttype</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Account Type to be used in Account Request Packet. Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div>
                                                    <div>Minimum value = 0</div>
                                                    <div>Maximum value = 15</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>radapn</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Called Station Id to be used in Account Request Packet. Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>radframedip</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Source ip with which the packet will go out . Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>radkey</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Authentication key (shared secret text string) for RADIUS clients and servers to exchange. Applicable to monitors of type <code>RADIUS</code> and <code>RADIUS_ACCOUNTING</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>radmsisdn</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Calling Stations Id to be used in Account Request Packet. Applicable to monitors of type <code>RADIUS_ACCOUNTING</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>radnasid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>NAS-Identifier to send in the Access-Request packet. Applicable to monitors of type <code>RADIUS</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>radnasip</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Network Access Server (NAS) IP address to use as the source IP address when monitoring a RADIUS server. Applicable to monitors of type <code>RADIUS</code> and <code>RADIUS_ACCOUNTING</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>recv</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>String expected from the server for the service to be marked as UP. Applicable to <code>TCP-ECV</code>, <code>HTTP-ECV</code>, and <code>UDP-ECV</code> monitors.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>respcode</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Response codes for which to mark the service as UP. For any other response code, the action performed depends on the monitor type. <code>HTTP</code> monitors and <code>RADIUS</code> monitors mark the service as <code>DOWN</code>, while <code>HTTP-INLINE</code> monitors perform the action indicated by the Action parameter.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>resptimeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Amount of time for which the appliance must wait before it marks a probe as FAILED. Must be less than the value specified for the Interval parameter.</div>
                                                    <div>Note: For <code>UDP-ECV</code> monitors for which a receive string is not configured, response timeout does not apply. For <code>UDP-ECV</code> monitors with no receive string, probe failure is indicated by an ICMP port unreachable error received from the service.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>20939</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>resptimeoutthresh</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Response time threshold, specified as a percentage of the Response Time-out parameter. If the response to a monitor probe has not arrived when the threshold is reached, the appliance generates an SNMP trap called monRespTimeoutAboveThresh. After the response time returns to a value below the threshold, the appliance generates a monRespTimeoutBelowThresh SNMP trap. For the traps to be generated, the &quot;MONITOR-RTO-THRESHOLD&quot; alarm must also be enabled.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>100</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>retries</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum number of probes to send to establish the state of a service for which a monitoring probe failed.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>127</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>reverse</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Mark a service as DOWN, instead of UP, when probe criteria are satisfied, and as UP instead of DOWN when probe criteria are not satisfied.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>rtsprequest</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>RTSP request to send to the server (for example, <code>&quot;OPTIONS *&quot;</code>).</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>save_config</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li><div style="color: blue"><b>yes</b>&nbsp;&larr;</div></li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>If true the module will save the configuration on the netscaler node if it makes any changes.</div>
                                                    <div>The module will not save the configuration on the netscaler node if it made no changes.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>scriptargs</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>String of arguments for the script. The string is copied verbatim into the request.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>scriptname</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Path and name of the script to execute. The script must be available on the NetScaler appliance, in the /nsconfig/monitors/ directory.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>secondarypassword</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Secondary password that users might have to provide to log on to the Access Gateway server. Applicable to <code>CITRIX-AG</code> monitors.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>secure</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Use a secure SSL connection when monitoring a service. Applicable only to TCP based monitors. The secure option cannot be used with a <code>CITRIX-AG</code> monitor, because a CITRIX-AG monitor uses a secure connection by default.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>send</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>String to send to the service. Applicable to <code>TCP-ECV</code>, <code>HTTP-ECV</code>, and <code>UDP-ECV</code> monitors.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sipmethod</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>OPTIONS</li>
                                                                                                                                                                                                <li>INVITE</li>
                                                                                                                                                                                                <li>REGISTER</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>SIP method to use for the query. Applicable only to monitors of type <code>SIP-UDP</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sipreguri</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>SIP user to be registered. Applicable only if the monitor is of type <code>SIP-UDP</code> and the SIP Method parameter is set to <code>REGISTER</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sipuri</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>SIP URI string to send to the service (for example, <code>sip:sip.test</code>). Applicable only to monitors of type <code>SIP-UDP</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sitepath</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>URL of the logon page. For monitors of type <code>CITRIX-WEB-INTERFACE</code>, to monitor a dynamic page under the site path, terminate the site path with a slash <code>/</code>. Applicable to <code>CITRIX-WEB-INTERFACE</code>, <code>CITRIX-WI-EXTENDED</code> and <code>CITRIX-XDM</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>snmpcommunity</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Community name for <code>SNMP</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>Snmpoid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>SNMP OID for <code>SNMP</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>snmpthreshold</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Threshold for <code>SNMP</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>snmpversion</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>V1</li>
                                                                                                                                                                                                <li>V2</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>SNMP version to be used for <code>SNMP</code> monitors.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sqlquery</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>SQL query for a <code>MYSQL-ECV</code> or <code>MSSQL-ECV</code> monitor. Sent to the database server after the server authenticates the connection.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>state</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                                    <b>Default:</b><br/><div style="color: blue">present</div>
                                    </td>
                                                                <td>
                                                                        <div>State of the monitor. The <code>disabled</code> setting disables not only the monitor being configured, but all monitors of the same type, until the parameter is set to <code>enabled</code>. If the monitor is bound to a service, the state of the monitor is not taken into account when the state of the service is determined.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>storedb</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Store the database list populated with the responses to monitor probes. Used in database specific load balancing if <code>MSSQL-ECV</code>/<code>MYSQL-ECV</code> monitor is configured.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>storefrontacctservice</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enable/Disable probing for Account Service. Applicable only to Store Front monitors. For multi-tenancy configuration users my skip account service.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>storefrontcheckbackendservices</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>This option will enable monitoring of services running on storefront server. Storefront services are monitored by probing to a Windows service that runs on the Storefront server and exposes details of which storefront services are running.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>storename</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Store Name. For monitors of type <code>STOREFRONT</code>, <code>storename</code> is an optional argument defining storefront service store name. Applicable to <code>STOREFRONT</code> monitors.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>successretries</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Number of consecutive successful probes required to transition a service&#x27;s state from DOWN to UP.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>32</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>supportedvendorids</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of Supported-Vendor-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum eight of these AVPs are supported in a monitoring message.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>4294967295</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tos</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Probe the service by encoding the destination IP address in the IP TOS (6) bits.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tosid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The TOS ID of the specified destination IP. Applicable only when the TOS parameter is set.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>63</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>transparent</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The monitor is bound to a transparent device such as a firewall or router. The state of a transparent device depends on the responsiveness of the services behind it. If a transparent device is being monitored, a destination IP address must be specified. The probe is sent to the specified IP address by using the MAC address of the transparent device.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>trofscode</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Code expected when the server is under maintenance.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>trofsstring</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>String expected from the server for the service to be marked as trofs. Applicable to HTTP-ECV/TCP-ECV monitors.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>type</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>PING</li>
                                                                                                                                                                                                <li>TCP</li>
                                                                                                                                                                                                <li>HTTP</li>
                                                                                                                                                                                                <li>TCP-ECV</li>
                                                                                                                                                                                                <li>HTTP-ECV</li>
                                                                                                                                                                                                <li>UDP-ECV</li>
                                                                                                                                                                                                <li>DNS</li>
                                                                                                                                                                                                <li>FTP</li>
                                                                                                                                                                                                <li>LDNS-PING</li>
                                                                                                                                                                                                <li>LDNS-TCP</li>
                                                                                                                                                                                                <li>LDNS-DNS</li>
                                                                                                                                                                                                <li>RADIUS</li>
                                                                                                                                                                                                <li>USER</li>
                                                                                                                                                                                                <li>HTTP-INLINE</li>
                                                                                                                                                                                                <li>SIP-UDP</li>
                                                                                                                                                                                                <li>SIP-TCP</li>
                                                                                                                                                                                                <li>LOAD</li>
                                                                                                                                                                                                <li>FTP-EXTENDED</li>
                                                                                                                                                                                                <li>SMTP</li>
                                                                                                                                                                                                <li>SNMP</li>
                                                                                                                                                                                                <li>NNTP</li>
                                                                                                                                                                                                <li>MYSQL</li>
                                                                                                                                                                                                <li>MYSQL-ECV</li>
                                                                                                                                                                                                <li>MSSQL-ECV</li>
                                                                                                                                                                                                <li>ORACLE-ECV</li>
                                                                                                                                                                                                <li>LDAP</li>
                                                                                                                                                                                                <li>POP3</li>
                                                                                                                                                                                                <li>CITRIX-XML-SERVICE</li>
                                                                                                                                                                                                <li>CITRIX-WEB-INTERFACE</li>
                                                                                                                                                                                                <li>DNS-TCP</li>
                                                                                                                                                                                                <li>RTSP</li>
                                                                                                                                                                                                <li>ARP</li>
                                                                                                                                                                                                <li>CITRIX-AG</li>
                                                                                                                                                                                                <li>CITRIX-AAC-LOGINPAGE</li>
                                                                                                                                                                                                <li>CITRIX-AAC-LAS</li>
                                                                                                                                                                                                <li>CITRIX-XD-DDC</li>
                                                                                                                                                                                                <li>ND6</li>
                                                                                                                                                                                                <li>CITRIX-WI-EXTENDED</li>
                                                                                                                                                                                                <li>DIAMETER</li>
                                                                                                                                                                                                <li>RADIUS_ACCOUNTING</li>
                                                                                                                                                                                                <li>STOREFRONT</li>
                                                                                                                                                                                                <li>APPC</li>
                                                                                                                                                                                                <li>SMPP</li>
                                                                                                                                                                                                <li>CITRIX-XNC-ECV</li>
                                                                                                                                                                                                <li>CITRIX-XDM</li>
                                                                                                                                                                                                <li>CITRIX-STA-SERVICE</li>
                                                                                                                                                                                                <li>CITRIX-STA-SERVICE-NHOP</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Type of monitor that you want to create.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>units1</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SEC</li>
                                                                                                                                                                                                <li>MSEC</li>
                                                                                                                                                                                                <li>MIN</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Unit of measurement for the Deviation parameter. Cannot be changed after the monitor is created.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>units2</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SEC</li>
                                                                                                                                                                                                <li>MSEC</li>
                                                                                                                                                                                                <li>MIN</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Unit of measurement for the Down Time parameter. Cannot be changed after the monitor is created.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>units3</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SEC</li>
                                                                                                                                                                                                <li>MSEC</li>
                                                                                                                                                                                                <li>MIN</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>monitor interval units.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>units4</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>SEC</li>
                                                                                                                                                                                                <li>MSEC</li>
                                                                                                                                                                                                <li>MIN</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>monitor response timeout units.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>username</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>User name with which to probe the <code>RADIUS</code>, <code>NNTP</code>, <code>FTP</code>, <code>FTP-EXTENDED</code>, <code>MYSQL</code>, <code>MSSQL</code>, <code>POP3</code>, <code>CITRIX-AG</code>, <code>CITRIX-XD-DDC</code>, <code>CITRIX-WI-EXTENDED</code>, <code>CITRIX-XNC</code> or <code>CITRIX-XDM</code> server.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>validate_certs</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                                <td>
                                                                        <div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>validatecred</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Validate the credentials of the Xen Desktop DDC server user. Applicable to monitors of type <code>CITRIX-XD-DDC</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>vendorid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Vendor-Id value for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>vendorspecificacctapplicationids</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of Vendor-Specific-Acct-Application-Id attribute value pairs (AVPs) to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>4294967295</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>vendorspecificauthapplicationids</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of Vendor-Specific-Auth-Application-Id attribute value pairs (AVPs) for the Capabilities-Exchange-Request (CER) message to use for monitoring Diameter servers. A maximum of eight of these AVPs are supported in a monitoring message. The specified value is combined with the value of vendorSpecificVendorId to obtain the Vendor-Specific-Application-Id AVP in the CER monitoring message.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>4294967295</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>vendorspecificvendorid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Vendor-Id to use in the Vendor-Specific-Application-Id grouped attribute-value pair (AVP) in the monitoring CER message. To specify Auth-Application-Id or Acct-Application-Id in Vendor-Specific-Application-Id, use vendorSpecificAuthApplicationIds or vendorSpecificAcctApplicationIds, respectively. Only one Vendor-Id is supported for all the Vendor-Specific-Application-Id AVPs in a CER monitoring message.</div>
                                                    <div>Minimum value = 1</div>
                                                                                </td>
            </tr>
                        </table>
    <br/>


Notes
-----

.. note::
    - For more information on using Ansible to manage Citrix NetScaler Network devices see https://www.ansible.com/ansible-netscaler.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Set lb monitor
      local_action:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no


        module: citrix_adc_lb_monitor
        state: present

        monitorname: monitor_1
        type: HTTP-INLINE
        action: DOWN
        respcode: ['400']




Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
                    <tr>
                                <td colspan="1">
                    <b>diff</b>
                    <br/><div style="font-size: small; color: red">dict</div>
                                    </td>
                <td>failure</td>
                <td>
                                            <div>List of differences between the actual configured object and the configuration specified in the module</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;targetlbvserver&#x27;: &#x27;difference. ours: (str) server1 other: (str) server2&#x27;}</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>loglines</b>
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>list of logged messages by the module</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[&#x27;message 1&#x27;, &#x27;message 2&#x27;]</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>msg</b>
                    <br/><div style="font-size: small; color: red">str</div>
                                    </td>
                <td>failure</td>
                <td>
                                            <div>Message detailing the failure reason</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Action does not exist</div>
                                    </td>
            </tr>
                        </table>
    <br/><br/>


Status
------



This module is flagged as **preview** which means that it is not guaranteed to have a backwards compatible interface.



Maintenance
-----------

This module is flagged as **community** which means that it is maintained by the Ansible Community. See :ref:`Module Maintenance & Support <modules_support>` for more info.

For a list of other modules that are also maintained by the Ansible Community, see :ref:`here <community_supported>`.





Author
~~~~~~

- George Nikolopoulos (@giorgos-nikolopoulos)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/citrix_adc_lb_monitor.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
