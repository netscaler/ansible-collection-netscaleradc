.. _netscaler_server:


netscaler_server - Manage server configuration
++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.2.3


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage server configuration
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
                <tr><td>ipaddress<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>IPv4 or IPv6 address of the server. If you create an IP address based server, you can specify the name of the server, instead of its IP address, when creating a service. Note. If you do not create a server entry, the server IP address that you enter when you create a service becomes the name of the server.</div>        </td></tr>
                <tr><td>name<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the server.</div><div>Must begin with an ASCII alphabetic or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.</div><div>Can be changed after the name is created.</div><div>Minimum length = 1</div>        </td></tr>
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
                <tr><td>operation<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td><ul><li>present</li><li>absent</li></ul></td>
        <td><div>The operation to perform for the given netscaler module.</div><div>When present the resource will be created if needed and configured according to the module's parameters.</div><div>When absent the resource will be deleted from the netscaler node.</div>        </td></tr>
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

    
    - name: Connect to netscaler appliance
        local_action:
            nsip: 172.18.0.2
            nitro_user: nsroot
            nitro_pass: nsroot
            ssl_cert_validation: no
    
            module: netscaler_server
            operation: present
    
            name: vserver1
            ipaddress: 192.168.1.1

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
        <td align=center> {'targetlbvserver': 'difference. ours: (str) server1 other: (str) server2'} </td>
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