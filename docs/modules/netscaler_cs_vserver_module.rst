.. _netscaler_cs_vserver:


netscaler_cs_vserver - Manage content switching vserver
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4.0


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage content switching vserver
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
        <td><div>Enable logging appflow flow information.</div>        </td></tr>
                <tr><td>authentication<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Authenticate users who request a connection to the content switching virtual server.</div>        </td></tr>
                <tr><td>authenticationhost<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>FQDN of the authentication virtual server. The service type of the virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div><div>Minimum length = 3</div><div>Maximum length = 252</div>        </td></tr>
                <tr><td>authn401<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Enable HTTP 401-response based authentication.</div>        </td></tr>
                <tr><td>authnprofile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the authentication profile to be used when authentication is turned on.</div>        </td></tr>
                <tr><td>authnvsname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of authentication virtual server that authenticates the incoming user requests to this content switching virtual server. .</div><div>Minimum length = 1</div><div>Maximum length = 252</div>        </td></tr>
                <tr><td>backupip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>backupvserver<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the backup virtual server that you are configuring. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore <code>_</code>, hash <code>#</code>, period <code>.</code>, space <code> </code>, colon <code>:</code>, at sign <code>@</code>, equal sign <code>=</code>, and hyphen <code>-</code> characters. Can be changed after the backup virtual server is created. You can assign a different backup virtual server or rename the existing virtual server.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>cacheable<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Use this option to specify whether a virtual server, used for load balancing or content switching, routes requests to the cache redirection virtual server before sending it to the configured servers.</div>        </td></tr>
                <tr><td>casesensitive<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Consider case in URLs (for policies that use URLs instead of RULES). For example, with the <code>on</code> setting, the URLs /a/1.html and /A/1.HTML are treated differently and can have different targets (set by content switching policies). With the <code>off</code> setting, /a/1.html and /A/1.HTML are switched to the same target.</div>        </td></tr>
                <tr><td>clttimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Idle time, in seconds, after which the client connection is terminated. The default values are:</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>31536000</code></div>        </td></tr>
                <tr><td>comment<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Information about this virtual server.</div>        </td></tr>
                <tr><td>cookiedomain<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>cookietimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>1440</code></div>        </td></tr>
                <tr><td>dbprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the DB profile.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>disabled<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>no</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>When set to <code>yes</code> the cs vserver will be disabled.</div><div>When set to <code>no</code> the cs vserver will be enabled.</div><div>Note that due to limitations of the underlying NITRO API a <code>disabled</code> state change alone does not cause the module result to report a changed status.</div>        </td></tr>
                <tr><td>disableprimaryondown<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Continue forwarding the traffic to backup virtual server even after the primary server comes UP from the DOWN state.</div>        </td></tr>
                <tr><td>dnsprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the DNS profile to be associated with the VServer. DNS profile properties will applied to the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>domainname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Domain name for which to change the time to live (TTL) and/or backup service IP address.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>downstateflush<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.</div>        </td></tr>
                <tr><td>httpprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the HTTP profile containing HTTP configuration settings for the virtual server. The service type of the virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>icmpvsrresponse<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>PASSIVE</li><li>ACTIVE</li></ul></td>
        <td><div>Can be active or passive.</div>        </td></tr>
                <tr><td>insertvserveripport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>OFF</li><li>VIPADDR</li><li>V6TOV4MAPPING</li></ul></td>
        <td><div>Insert the virtual server's VIP address and port number in the request header. Available values function as follows:</div><div><code>VIPADDR</code> - Header contains the vserver's IP address and port number without any translation.</div><div><code>OFF</code> - The virtual IP and port header insertion option is disabled.</div><div><code>V6TOV4MAPPING</code> - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns ip6 command.</div>        </td></tr>
                <tr><td>ipmask<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, <code>255.255.240.0</code> or <code>0.0.255.255</code>). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.</div>        </td></tr>
                <tr><td>ippattern<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern. Mutually exclusive with the IP Address parameter.</div><div>For example, if the IP pattern assigned to the virtual server is <code>198.51.100.0</code> and the IP mask is <code>255.255.240.0</code> (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254. You can also use a pattern such as <code>0.0.2.2</code> and a mask such as <code>0.0.255.255</code> (a reverse mask).</div><div>If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if the virtual servers, <code>vs1</code> and <code>vs2</code>, have the same IP pattern, <code>0.0.100.128</code>, but different IP masks of <code>0.0.255.255</code> and <code>0.0.224.255</code>, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of <code>vs1</code>. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.</div>        </td></tr>
                <tr><td>ipv46<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP address of the content switching virtual server.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>l2conn<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Use L2 Parameters to identify a connection.</div>        </td></tr>
                <tr><td>listenpolicy<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>String specifying the listen policy for the content switching virtual server. Can be either the name of an existing expression or an in-line expression.</div>        </td></tr>
                <tr><td>mssqlserverversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>70</li><li>2000</li><li>2000SP1</li><li>2005</li><li>2008</li><li>2008R2</li><li>2012</li><li>2014</li></ul></td>
        <td><div>The version of the MSSQL server.</div>        </td></tr>
                <tr><td>mysqlcharacterset<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The character set returned by the mysql vserver.</div>        </td></tr>
                <tr><td>mysqlprotocolversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The protocol version returned by the mysql vserver.</div>        </td></tr>
                <tr><td>mysqlservercapabilities<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The server capabilities returned by the mysql vserver.</div>        </td></tr>
                <tr><td>mysqlserverversion<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The server version string returned by the mysql vserver.</div><div>Minimum length = 1</div><div>Maximum length = 31</div>        </td></tr>
                <tr><td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the content switching virtual server. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore <code>_</code>, hash <code>#</code>, period <code>.</code>, space, colon <code>:</code>, at sign <code>@</code>, equal sign <code>=</code>, and hyphen <code>-</code> characters.</div><div>Cannot be changed after the CS virtual server is created.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>netprofile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the network profile.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
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
        <td><div>Oracle server version.</div>        </td></tr>
                <tr><td>port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Port number for content switching virtual server.</div><div>Minimum value = 1</div><div>Range <code>1</code> - <code>65535</code></div><div>* in CLI is represented as 65535 in NITRO API</div>        </td></tr>
                <tr><td>precedence<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>RULE</li><li>URL</li></ul></td>
        <td><div>Type of precedence to use for both RULE-based and URL-based policies on the content switching virtual server. With the default <code>RULE</code> setting, incoming requests are evaluated against the rule-based content switching policies. If none of the rules match, the URL in the request is evaluated against the URL-based content switching policies.</div>        </td></tr>
                <tr><td>push<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Process traffic with the push virtual server that is bound to this content switching virtual server (specified by the Push VServer parameter). The service type of the push virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div>        </td></tr>
                <tr><td>pushlabel<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Expression for extracting the label from the response received from server. This string can be either an existing rule name or an inline expression. The service type of the virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div>        </td></tr>
                <tr><td>pushmulticlients<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.</div>        </td></tr>
                <tr><td>pushvserver<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the load balancing virtual server, of type <code>PUSH</code> or <code>SSL_PUSH</code>, to which the server pushes updates received on the client-facing load balancing virtual server.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>range<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Number of consecutive IP addresses, starting with the address specified by the IP Address parameter, to include in a range of addresses assigned to this virtual server.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>254</code></div>        </td></tr>
                <tr><td>redirectportrewrite<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>State of port rewrite while performing HTTP redirect.</div>        </td></tr>
                <tr><td>redirecturl<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>URL to which traffic is redirected if the virtual server becomes unavailable. The service type of the virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div><div>Caution: Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>rhistate<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>PASSIVE</li><li>ACTIVE</li></ul></td>
        <td><div>A host route is injected according to the setting on the virtual servers</div><div>* If set to <code>PASSIVE</code> on all the virtual servers that share the IP address, the appliance always injects the hostroute.</div><div>* If set to <code>ACTIVE</code> on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.</div><div>* If set to <code>ACTIVE</code> on some virtual servers and <code>PASSIVE</code> on the others, the appliance, injects even if one virtual server set to <code>ACTIVE</code> is UP.</div>        </td></tr>
                <tr><td>rtspnat<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Enable network address translation (NAT) for real-time streaming protocol (RTSP) connections.</div>        </td></tr>
                <tr><td>save_config<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If true the module will save the configuration on the netscaler node if it makes any changes.</div><div>The module will not save the configuration on the netscaler node if it made no changes.</div>        </td></tr>
                <tr><td>servicetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>HTTP</li><li>SSL</li><li>TCP</li><li>FTP</li><li>RTSP</li><li>SSL_TCP</li><li>UDP</li><li>DNS</li><li>SIP_UDP</li><li>SIP_TCP</li><li>SIP_SSL</li><li>ANY</li><li>RADIUS</li><li>RDP</li><li>MYSQL</li><li>MSSQL</li><li>DIAMETER</li><li>SSL_DIAMETER</li><li>DNS_TCP</li><li>ORACLE</li><li>SMPP</li></ul></td>
        <td><div>Protocol used by the virtual server.</div>        </td></tr>
                <tr><td>sitedomainttl<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>.</div><div>Minimum value = <code>1</code></div>        </td></tr>
                <tr><td>sobackupaction<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>DROP</li><li>ACCEPT</li><li>REDIRECT</li></ul></td>
        <td><div>Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.</div>        </td></tr>
                <tr><td>somethod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>CONNECTION</li><li>DYNAMICCONNECTION</li><li>BANDWIDTH</li><li>HEALTH</li><li>NONE</li></ul></td>
        <td><div>Type of spillover used to divert traffic to the backup virtual server when the primary virtual server reaches the spillover threshold. Connection spillover is based on the number of connections. Bandwidth spillover is based on the total Kbps of incoming and outgoing traffic.</div>        </td></tr>
                <tr><td>sopersistence<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Maintain source-IP based persistence on primary and backup virtual servers.</div>        </td></tr>
                <tr><td>sopersistencetimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time-out value, in minutes, for spillover persistence.</div><div>Minimum value = <code>2</code></div><div>Maximum value = <code>1440</code></div>        </td></tr>
                <tr><td>sothreshold<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Depending on the spillover method, the maximum number of connections or the maximum total bandwidth (Kbps) that a virtual server can handle before spillover occurs.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>4294967287</code></div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>The state of the resource being configured by the module on the netscaler node.</div><div>When present the resource will be created if needed and configured according to the module's parameters.</div><div>When absent the resource will be deleted from the netscaler node.</div>        </td></tr>
                <tr><td>stateupdate<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Enable state updates for a specific content switching virtual server. By default, the Content Switching virtual server is always UP, regardless of the state of the Load Balancing virtual servers bound to it. This parameter interacts with the global setting as follows:</div><div>Global Level | Vserver Level | Result</div><div>ENABLED ENABLED ENABLED</div><div>ENABLED DISABLED ENABLED</div><div>DISABLED ENABLED ENABLED</div><div>DISABLED DISABLED DISABLED</div><div>If you want to enable state updates for only some content switching virtual servers, be sure to disable the state update parameter.</div>        </td></tr>
                <tr><td>targettype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>GSLB</li></ul></td>
        <td><div>Virtual server target type.</div>        </td></tr>
                <tr><td>tcpprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the TCP profile containing TCP configuration settings for the virtual server.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>td<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.</div><div>Minimum value = 0</div><div>Maximum value = 4094</div>        </td></tr>
                <tr><td>ttl<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>.</div><div>Minimum value = <code>1</code></div>        </td></tr>
                <tr><td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td></td>
        <td><div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>        </td></tr>
                <tr><td>vipheader<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of virtual server IP and port header, for use with the VServer IP Port Insertion parameter.</div><div>Minimum length = 1</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    # policy_1 must have been already created with the netscaler_cs_policy module
    # lbvserver_1 must have been already created with the netscaler_lb_vserver module
    
    - name: Setup content switching vserver
      delegate_to: localhost
      netscaler_cs_vserver:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
    
        state: present
    
        name: cs_vserver_1
        ipv46: 192.168.1.1
        port: 80
        servicetype: HTTP
    
        policybindings:
          - policyname: policy_1
            targetlbvserver: lbvserver_1

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
        <td align=center> {'clttimeout': 'difference. ours: (float) 100.0 other: (float) 60.0'} </td>
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

This module is community maintained without core committer oversight.

For more information on what this means please read :doc:`modules_support`


For help in developing on modules, should you be so inclined, please read :doc:`community`, :doc:`dev_guide/developing_test_pr` and :doc:`dev_guide/developing_modules`.