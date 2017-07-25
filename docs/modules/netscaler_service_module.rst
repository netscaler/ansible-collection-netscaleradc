.. _netscaler_service:


netscaler_service - Manage service configuration in Netscaler
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4.0


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage service configuration in Netscaler.
* This module allows the creation, deletion and modification of Netscaler services.
* This module is intended to run either on the ansible  control node or a bastion (jumpserver) with access to the actual netscaler instance.
* This module supports check mode.


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
                <tr><td>accessdown<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Use Layer 2 mode to bridge the packets sent to this service if it is marked as DOWN. If the service is DOWN, and this parameter is disabled, the packets are dropped.</div>        </td></tr>
                <tr><td>appflowlog<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>ENABLED</td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Enable logging of AppFlow information.</div>        </td></tr>
                <tr><td>cacheable<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Use the transparent cache redirection virtual server to forward requests to the cache server.</div><div>Note: Do not specify this parameter if you set the Cache Type parameter.</div>        </td></tr>
                <tr><td>cachetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>TRANSPARENT</li><li>REVERSE</li><li>FORWARD</li></ul></td>
        <td><div>Cache type supported by the cache server.</div>        </td></tr>
                <tr><td>cip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Before forwarding a request to the service, insert an HTTP header with the client's IPv4 or IPv6 address as its value. Used if the server needs the client's IP address for security, accounting, or other purposes, and setting the Use Source IP parameter is not a viable option.</div>        </td></tr>
                <tr><td>cipheader<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If you set the Client IP parameter, and you do not specify a name for the header, the appliance uses the header name specified for the global Client IP Header parameter (the cipHeader parameter in the set ns param CLI command or the Client IP Header parameter in the Configure HTTP Parameters dialog box at System &gt; Settings &gt; Change HTTP parameters). If the global Client IP Header parameter is not specified, the appliance inserts a header with the name "client-ip.".</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>cka<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Enable client keep-alive for the service.</div>        </td></tr>
                <tr><td>cleartextport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Port to which clear text data must be sent after the appliance decrypts incoming SSL traffic. Applicable to transparent SSL services.</div><div>Minimum value = 1</div>        </td></tr>
                <tr><td>clttimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time, in seconds, after which to terminate an idle client connection.</div><div>Minimum value = 0</div><div>Maximum value = 31536000</div>        </td></tr>
                <tr><td>cmp<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Enable compression for the service.</div>        </td></tr>
                <tr><td>comment<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Any information about the service.</div>        </td></tr>
                <tr><td>customserverid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>None</td>
        <td></td>
        <td><div>Unique identifier for the service. Used when the persistency type for the virtual server is set to Custom Server ID.</div>        </td></tr>
                <tr><td>dnsprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the DNS profile to be associated with the service. DNS profile properties will applied to the transactions processed by a service. This parameter is valid only for ADNS and ADNS-TCP services.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>downstateflush<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>ENABLED</td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Flush all active transactions associated with a service whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.</div>        </td></tr>
                <tr><td>graceful<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Shut down gracefully, not accepting any new connections, and disabling the service when all of its connections are closed.</div>        </td></tr>
                <tr><td>hashid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>A numerical identifier that can be used by hash based load balancing methods. Must be unique for each service.</div><div>Minimum value = 1</div>        </td></tr>
                <tr><td>healthmonitor<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td></td>
        <td><div>Monitor the health of this service</div>        </td></tr>
                <tr><td>httpprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the HTTP profile that contains HTTP configuration settings for the service.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>ip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP to assign to the service.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>ipaddress<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The new IP address of the service.</div>        </td></tr>
                <tr><td>maxbandwidth<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum bandwidth, in Kbps, allocated to the service.</div><div>Minimum value = 0</div><div>Maximum value = 4294967287</div>        </td></tr>
                <tr><td>maxclient<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum number of simultaneous open connections to the service.</div><div>Minimum value = 0</div><div>Maximum value = 4294967294</div>        </td></tr>
                <tr><td>maxreq<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum number of requests that can be sent on a persistent connection to the service.</div><div>Note: Connection requests beyond this value are rejected.</div><div>Minimum value = 0</div><div>Maximum value = 65535</div>        </td></tr>
                <tr><td rowspan="2">monitor_bindings<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td><td></td>
    <td> <div>A list of load balancing monitors to bind to this service.</div><div>Each monitor entry is a dictionary which may contain the following options.</div><div>Note that if not using the built in monitors they must first be setup.</div>    </tr>
    <tr>
    <td colspan="5">
    <table border=1 cellpadding=4>
    <caption><b>Dictionary object monitor_bindings</b></caption>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
                    <tr><td>dup_state<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
                <td><div>State of the monitor.</div><div>The state setting for a monitor of a given type affects all monitors of that type.</div><div>For example, if an HTTP monitor is enabled, all HTTP monitors on the appliance are (or remain) enabled.</div><div>If an HTTP monitor is disabled, all HTTP monitors on the appliance are disabled.</div>        </td></tr>
                    <tr><td>monitorname<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Name of the monitor.</div>        </td></tr>
                    <tr><td>weight<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Weight to assign to the binding between the monitor and service.</div>        </td></tr>
                    <tr><td>dup_weight<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Weight to assign to the binding between the monitor and service.</div>        </td></tr>
        </table>
    </td>
    </tr>
        </td></tr>
                <tr><td>monthreshold<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.</div><div>Minimum value = 0</div><div>Maximum value = 65535</div>        </td></tr>
                <tr><td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the service. Must begin with an ASCII alphabetic or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore <code>_</code>, hash <code>#</code>, period <code>.</code>, space <code> </code>, colon <code>:</code>, at <code>@</code>, equals <code>=</code>, and hyphen <code>-</code> characters. Cannot be changed after the service has been created.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>netprofile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Network profile to use for the service.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
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
                <tr><td>pathmonitor<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Path monitoring for clustering.</div>        </td></tr>
                <tr><td>pathmonitorindv<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Individual Path monitoring decisions.</div>        </td></tr>
                <tr><td>port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Port number of the service.</div><div>Range 1 - 65535</div><div>* in CLI is represented as 65535 in NITRO API</div>        </td></tr>
                <tr><td>processlocal<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>DISABLED</td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>By turning on this option packets destined to a service in a cluster will not under go any steering. Turn this option for single packet request response mode or when the upstream device is performing a proper RSS for connection based distribution.</div>        </td></tr>
                <tr><td>rtspsessionidremap<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Enable RTSP session ID mapping for the service.</div>        </td></tr>
                <tr><td>save_config<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If true the module will save the configuration on the netscaler node if it makes any changes.</div><div>The module will not save the configuration on the netscaler node if it made no changes.</div>        </td></tr>
                <tr><td>sc<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>State of SureConnect for the service.</div>        </td></tr>
                <tr><td>serverid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The identifier for the service. This is used when the persistency type is set to Custom Server ID.</div>        </td></tr>
                <tr><td>servername<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the server that hosts the service.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>servicetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>HTTP</li><li>FTP</li><li>TCP</li><li>UDP</li><li>SSL</li><li>SSL_BRIDGE</li><li>SSL_TCP</li><li>DTLS</li><li>NNTP</li><li>RPCSVR</li><li>DNS</li><li>ADNS</li><li>SNMP</li><li>RTSP</li><li>DHCPRA</li><li>ANY</li><li>SIP_UDP</li><li>SIP_TCP</li><li>SIP_SSL</li><li>DNS_TCP</li><li>ADNS_TCP</li><li>MYSQL</li><li>MSSQL</li><li>ORACLE</li><li>RADIUS</li><li>RADIUSListener</li><li>RDP</li><li>DIAMETER</li><li>SSL_DIAMETER</li><li>TFTP</li><li>SMPP</li><li>PPTP</li><li>GRE</li><li>SYSLOGTCP</li><li>SYSLOGUDP</li><li>FIX</li><li>SSL_FIX</li></ul></td>
        <td><div>Protocol in which data is exchanged with the service.</div>        </td></tr>
                <tr><td>sp<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Enable surge protection for the service.</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>The state of the resource being configured by the module on the netscaler node.</div><div>When present the resource will be created if needed and configured according to the module's parameters.</div><div>When absent the resource will be deleted from the netscaler node.</div>        </td></tr>
                <tr><td>svrtimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time, in seconds, after which to terminate an idle server connection.</div><div>Minimum value = 0</div><div>Maximum value = 31536000</div>        </td></tr>
                <tr><td>tcpb<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Enable TCP buffering for the service.</div>        </td></tr>
                <tr><td>tcpprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the TCP profile that contains TCP configuration settings for the service.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>td<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.</div><div>Minimum value = 0</div><div>Maximum value = 4094</div>        </td></tr>
                <tr><td>useproxyport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.</div><div>Note: This parameter is available only when the Use Source IP (USIP) parameter is set to YES.</div>        </td></tr>
                <tr><td>usip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Use the client's IP address as the source IP address when initiating a connection to the server. When creating a service, if you do not set this parameter, the service inherits the global Use Source IP setting (available in the enable ns mode and disable ns mode CLI commands, or in the System &gt; Settings &gt; Configure modes &gt; Configure Modes dialog box). However, you can override this setting after you create the service.</div>        </td></tr>
                <tr><td>validate_certs<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>yes</td>
        <td></td>
        <td><div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    # Monitor monitor-1 must have been already setup
    
    - name: Setup http service
      gather_facts: False
      delegate_to: localhost
      netscaler_service:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
    
        state: present
    
        name: service-http-1
        servicetype: HTTP
        ipaddress: 10.78.0.1
        port: 80
    
        monitor_bindings:
          - monitor-1

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
        <td> loglines </td>
        <td> list of logged messages by the module </td>
        <td align=center> always </td>
        <td align=center> list </td>
        <td align=center> ['message 1', 'message 2'] </td>
    </tr>
            <tr>
        <td> diff </td>
        <td> A dictionary with a list of differences between the actual configured object and the configuration specified in the module </td>
        <td align=center> failure </td>
        <td align=center> dict </td>
        <td align=center> { 'clttimeout': 'difference. ours: (float) 10.0 other: (float) 20.0' } </td>
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