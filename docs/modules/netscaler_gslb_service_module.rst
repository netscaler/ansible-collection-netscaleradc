.. _netscaler_gslb_service:


netscaler_gslb_service - Manage gslb service entities in Netscaler.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4.0


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage gslb service entities in Netscaler.


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
                <tr><td>cip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>In the request that is forwarded to the GSLB service, insert a header that stores the client's IP address. Client IP header insertion is used in connection-proxy based site persistence.</div>        </td></tr>
                <tr><td>cipheader<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the HTTP header that stores the client's IP address. Used with the Client IP option. If client IP header insertion is enabled on the service and a name is not specified for the header, the NetScaler appliance uses the name specified by the cipHeader parameter in the set ns param command or, in the GUI, the Client IP Header parameter in the Configure HTTP Parameters dialog box.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>clttimeout<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy based site persistence is used.</div><div>Minimum value = 0</div><div>Maximum value = 31536000</div>        </td></tr>
                <tr><td>cnameentry<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Canonical name of the GSLB service. Used in CNAME-based GSLB.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>comment<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Any comments that you might want to associate with the GSLB service.</div>        </td></tr>
                <tr><td>downstateflush<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Flush all active transactions associated with the GSLB service when its state transitions from UP to DOWN. Do not enable this option for services that must complete their transactions. Applicable if connection proxy based site persistence is used.</div>        </td></tr>
                <tr><td>hashid<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Unique hash identifier for the GSLB service, used by hash based load balancing methods.</div><div>Minimum value = <code>1</code></div>        </td></tr>
                <tr><td>healthmonitor<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>Monitor the health of the GSLB service.</div>        </td></tr>
                <tr><td>ipaddress<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IP address for the GSLB service. Should represent a load balancing, content switching, or VPN virtual server on the NetScaler appliance, or the IP address of another load balancing device.</div>        </td></tr>
                <tr><td>maxaaausers<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is represented by this GSLB service. A GSLB service whose user count reaches the maximum is not considered when a GSLB decision is made, until the count drops below the maximum.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>65535</code></div>        </td></tr>
                <tr><td>maxbandwidth<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth reaches the maximum is not considered when a GSLB decision is made, until its bandwidth consumption drops below the maximum.</div>        </td></tr>
                <tr><td>maxclient<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The maximum number of open connections that the service can support at any given time. A GSLB service whose connection count reaches the maximum is not considered when a GSLB decision is made, until the connection count drops below the maximum.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>4294967294</code></div>        </td></tr>
                <tr><td rowspan="2">monitor_bindings<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td><td></td>
    <td> <div>Bind monitors to this gslb service</div>    </tr>
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
                    <tr><td>monitor_name<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Monitor name.</div>        </td></tr>
                    <tr><td>weight<br/><div style="font-size: small;"></div></td>
        <td>no</td>
        <td></td>
                <td></td>
                <td><div>Weight to assign to the monitor-service binding.</div><div>A larger number specifies a greater weight.</div><div>Contributes to the monitoring threshold, which determines the state of the service.</div><div>Minimum value = <code>1</code></div><div>Maximum value = <code>100</code></div>        </td></tr>
        </table>
    </td>
    </tr>
        </td></tr>
                <tr><td>monthreshold<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are bound to this GSLB service and are in the UP state is not equal to or greater than this threshold value, the service is marked as DOWN.</div><div>Minimum value = <code>0</code></div><div>Maximum value = <code>65535</code></div>        </td></tr>
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
                <tr><td>port<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Port on which the load balancing entity represented by this GSLB service listens.</div><div>Minimum value = 1</div><div>Range 1 - 65535</div><div>* in CLI is represented as 65535 in NITRO API</div>        </td></tr>
                <tr><td>publicip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The public IP address that a NAT device translates to the GSLB service's private IP address. Optional.</div>        </td></tr>
                <tr><td>publicport<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional.</div>        </td></tr>
                <tr><td>save_config<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>True</td>
        <td><ul><li>yes</li><li>no</li></ul></td>
        <td><div>If true the module will save the configuration on the netscaler node if it makes any changes.</div><div>The module will not save the configuration on the netscaler node if it made no changes.</div>        </td></tr>
                <tr><td>servername<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the server hosting the GSLB service.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>servicename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore <code>_</code>, hash <code>#</code>, period <code>.</code>, space, colon <code>:</code>, at <code>@</code>, equals <code>=</code>, and hyphen <code>-</code> characters. Can be changed after the GSLB service is created.</div><div></div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>servicetype<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>HTTP</li><li>FTP</li><li>TCP</li><li>UDP</li><li>SSL</li><li>SSL_BRIDGE</li><li>SSL_TCP</li><li>NNTP</li><li>ANY</li><li>SIP_UDP</li><li>SIP_TCP</li><li>SIP_SSL</li><li>RADIUS</li><li>RDP</li><li>RTSP</li><li>MYSQL</li><li>MSSQL</li><li>ORACLE</li></ul></td>
        <td><div>Type of service to create.</div>        </td></tr>
                <tr><td>sitename<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the GSLB site to which the service belongs.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>sitepersistence<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ConnectionProxy</li><li>HTTPRedirect</li><li>NONE</li></ul></td>
        <td><div>Use cookie-based site persistence. Applicable only to <code>HTTP</code> and <code>SSL</code> GSLB services.</div>        </td></tr>
                <tr><td>siteprefix<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The site's prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound service-domain pair by concatenating the site prefix of the service and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the NetScaler appliance redirects GSLB requests to GSLB services by using their site domains.</div>        </td></tr>
                <tr><td>state<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>present</td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>The state of the resource being configured by the module on the netscaler node.</div><div>When present the resource will be created if needed and configured according to the module's parameters.</div><div>When absent the resource will be deleted from the netscaler node.</div>        </td></tr>
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

    
    - name: Setup gslb service 2
    
      delegate_to: localhost
      register: result
      check_mode: "{{ check_mode }}"
    
      netscaler_gslb_service:
        operation: present
    
        servicename: gslb-service-2
        cnameentry: example.com
        sitename: gslb-site-1

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
        <td align=center> string </td>
        <td align=center> Action does not exist </td>
    </tr>
            <tr>
        <td> diff </td>
        <td> List of differences between the actual configured object and the configuration specified in the module </td>
        <td align=center> failure </td>
        <td align=center> dictionary </td>
        <td align=center> { 'targetlbvserver': 'difference. ours: (str) server1 other: (str) server2' } </td>
    </tr>
        <tr><td>contains: </td>
    <td colspan=4>
        <table border=1 cellpadding=2>
        <tr>
        <th class="head">name</th>
        <th class="head">description</th>
        <th class="head">returned</th>
        <th class="head">type</th>
        <th class="head">sample</th>
        </tr>

        
        </table>
    </td></tr>

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