.. _netscaler_servicegroup:


netscaler_servicegroup - Manage service group configuration in Netscaler
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4.0


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage service group configuration in Netscaler
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
        <td><div>Enable logging of AppFlow information for the specified service group.</div><div>Default value = ENABLED</div>        </td></tr>
                <tr><td>autoscale<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>DISABLED</li><li>DNS</li><li>POLICY</li></ul></td>
        <td><div>Auto scale option for a servicegroup.</div><div>Default value = DISABLED</div>        </td></tr>
                <tr><td>cacheable<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Use the transparent cache redirection virtual server to forward the request to the cache server.</div><div>Note. Do not set this parameter if you set the Cache Type.</div><div>Default value = NO</div><div>Possible values = YES, NO</div>        </td></tr>
                <tr><td>cachetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>TRANSPARENT</li><li>REVERSE</li><li>FORWARD</li></ul></td>
        <td><div>Cache type supported by the cache server.</div><div>Possible values = TRANSPARENT, REVERSE, FORWARD</div>        </td></tr>
                <tr><td>cip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Insert the Client IP header in requests forwarded to the service.</div><div>Possible values = ENABLED, DISABLED</div>        </td></tr>
                <tr><td>cipheader<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the HTTP header whose value must be set to the IP address of the client. Used with the Client IP parameter. If client IP insertion is enabled, and the client IP header is not specified, the value of Client IP Header parameter or the value set by the set ns config command is used as client's IP header name.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>cka<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Enable client keep-alive for the service group.</div>        </td></tr>
                <tr><td>clttimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time, in seconds, after which to terminate an idle client connection.</div><div>Minimum value = 0</div><div>Maximum value = 31536000</div>        </td></tr>
                <tr><td>cmp<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Enable compression for the specified service.</div>        </td></tr>
                <tr><td>comment<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Any information about the service group.</div>        </td></tr>
                <tr><td>downstateflush<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Flush all active transactions associated with all the services in the service group whose state transitions from UP to DOWN. Do not enable this option for applications that must complete their transactions.</div><div>Default value = ENABLED</div>        </td></tr>
                <tr><td>graceful<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Wait for all existing connections to the service to terminate before shutting down the service.</div><div>Default value = NO</div>        </td></tr>
                <tr><td>healthmonitor<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Monitor the health of this service. Available settings function as follows.</div><div>YES - Send probes to check the health of the service.</div><div>NO - Do not send probes to check the health of the service. With the NO option, the appliance shows the service as UP at all times.</div><div>Default value = YES</div>        </td></tr>
                <tr><td>httpprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the HTTP profile that contains HTTP configuration settings for the service group.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>maxbandwidth<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum bandwidth, in Kbps, allocated for all the services in the service group.</div><div>Minimum value = 0</div><div>Maximum value = 4294967287</div>        </td></tr>
                <tr><td>maxclient<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum number of simultaneous open connections for the service group.</div><div>Minimum value = 0</div><div>Maximum value = 4294967294</div>        </td></tr>
                <tr><td>maxreq<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum number of requests that can be sent on a persistent connection to the service group.</div><div>Note. Connection requests beyond this value are rejected.</div><div>Minimum value = 0</div><div>Maximum value = 65535</div>        </td></tr>
                <tr><td>memberport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>member port.</div>        </td></tr>
                <tr><td rowspan="2">monitorbindings<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td><td></td>
    <td> <div>A list of monitornames to bind to this service</div><div>Note that the monitors must have already been setup possibly using the <span class='module'>netscaler_lb_monitor</span> module or some other method</div>    </tr>
    <tr>
    <td colspan="5">
    <table border=1 cellpadding=4>
    <caption><b>Dictionary object monitorbindings</b></caption>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
                    <tr><td>monitorname<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>T</div><div>h</div><div>e</div><div> </div><div>m</div><div>o</div><div>n</div><div>i</div><div>t</div><div>o</div><div>r</div><div> </div><div>n</div><div>a</div><div>m</div><div>e</div><div> </div><div>t</div><div>o</div><div> </div><div>b</div><div>i</div><div>n</div><div>d</div><div> </div><div>t</div><div>o</div><div> </div><div>t</div><div>h</div><div>i</div><div>s</div><div> </div><div>s</div><div>e</div><div>r</div><div>v</div><div>i</div><div>c</div><div>e</div><div>g</div><div>r</div><div>o</div><div>u</div><div>p</div>        </td></tr>
        </table>
    </td>
    </tr>
        </td></tr>
                <tr><td>monthreshold<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Minimum sum of weights of the monitors that are bound to this service. Used to determine whether to mark a service as UP or DOWN.</div><div>Minimum value = 0</div><div>Maximum value = 65535</div>        </td></tr>
                <tr><td>netprofile<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Network profile for the service group.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
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
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Path monitoring for clustering.</div>        </td></tr>
                <tr><td>pathmonitorindv<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Individual Path monitoring decisions.</div><div>Possible values = YES, NO</div>        </td></tr>
                <tr><td>rtspsessionidremap<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>Enable RTSP session ID mapping for the service group.</div><div>Default value = OFF</div>        </td></tr>
                <tr><td>save_config<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If true the module will save the configuration on the netscaler node if it makes any changes.</div><div>The module will not save the configuration on the netscaler node if it made no changes.</div>        </td></tr>
                <tr><td>sc<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>State of the SureConnect feature for the service group.</div><div>Default value = OFF</div>        </td></tr>
                <tr><td>servicegroupname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the service group. Must begin with an ASCII alphabetic or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore <code>_</code>, hash <code>#</code>, period <code>.</code>, space, colon <code>:</code>, at <code>@</code>, equals <code>=</code>, and hyphen <code>-</code> characters. Can be changed after the name is created.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td rowspan="2">servicemembers<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td><td></td>
    <td> <div>A list of dictionaries describing each service member of the service group</div><div>The dictionary for each member must contain the following keys.</div><div>ip. The ip address of the service member</div><div>port. The port of the service member</div><div>weight. The weight of this service member</div>    </tr>
    <tr>
    <td colspan="5">
    <table border=1 cellpadding=4>
    <caption><b>Dictionary object servicemembers</b></caption>
    <tr>
    <th class="head">parameter</th>
    <th class="head">required</th>
    <th class="head">default</th>
    <th class="head">choices</th>
    <th class="head">comments</th>
    </tr>
                    <tr><td>hashid<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>The hash identifier for the service.</div><div>This must be unique for each service.</div><div>This parameter is used by hash based load balancing methods.</div><div>Minimum value = 1</div>        </td></tr>
                    <tr><td>weight<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Weight to assign to the servers in the service group.</div><div>Specifies the capacity of the servers relative to the other servers in the load balancing configuration.</div><div>The higher the weight, the higher the percentage of requests sent to the service.</div><div>Minimum value = 1</div><div>Maximum value = 100</div>        </td></tr>
                    <tr><td>ip<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>i</div><div>p</div><div> </div><div>a</div><div>d</div><div>d</div><div>r</div><div>e</div><div>s</div><div>s</div><div> </div><div>o</div><div>f</div><div> </div><div>t</div><div>h</div><div>e</div><div> </div><div>s</div><div>e</div><div>r</div><div>v</div><div>i</div><div>c</div><div>e</div><div>.</div><div> </div><div>M</div><div>u</div><div>s</div><div>t</div><div> </div><div>n</div><div>o</div><div>t</div><div> </div><div>o</div><div>v</div><div>e</div><div>r</div><div>l</div><div>a</div><div>p</div><div> </div><div>w</div><div>i</div><div>t</div><div>h</div><div> </div><div>a</div><div>n</div><div> </div><div>e</div><div>x</div><div>i</div><div>s</div><div>t</div><div>i</div><div>n</div><div>g</div><div> </div><div>s</div><div>e</div><div>r</div><div>v</div><div>e</div><div>r</div><div> </div><div>e</div><div>n</div><div>t</div><div>i</div><div>t</div><div>y</div><div> </div><div>d</div><div>e</div><div>f</div><div>i</div><div>n</div><div>e</div><div>d</div><div> </div><div>b</div><div>y</div><div> </div><div>n</div><div>a</div><div>m</div><div>e</div><div>.</div>        </td></tr>
                    <tr><td>customserverid<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td>None</td>
                <td></td>
                <td><div>The identifier for this IP:Port pair.</div><div>Used when the persistency type is set to Custom Server ID.</div>        </td></tr>
                    <tr><td>servername<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Name of the server to which to bind the service group.</div><div>The server must already be configured as a named server.</div><div>Minimum length = 1</div>        </td></tr>
                    <tr><td>serverid<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>The identifier for the service.</div><div>This is used when the persistency type is set to Custom Server ID.</div>        </td></tr>
                    <tr><td>port<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Server port number.</div><div>Range 1 - 65535</div><div>* in CLI is represented as 65535 in NITRO API</div>        </td></tr>
        </table>
    </td>
    </tr>
        </td></tr>
                <tr><td>servicetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>HTTP</li><li>FTP</li><li>TCP</li><li>UDP</li><li>SSL</li><li>SSL_BRIDGE</li><li>SSL_TCP</li><li>DTLS</li><li>NNTP</li><li>RPCSVR</li><li>DNS</li><li>ADNS</li><li>SNMP</li><li>RTSP</li><li>DHCPRA</li><li>ANY</li><li>SIP_UDP</li><li>SIP_TCP</li><li>SIP_SSL</li><li>DNS_TCP</li><li>ADNS_TCP</li><li>MYSQL</li><li>MSSQL</li><li>ORACLE</li><li>RADIUS</li><li>RADIUSListener</li><li>RDP</li><li>DIAMETER</li><li>SSL_DIAMETER</li><li>TFTP</li><li>SMPP</li><li>PPTP</li><li>GRE</li><li>SYSLOGTCP</li><li>SYSLOGUDP</li><li>FIX</li><li>SSL_FIX</li></ul></td>
        <td><div>Protocol used to exchange data with the service.</div>        </td></tr>
                <tr><td>sp<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ON</li><li>OFF</li></ul></td>
        <td><div>Enable surge protection for the service group.</div><div>Default value = OFF</div>        </td></tr>
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
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Enable TCP buffering for the service group.</div>        </td></tr>
                <tr><td>tcpprofilename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the TCP profile that contains TCP configuration settings for the service group.</div><div>Minimum length = 1</div><div>Maximum length = 127</div>        </td></tr>
                <tr><td>useproxyport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Use the proxy port as the source port when initiating connections with the server. With the NO setting, the client-side connection port is used as the source port for the server-side connection.</div><div>Note. This parameter is available only when the Use Source IP (USIP) parameter is set to YES.</div><div>Possible values = YES, NO</div>        </td></tr>
                <tr><td>usip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Use client's IP address as the source IP address when initiating connection to the server. With the NO setting, which is the default, a mapped IP (MIP) address or subnet IP (SNIP) address is used as the source IP address to initiate server side connections.</div>        </td></tr>
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

    
    # The LB Monitor monitor-1 must already exist
    # Service members defined by C(ip) must not redefine an existing server's ip address.
    # Service members defined by C(servername) must already exist.
    
    - name: Setup http service with ip members
      delegate_to: localhost
      netscaler_servicegroup:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
    
        state: present
    
        servicegroupname: service-group-1
        servicetype: HTTP
        servicemembers:
            - ip: 10.78.78.78
              port: 80
              weight: 50
            - ip: 10.79.79.79
              port: 80
              weight: 40
            - servername: server-1
              port: 80
              weight: 10
    
        monitorbindings:
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