:source: citrix_adc_cs_vserver.py

:orphan:

.. _citrix_adc_cs_vserver_module:


citrix_adc_cs_vserver - Manage content switching vserver
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Manage content switching vserver
- This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance



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
                    <b>appflowlog</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enable logging appflow flow information.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>authentication</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Authenticate users who request a connection to the content switching virtual server.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>authenticationhost</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>FQDN of the authentication virtual server. The service type of the virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div>
                                                    <div>Minimum length = 3</div>
                                                    <div>Maximum length = 252</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>authn401</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enable HTTP 401-response based authentication.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>authnprofile</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the authentication profile to be used when authentication is turned on.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>authnvsname</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of authentication virtual server that authenticates the incoming user requests to this content switching virtual server. .</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 252</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>backupip</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>backupvserver</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the backup virtual server that you are configuring. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore <code>_</code>, hash <code>#</code>, period <code>.</code>, space <code> </code>, colon <code>:</code>, at sign <code>@</code>, equal sign <code>=</code>, and hyphen <code>-</code> characters. Can be changed after the backup virtual server is created. You can assign a different backup virtual server or rename the existing virtual server.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cacheable</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Use this option to specify whether a virtual server, used for load balancing or content switching, routes requests to the cache redirection virtual server before sending it to the configured servers.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>casesensitive</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Consider case in URLs (for policies that use URLs instead of RULES). For example, with the <code>on</code> setting, the URLs /a/1.html and /A/1.HTML are treated differently and can have different targets (set by content switching policies). With the <code>off</code> setting, /a/1.html and /A/1.HTML are switched to the same target.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>clttimeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Idle time, in seconds, after which the client connection is terminated. The default values are:</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>31536000</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>comment</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Information about this virtual server.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cookiedomain</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>cookietimeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>1440</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>dbprofilename</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the DB profile.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 127</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>disabled</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>When set to <code>yes</code> the cs vserver will be disabled.</div>
                                                    <div>When set to <code>no</code> the cs vserver will be enabled.</div>
                                                    <div>Note that due to limitations of the underlying NITRO API a <code>disabled</code> state change alone does not cause the module result to report a changed status.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>disableprimaryondown</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Continue forwarding the traffic to backup virtual server even after the primary server comes UP from the DOWN state.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>dnsprofilename</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the DNS profile to be associated with the VServer. DNS profile properties will applied to the transactions processed by a VServer. This parameter is valid only for DNS and DNS-TCP VServers.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 127</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>domainname</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Domain name for which to change the time to live (TTL) and/or backup service IP address.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>downstateflush</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Flush all active transactions associated with a virtual server whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>httpprofilename</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the HTTP profile containing HTTP configuration settings for the virtual server. The service type of the virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 127</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>icmpvsrresponse</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>PASSIVE</li>
                                                                                                                                                                                                <li>ACTIVE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Can be active or passive.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>insertvserveripport</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>OFF</li>
                                                                                                                                                                                                <li>VIPADDR</li>
                                                                                                                                                                                                <li>V6TOV4MAPPING</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Insert the virtual server&#x27;s VIP address and port number in the request header. Available values function as follows:</div>
                                                    <div><code>VIPADDR</code> - Header contains the vserver&#x27;s IP address and port number without any translation.</div>
                                                    <div><code>OFF</code> - The virtual IP and port header insertion option is disabled.</div>
                                                    <div><code>V6TOV4MAPPING</code> - Header contains the mapped IPv4 address corresponding to the IPv6 address of the vserver and the port number. An IPv6 address can be mapped to a user-specified IPv4 address using the set ns ip6 command.</div>
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
                    <b>ipmask</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have leading or trailing non-zero octets (for example, <code>255.255.240.0</code> or <code>0.0.255.255</code>). Accordingly, the mask specifies whether the first n bits or the last n bits of the destination IP address in a client request are to be matched with the corresponding bits in the IP pattern. The former is called a forward mask. The latter is called a reverse mask.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ippattern</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>IP address pattern, in dotted decimal notation, for identifying packets to be accepted by the virtual server. The IP Mask parameter specifies which part of the destination IP address is matched against the pattern. Mutually exclusive with the IP Address parameter.</div>
                                                    <div>For example, if the IP pattern assigned to the virtual server is <code>198.51.100.0</code> and the IP mask is <code>255.255.240.0</code> (a forward mask), the first 20 bits in the destination IP addresses are matched with the first 20 bits in the pattern. The virtual server accepts requests with IP addresses that range from 198.51.96.1 to 198.51.111.254. You can also use a pattern such as <code>0.0.2.2</code> and a mask such as <code>0.0.255.255</code> (a reverse mask).</div>
                                                    <div>If a destination IP address matches more than one IP pattern, the pattern with the longest match is selected, and the associated virtual server processes the request. For example, if the virtual servers, <code>vs1</code> and <code>vs2</code>, have the same IP pattern, <code>0.0.100.128</code>, but different IP masks of <code>0.0.255.255</code> and <code>0.0.224.255</code>, a destination IP address of 198.51.100.128 has the longest match with the IP pattern of <code>vs1</code>. If a destination IP address matches two or more virtual servers to the same extent, the request is processed by the virtual server whose port number matches the port number in the request.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ipv46</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>IP address of the content switching virtual server.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>l2conn</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Use L2 Parameters to identify a connection.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>lbvserver</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.5)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The default Load Balancing virtual server.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>listenpolicy</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>String specifying the listen policy for the content switching virtual server. Can be either the name of an existing expression or an in-line expression.</div>
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
                    <b>mssqlserverversion</b>
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
                                                                        <div>The version of the MSSQL server.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mysqlcharacterset</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The character set returned by the mysql vserver.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mysqlprotocolversion</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The protocol version returned by the mysql vserver.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mysqlservercapabilities</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The server capabilities returned by the mysql vserver.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>mysqlserverversion</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The server version string returned by the mysql vserver.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 31</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name for the content switching virtual server. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore <code>_</code>, hash <code>#</code>, period <code>.</code>, space, colon <code>:</code>, at sign <code>@</code>, equal sign <code>=</code>, and hyphen <code>-</code> characters.</div>
                                                    <div>Cannot be changed after the CS virtual server is created.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>netprofile</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The name of the network profile.</div>
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
                    <b>oracleserverversion</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>10G</li>
                                                                                                                                                                                                <li>11G</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Oracle server version.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>port</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Port number for content switching virtual server.</div>
                                                    <div>Minimum value = 1</div>
                                                    <div>Range <code>1</code> - <code>65535</code></div>
                                                    <div>* in CLI is represented as 65535 in NITRO API</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>precedence</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>RULE</li>
                                                                                                                                                                                                <li>URL</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Type of precedence to use for both RULE-based and URL-based policies on the content switching virtual server. With the default <code>RULE</code> setting, incoming requests are evaluated against the rule-based content switching policies. If none of the rules match, the URL in the request is evaluated against the URL-based content switching policies.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>push</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Process traffic with the push virtual server that is bound to this content switching virtual server (specified by the Push VServer parameter). The service type of the push virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>pushlabel</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Expression for extracting the label from the response received from server. This string can be either an existing rule name or an inline expression. The service type of the virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>pushmulticlients</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Allow multiple Web 2.0 connections from the same client to connect to the virtual server and expect updates.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>pushvserver</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the load balancing virtual server, of type <code>PUSH</code> or <code>SSL_PUSH</code>, to which the server pushes updates received on the client-facing load balancing virtual server.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>range</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Number of consecutive IP addresses, starting with the address specified by the IP Address parameter, to include in a range of addresses assigned to this virtual server.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>254</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>redirectportrewrite</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>State of port rewrite while performing HTTP redirect.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>redirecturl</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>URL to which traffic is redirected if the virtual server becomes unavailable. The service type of the virtual server should be either <code>HTTP</code> or <code>SSL</code>.</div>
                                                    <div>Caution: Make sure that the domain in the URL does not match the domain specified for a content switching policy. If it does, requests are continuously redirected to the unavailable virtual server.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>rhistate</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>PASSIVE</li>
                                                                                                                                                                                                <li>ACTIVE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>A host route is injected according to the setting on the virtual servers</div>
                                                    <div>* If set to <code>PASSIVE</code> on all the virtual servers that share the IP address, the appliance always injects the hostroute.</div>
                                                    <div>* If set to <code>ACTIVE</code> on all the virtual servers that share the IP address, the appliance injects even if one virtual server is UP.</div>
                                                    <div>* If set to <code>ACTIVE</code> on some virtual servers and <code>PASSIVE</code> on the others, the appliance, injects even if one virtual server set to <code>ACTIVE</code> is UP.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>rtspnat</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enable network address translation (NAT) for real-time streaming protocol (RTSP) connections.</div>
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
                    <b>servicetype</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>HTTP</li>
                                                                                                                                                                                                <li>SSL</li>
                                                                                                                                                                                                <li>TCP</li>
                                                                                                                                                                                                <li>FTP</li>
                                                                                                                                                                                                <li>RTSP</li>
                                                                                                                                                                                                <li>SSL_TCP</li>
                                                                                                                                                                                                <li>UDP</li>
                                                                                                                                                                                                <li>DNS</li>
                                                                                                                                                                                                <li>SIP_UDP</li>
                                                                                                                                                                                                <li>SIP_TCP</li>
                                                                                                                                                                                                <li>SIP_SSL</li>
                                                                                                                                                                                                <li>ANY</li>
                                                                                                                                                                                                <li>RADIUS</li>
                                                                                                                                                                                                <li>RDP</li>
                                                                                                                                                                                                <li>MYSQL</li>
                                                                                                                                                                                                <li>MSSQL</li>
                                                                                                                                                                                                <li>DIAMETER</li>
                                                                                                                                                                                                <li>SSL_DIAMETER</li>
                                                                                                                                                                                                <li>DNS_TCP</li>
                                                                                                                                                                                                <li>ORACLE</li>
                                                                                                                                                                                                <li>SMPP</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Protocol used by the virtual server.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sitedomainttl</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sobackupaction</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>DROP</li>
                                                                                                                                                                                                <li>ACCEPT</li>
                                                                                                                                                                                                <li>REDIRECT</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Action to be performed if spillover is to take effect, but no backup chain to spillover is usable or exists.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>somethod</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>CONNECTION</li>
                                                                                                                                                                                                <li>DYNAMICCONNECTION</li>
                                                                                                                                                                                                <li>BANDWIDTH</li>
                                                                                                                                                                                                <li>HEALTH</li>
                                                                                                                                                                                                <li>NONE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Type of spillover used to divert traffic to the backup virtual server when the primary virtual server reaches the spillover threshold. Connection spillover is based on the number of connections. Bandwidth spillover is based on the total Kbps of incoming and outgoing traffic.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sopersistence</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Maintain source-IP based persistence on primary and backup virtual servers.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sopersistencetimeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Time-out value, in minutes, for spillover persistence.</div>
                                                    <div>Minimum value = <code>2</code></div>
                                                    <div>Maximum value = <code>1440</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>sothreshold</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Depending on the spillover method, the maximum number of connections or the maximum total bandwidth (Kbps) that a virtual server can handle before spillover occurs.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>4294967287</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ssl_certkey</b>
                                                            <br/><div style="font-size: small; color: darkgreen">(added in 2.5)</div>                </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The name of the ssl certificate that is bound to this service.</div>
                                                    <div>The ssl certificate must already exist.</div>
                                                    <div>Creating the certificate can be done with the <span class='module'>citrix_adc_ssl_certkey</span> module.</div>
                                                    <div>This option is only applicable only when <code>servicetype</code> is <code>SSL</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>state</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>absent</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>The state of the resource being configured by the module on the netscaler node.</div>
                                                    <div>When present the resource will be created if needed and configured according to the module&#x27;s parameters.</div>
                                                    <div>When absent the resource will be deleted from the netscaler node.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>stateupdate</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Enable state updates for a specific content switching virtual server. By default, the Content Switching virtual server is always UP, regardless of the state of the Load Balancing virtual servers bound to it. This parameter interacts with the global setting as follows:</div>
                                                    <div>Global Level | Vserver Level | Result</div>
                                                    <div>enabled enabled enabled</div>
                                                    <div>enabled disabled enabled</div>
                                                    <div>disabled enabled enabled</div>
                                                    <div>disabled disabled disabled</div>
                                                    <div>If you want to enable state updates for only some content switching virtual servers, be sure to disable the state update parameter.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>targettype</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>GSLB</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Virtual server target type.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>tcpprofilename</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the TCP profile containing TCP configuration settings for the virtual server.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 127</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>td</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.</div>
                                                    <div>Minimum value = 0</div>
                                                    <div>Maximum value = 4094</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>ttl</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>.</div>
                                                    <div>Minimum value = <code>1</code></div>
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
                    <b>vipheader</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of virtual server IP and port header, for use with the VServer IP Port Insertion parameter.</div>
                                                    <div>Minimum length = 1</div>
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

    
    # policy_1 must have been already created with the citrix_adc_cs_policy module
    # lbvserver_1 must have been already created with the citrix_adc_lb_vserver module

    - name: Setup content switching vserver
      delegate_to: localhost
      citrix_adc_cs_vserver:
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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;clttimeout&#x27;: &#x27;difference. ours: (float) 100.0 other: (float) 60.0&#x27;}</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/citrix_adc_cs_vserver.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
