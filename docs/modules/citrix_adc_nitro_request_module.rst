:source: citrix_adc_nitro_request.py

:orphan:

.. _citrix_adc_nitro_request_module:


citrix_adc_nitro_request - Issue Nitro API requests to a Netscaler instance
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5.0

.. contents::
   :local:
   :depth: 2


Synopsis
--------
- Issue Nitro API requests to a Netscaler instance.
- This is intended to be a short hand for using the uri Ansible module to issue the raw HTTP requests directly.
- It provides consistent return values and has no other dependencies apart from the base Ansible runtime environment.
- This module is intended to run either on the Ansible control node or a bastion (jumpserver) with access to the actual Netscaler instance




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
                                                                        <div>The action to perform when the <em>operation</em> value is set to <code>action</code>.</div>
                                                    <div>Some common values for this parameter are <code>enable</code>, <code>disable</code>, <code>rename</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>args</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A dictionary which defines the key arguments by which we will select the Nitro object to operate on.</div>
                                                    <div>It is required for the following <em>operation</em> values: <code>get_by_args</code>, <code>&#x27;delete_by_args&#x27;</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>attributes</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The attributes of the Nitro object we are operating on.</div>
                                                    <div>It is required for the following <em>operation</em> values: <code>add</code>, <code>update</code>, <code>action</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>expected_nitro_errorcode</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                                    <b>Default:</b><br/><div style="color: blue">[0]</div>
                                    </td>
                                                                <td>
                                                                        <div>A list of numeric values that signify that the operation was successful.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>filter</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>A dictionary which defines the filter with which to refine the Nitro objects returned by the <code>get_filtered</code> <em>operation</em>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>instance_id</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The id of the target Netscaler instance when issuing a Nitro request through a MAS proxy.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>instance_ip</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The IP address of the target Netscaler instance when issuing a Nitro request through a MAS proxy.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>instance_name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The name of the target Netscaler instance when issuing a Nitro request through a MAS proxy.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>name</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The name of the resource we are operating on.</div>
                                                    <div>It is required for the following <em>operation</em> values: <code>update</code>, <code>get</code>, <code>delete</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nitro_auth_token</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The authentication token provided by the <code>mas_login</code> operation. It is required when issuing Nitro API calls through a MAS proxy.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nitro_pass</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The password with which to authenticate to the Netscaler node.</div>
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
                                                                        <div>Which protocol to use when accessing the Nitro API objects.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nitro_user</b>
                                        <br/><div style="font-size: small; color: red">required</div>                                    </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The username with which to authenticate to the Netscaler node.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>nsip</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The IP address of the Netscaler or MAS instance where the Nitro API calls will be made.</div>
                                                    <div>The port can be specified with the colon <code>:</code>. E.g. <code>192.168.1.1:555</code>.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>operation</b>
                                                                            </td>
                                <td>
                                                                                                                            <ul><b>Choices:</b>
                                                                                                                                                                <li>add</li>
                                                                                                                                                                                                <li>update</li>
                                                                                                                                                                                                <li>get</li>
                                                                                                                                                                                                <li>get_by_args</li>
                                                                                                                                                                                                <li>get_filtered</li>
                                                                                                                                                                                                <li>get_all</li>
                                                                                                                                                                                                <li>delete</li>
                                                                                                                                                                                                <li>delete_by_args</li>
                                                                                                                                                                                                <li>count</li>
                                                                                                                                                                                                <li>mas_login</li>
                                                                                                                                                                                                <li>save_config</li>
                                                                                                                                                                                                <li>action</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Define the Nitro operation that we want to perform.</div>
                                                                                </td>
            </tr>
                                <tr>
                                                                <td colspan="1">
                    <b>resource</b>
                                                                            </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>The type of resource we are operating on.</div>
                                                    <div>It is required for all <em>operation</em> values except <code>mas_login</code> and <code>save_config</code>.</div>
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



Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add a server
      delegate_to: localhost
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: add
        resource: server
        name: test-server-1
        attributes:
          name: test-server-1
          ipaddress: 192.168.1.1

    - name: Update server
      delegate_to: localhost
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: update
        resource: server
        name: test-server-1
        attributes:
          name: test-server-1
          ipaddress: 192.168.1.2

    - name: Get server
      delegate_to: localhost
      register: result
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: get
        resource: server
        name: test-server-1

    - name: Delete server
      delegate_to: localhost
      register: result
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: delete
        resource: server
        name: test-server-1

    - name: Rename server
      delegate_to: localhost
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: action
        action: rename
        resource: server
        attributes:
          name: test-server-1
          newname: test-server-2

    - name: Get server by args
      delegate_to: localhost
      register: result
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: get_by_args
        resource: server
        args:
          name: test-server-1

    - name: Get server by filter
      delegate_to: localhost
      register: result
      citrix_adc_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: get_filtered
        resource: server
        filter:
          ipaddress: 192.168.1.2

    # Doing a NITRO request through MAS.
    # Requires to have an authentication token from the mas_login and used as the nitro_auth_token parameter
    # Also nsip is the MAS address and the target Netscaler IP must be defined with instance_ip
    # The rest of the task arguments remain the same as when issuing the NITRO request directly to a Netscaler instance.

    - name: Do mas login
      delegate_to: localhost
      register: login_result
      citrix_adc_nitro_request:
        nsip: "{{ mas_ip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: mas_login

    - name: Add resource through MAS proxy
      delegate_to: localhost
      citrix_adc_nitro_request:
        nsip: "{{ mas_ip }}"
        nitro_auth_token: "{{ login_result.nitro_auth_token }}"
        instance_ip: "{{ nsip }}"
        operation: add
        resource: server
        name: test-server-1
        attributes:
          name: test-server-1
          ipaddress: 192.168.1.7




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
                    <b>http_response_body</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A string with the actual HTTP response body content if existent. If there is no HTTP response body it is an empty string.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{ errorcode: 0, message: Done, severity: NONE }</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>http_response_data</b>
                    <br/><div style="font-size: small; color: red">dict</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A dictionary that contains all the HTTP response&#x27;s data.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">status: 200</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>nitro_auth_token</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>when applicable</td>
                <td>
                                            <div>The token returned by the <code>mas_login</code> operation when succesful.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">##E8D7D74DDBD907EE579E8BB8FF4529655F22227C1C82A34BFC93C9539D66</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>nitro_errorcode</b>
                    <br/><div style="font-size: small; color: red">int</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A numeric value containing the return code of the NITRO operation. When 0 the operation is succesful. Any non zero value indicates an error.</div>
                                        <br/>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>nitro_message</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A string containing a human readable explanation for the NITRO operation result.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">Success</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>nitro_object</b>
                    <br/><div style="font-size: small; color: red">list</div>
                                    </td>
                <td>when applicable</td>
                <td>
                                            <div>The object returned from the NITRO operation. This is applicable to the various get operations which return an object.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;ipv6address&#x27;: &#x27;NO&#x27;, &#x27;sp&#x27;: &#x27;OFF&#x27;, &#x27;name&#x27;: &#x27;test-server-1&#x27;, &#x27;port&#x27;: 0, &#x27;maxbandwidth&#x27;: &#x27;0&#x27;, &#x27;ipaddress&#x27;: &#x27;192.168.1.8&#x27;, &#x27;state&#x27;: &#x27;ENABLED&#x27;}]</div>
                                    </td>
            </tr>
                                <tr>
                                <td colspan="1">
                    <b>nitro_severity</b>
                    <br/><div style="font-size: small; color: red">string</div>
                                    </td>
                <td>always</td>
                <td>
                                            <div>A string describing the severity of the NITRO operation error or NONE.</div>
                                        <br/>
                                            <div style="font-size: smaller"><b>Sample:</b></div>
                                                <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">NONE</div>
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
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/citrix_adc_nitro_request.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
