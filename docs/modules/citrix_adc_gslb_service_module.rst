:source: citrix_adc_gslb_service.py

:orphan:

.. _citrix_adc_gslb_service_module:


citrix_adc_gslb_service - Manage gslb service entities in Netscaler
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Manage gslb service entities in Netscaler.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- nitro python sdk


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>cip</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>In the request that is forwarded to the GSLB service, insert a header that stores the client&#x27;s IP address. Client IP header insertion is used in connection-proxy based site persistence.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>cipheader</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name for the HTTP header that stores the client&#x27;s IP address. Used with the Client IP option. If client IP header insertion is enabled on the service and a name is not specified for the header, the NetScaler appliance uses the name specified by the cipHeader parameter in the set ns param command or, in the GUI, the Client IP Header parameter in the Configure HTTP Parameters dialog box.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>clttimeout</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy based site persistence is used.</div>
                                                    <div>Minimum value = 0</div>
                                                    <div>Maximum value = 31536000</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>cnameentry</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Canonical name of the GSLB service. Used in CNAME-based GSLB.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>comment</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Any comments that you might want to associate with the GSLB service.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>downstateflush</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>enabled</li>
                                                                                                                                                                                                <li>disabled</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Flush all active transactions associated with the GSLB service when its state transitions from UP to DOWN. Do not enable this option for services that must complete their transactions. Applicable if connection proxy based site persistence is used.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>hashid</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Unique hash identifier for the GSLB service, used by hash based load balancing methods.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>healthmonitor</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                        <ul><b>Choices:</b>
                                                                                                                                                                <li>no</li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Monitor the health of the GSLB service.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>ipaddress</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>IP address for the GSLB service. Should represent a load balancing, content switching, or VPN virtual server on the NetScaler appliance, or the IP address of another load balancing device.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>maxaaausers</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is represented by this GSLB service. A GSLB service whose user count reaches the maximum is not considered when a GSLB decision is made, until the count drops below the maximum.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>65535</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>maxbandwidth</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth reaches the maximum is not considered when a GSLB decision is made, until its bandwidth consumption drops below the maximum.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>maxclient</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The maximum number of open connections that the service can support at any given time. A GSLB service whose connection count reaches the maximum is not considered when a GSLB decision is made, until the connection count drops below the maximum.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>4294967294</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>monitor_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Bind monitors to this gslb service</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>weight</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Weight to assign to the monitor-service binding.</div>
                                                    <div>A larger number specifies a greater weight.</div>
                                                    <div>Contributes to the monitoring threshold, which determines the state of the service.</div>
                                                    <div>Minimum value = <code>1</code></div>
                                                    <div>Maximum value = <code>100</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>monitor_name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Monitor name.</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>monthreshold</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are bound to this GSLB service and are in the UP state is not equal to or greater than this threshold value, the service is marked as DOWN.</div>
                                                    <div>Minimum value = <code>0</code></div>
                                                    <div>Maximum value = <code>65535</code></div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>port</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Port on which the load balancing entity represented by this GSLB service listens.</div>
                                                    <div>Minimum value = 1</div>
                                                    <div>Range 1 - 65535</div>
                                                    <div>* in CLI is represented as 65535 in NITRO API</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>publicip</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The public IP address that a NAT device translates to the GSLB service&#x27;s private IP address. Optional.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>publicport</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The public port associated with the GSLB service&#x27;s public IP address. The port is mapped to the service&#x27;s private port number. Applicable to the local GSLB service. Optional.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>servername</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the server hosting the GSLB service.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>servicename</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore <code>_</code>, hash <code>#</code>, period <code>.</code>, space, colon <code>:</code>, at <code>@</code>, equals <code>=</code>, and hyphen <code>-</code> characters. Can be changed after the GSLB service is created.</div>
                                                    <div></div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>servicetype</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>HTTP</li>
                                                                                                                                                                                                <li>FTP</li>
                                                                                                                                                                                                <li>TCP</li>
                                                                                                                                                                                                <li>UDP</li>
                                                                                                                                                                                                <li>SSL</li>
                                                                                                                                                                                                <li>SSL_BRIDGE</li>
                                                                                                                                                                                                <li>SSL_TCP</li>
                                                                                                                                                                                                <li>NNTP</li>
                                                                                                                                                                                                <li>ANY</li>
                                                                                                                                                                                                <li>SIP_UDP</li>
                                                                                                                                                                                                <li>SIP_TCP</li>
                                                                                                                                                                                                <li>SIP_SSL</li>
                                                                                                                                                                                                <li>RADIUS</li>
                                                                                                                                                                                                <li>RDP</li>
                                                                                                                                                                                                <li>RTSP</li>
                                                                                                                                                                                                <li>MYSQL</li>
                                                                                                                                                                                                <li>MSSQL</li>
                                                                                                                                                                                                <li>ORACLE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Type of service to create.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sitename</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name of the GSLB site to which the service belongs.</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>sitepersistence</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>ConnectionProxy</li>
                                                                                                                                                                                                <li>HTTPRedirect</li>
                                                                                                                                                                                                <li>NONE</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Use cookie-based site persistence. Applicable only to <code>HTTP</code> and <code>SSL</code> GSLB services.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
                    <b>siteprefix</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The site&#x27;s prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound service-domain pair by concatenating the site prefix of the service and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the NetScaler appliance redirects GSLB requests to GSLB services by using their site domains.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="2">
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
                                                                <td colspan="2">
                    <b>validate_certs</b>
                                                                            </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">yes</div>
                                    </td>
                                                                <td>
                                                                        <div>If <code>no</code>, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.</div>
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

    
    - name: Setup gslb service 2

      delegate_to: localhost
      register: result
      check_mode: "{{ check_mode }}"

      citrix_adc_gslb_service:
        operation: present

        servicename: gslb-service-2
        cnameentry: example.com
        sitename: gslb-site-1




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
                    <br/><div style="font-size: small; color: red">dictionary</div>
                                    </td>
                <td>failure</td>
                <td>
                                            <div>List of differences between the actual configured object and the configuration specified in the module</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{ &#x27;targetlbvserver&#x27;: &#x27;difference. ours: (str) server1 other: (str) server2&#x27; }</div>
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
                    <br/><div style="font-size: small; color: red">string</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/citrix_adc_gslb_service.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
