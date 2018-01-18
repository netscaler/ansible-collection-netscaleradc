.. _netscaler_nitro_request:


netscaler_nitro_request - Issue Nitro API requests to a Netscaler instance.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.5.0


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Issue Nitro API requests to a Netscaler instance.
* This is intended to be a short hand for using the uri Ansible module to issue the raw HTTP requests directly.
* It provides consistent return values and has no other dependencies apart from the base Ansible runtime environment.
* This module is intended to run either on the Ansible control node or a bastion (jumpserver) with access to the actual Netscaler instance




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
                <tr><td>action<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The action to perform when the <em>operation</em> value is set to <code>action</code>.</div><div>Some common values for this parameter are <code>enable</code>, <code>disable</code>, <code>rename</code>.</div>        </td></tr>
                <tr><td>args<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>A dictionary which defines the key arguments by which we will select the Nitro object to operate on.</div><div>It is required for the following <em>operation</em> values: <code>get_by_args</code>, <code>'delete_by_args'</code>.</div>        </td></tr>
                <tr><td>attributes<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The attributes of the Nitro object we are operating on.</div><div>It is required for the following <em>operation</em> values: <code>add</code>, <code>update</code>, <code>action</code>.</div>        </td></tr>
                <tr><td>expected_nitro_errorcode<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td>[0]</td>
        <td></td>
        <td><div>A list of numeric values that signify that the operation was successful.</div>        </td></tr>
                <tr><td>filter<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>A dictionary which defines the filter with which to refine the Nitro objects returned by the <code>get_filtered</code> <em>operation</em>.</div>        </td></tr>
                <tr><td>instance_id<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The id of the target Netscaler instance when issuing a Nitro request through a MAS proxy.</div>        </td></tr>
                <tr><td>instance_ip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The IP address of the target Netscaler instance when issuing a Nitro request through a MAS proxy.</div>        </td></tr>
                <tr><td>instance_name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the target Netscaler instance when issuing a Nitro request through a MAS proxy.</div>        </td></tr>
                <tr><td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The name of the resource we are operating on.</div><div>It is required for the following <em>operation</em> values: <code>update</code>, <code>get</code>, <code>delete</code>.</div>        </td></tr>
                <tr><td>nitro_auth_token<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The authentication token provided by the <code>mas_login</code> operation. It is required when issuing Nitro API calls through a MAS proxy.</div>        </td></tr>
                <tr><td>nitro_pass<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The password with which to authenticate to the Netscaler node.</div>        </td></tr>
                <tr><td>nitro_protocol<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td>http</td>
        <td><ul><li>http</li><li>https</li></ul></td>
        <td><div>Which protocol to use when accessing the Nitro API objects.</div>        </td></tr>
                <tr><td>nitro_user<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The username with which to authenticate to the Netscaler node.</div>        </td></tr>
                <tr><td>nsip<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The IP address of the Netscaler or MAS instance where the Nitro API calls will be made.</div><div>The port can be specified with the colon <code>:</code>. E.g. <code>192.168.1.1:555</code>.</div>        </td></tr>
                <tr><td>operation<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>add</li><li>update</li><li>get</li><li>get_by_args</li><li>get_filtered</li><li>get_all</li><li>delete</li><li>delete_by_args</li><li>count</li><li>mas_login</li><li>save_config</li><li>action</li></ul></td>
        <td><div>Define the Nitro operation that we want to perform.</div>        </td></tr>
                <tr><td>resource<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>The type of resource we are operating on.</div><div>It is required for all <em>operation</em> values except <code>mas_login</code> and <code>save_config</code>.</div>        </td></tr>
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


    - name: Add a server
      delegate_to: localhost
      netscaler_nitro_request:
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
      netscaler_nitro_request:
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
      netscaler_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: get
        resource: server
        name: test-server-1

    - name: Delete server
      delegate_to: localhost
      register: result
      netscaler_nitro_request:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: delete
        resource: server
        name: test-server-1

    - name: Rename server
      delegate_to: localhost
      netscaler_nitro_request:
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
      netscaler_nitro_request:
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
      netscaler_nitro_request:
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
      netscaler_nitro_request:
        nsip: "{{ mas_ip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        operation: mas_login

    - name: Add resource through MAS proxy
      delegate_to: localhost
      netscaler_nitro_request:
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
        <td> nitro_severity </td>
        <td> A string describing the severity of the NITRO operation error or NONE. </td>
        <td align=center> always </td>
        <td align=center> string </td>
        <td align=center> NONE </td>
    </tr>
            <tr>
        <td> http_response_body </td>
        <td> A string with the actual HTTP response body content if existent. If there is no HTTP response body it is an empty string. </td>
        <td align=center> always </td>
        <td align=center> string </td>
        <td align=center> { errorcode: 0, message: Done, severity: NONE } </td>
    </tr>
            <tr>
        <td> http_response_data </td>
        <td> A dictionary that contains all the HTTP response's data. </td>
        <td align=center> always </td>
        <td align=center> dict </td>
        <td align=center> status: 200 </td>
    </tr>
            <tr>
        <td> nitro_message </td>
        <td> A string containing a human readable explanation for the NITRO operation result. </td>
        <td align=center> always </td>
        <td align=center> string </td>
        <td align=center> Success </td>
    </tr>
            <tr>
        <td> nitro_object </td>
        <td> The object returned from the NITRO operation. This is applicable to the various get operations which return an object. </td>
        <td align=center> when applicable </td>
        <td align=center> list </td>
        <td align=center> [{'state': 'ENABLED', 'name': 'test-server-1', 'ipv6address': 'NO', 'maxbandwidth': '0', 'sp': 'OFF', 'ipaddress': '192.168.1.8', 'port': 0}] </td>
    </tr>
            <tr>
        <td> nitro_auth_token </td>
        <td> The token returned by the C(mas_login) operation when succesful. </td>
        <td align=center> when applicable </td>
        <td align=center> string </td>
        <td align=center> ##E8D7D74DDBD907EE579E8BB8FF4529655F22227C1C82A34BFC93C9539D66 </td>
    </tr>
            <tr>
        <td> nitro_errorcode </td>
        <td> A numeric value containing the return code of the NITRO operation. When 0 the operation is succesful. Any non zero value indicates an error. </td>
        <td align=center> always </td>
        <td align=center> int </td>
        <td align=center> 0 </td>
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
