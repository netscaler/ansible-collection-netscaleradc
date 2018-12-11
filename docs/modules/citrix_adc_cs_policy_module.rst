:source: citrix_adc_cs_policy.py

:orphan:

.. _citrix_adc_cs_policy_module:


citrix_adc_cs_policy - Manage content switching policy
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Manage content switching policy.
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
                    <b>action</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Content switching action that names the target load balancing virtual server to which the traffic is switched.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>domain</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The domain name. The string value can range to 63 characters.</div>
                                                    <div>Minimum length = 1</div>
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
                    <b>policyname</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Name for the content switching policy. Must begin with an ASCII alphanumeric or underscore <code>_</code> character, and must contain only ASCII alphanumeric, underscore, hash <code>#</code>, period <code>.</code>, space <code> </code>, colon <code>:</code>, at sign <code>@</code>, equal sign <code>=</code>, and hyphen <code>-</code> characters. Cannot be changed after a policy is created.</div>
                                                    <div>The following requirement applies only to the NetScaler CLI:</div>
                                                    <div>If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, my policy or my policy).</div>
                                                    <div>Minimum length = 1</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>rule</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Expression, or name of a named expression, against which traffic is evaluated. Written in the classic or default syntax.</div>
                                                    <div>Note:</div>
                                                    <div>Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: &#x27;&quot;&lt;string of 255 characters&gt;&quot; + &quot;&lt;string of 245 characters&gt;&quot;&#x27;</div>
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
                    <b>url</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>URL string that is matched with the URL of a request. Can contain a wildcard character. Specify the string value in the following format: <code>[[prefix] [*]] [.suffix]</code>.</div>
                                                    <div>Minimum length = 1</div>
                                                    <div>Maximum length = 208</div>
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
                        </table>
    <br/>


Notes
-----

.. note::
    - For more information on using Ansible to manage Citrix NetScaler Network devices see https://www.ansible.com/ansible-netscaler.


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Create url cs policy
      delegate_to: localhost
      citrix_adc_cs_policy:
        nsip: 172.18.0.2
        nitro_user: nsroot
        nitro_pass: nsroot
        validate_certs: no

        state: present

        policyname: policy_1
        url: /example/




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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;url&#x27;: &#x27;difference. ours: (str) example1 other: (str) /example1&#x27;}</div>
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
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Could not load nitro python sdk</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/citrix_adc_cs_policy.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
