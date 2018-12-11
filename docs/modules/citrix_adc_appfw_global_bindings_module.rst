:source: citrix_adc_appfw_global_bindings.py

:orphan:

.. _citrix_adc_appfw_global_bindings_module:


citrix_adc_appfw_global_bindings - Define global bindings for AppFW
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.8.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Define global bindings for AppFW
- Note that due to limitations in the NITRO API this module will always report a changed status.




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
                    <b>appfwpolicy_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>appfwpolicy bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>policyname</div>
                                                    <div>priority</div>
                                                    <div>gotopriorityexpression</div>
                                                    <div>invoke</div>
                                                    <div>state</div>
                                                    <div>labeltype</div>
                                                    <div>labelname</div>
                                                    <div>type</div>
                                                    <div>globalbindtype</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>auditnslogpolicy_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>auditnslogpolicy bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>policyname</div>
                                                    <div>priority</div>
                                                    <div>state</div>
                                                    <div>type</div>
                                                    <div>gotopriorityexpression</div>
                                                    <div>invoke</div>
                                                    <div>labeltype</div>
                                                    <div>labelname</div>
                                                                                </td>
            </tr>
                    
                                                <tr>
                                                                <td colspan="2">
                    <b>auditsyslogpolicy_bindings</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>auditsyslogpolicy bindings</div>
                                                                                </td>
            </tr>
                                                            <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>mode</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>bind</li>
                                                                                                                                                                                                <li>unbind</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>{&#x27;If mode is <code>bind</code>&#x27;: None}</div>
                                                    <div>Any bindings in the attributes list that do not exist will be created on the target Citrix ADC.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                    <div>{&#x27;If mode is <code>unbind</code>&#x27;: None}</div>
                                                    <div>Any bindings defined in the attributes list that also exist on the target Citrix ADC will be removed.</div>
                                                    <div>Existing bindings that are not on the attributes list remain unaffected.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                    <td class="elbow-placeholder"></td>
                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>List of the attributes dictionaries for the bindings.</div>
                                                    <div>{&#x27;Valid attribute keys&#x27;: None}</div>
                                                    <div>policyname</div>
                                                    <div>priority</div>
                                                    <div>state</div>
                                                    <div>type</div>
                                                    <div>gotopriorityexpression</div>
                                                    <div>invoke</div>
                                                    <div>labeltype</div>
                                                    <div>labelname</div>
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
- Sumanth Lingappa (@sumanth-lingappa)


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/citrix_adc_appfw_global_bindings.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
