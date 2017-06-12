.. _netscaler_ssl_certkey:


netscaler_ssl_certkey - Manage ssl cerificate keys.
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.4.0


.. contents::
   :local:
   :depth: 2


Synopsis
--------

* Manage ssl cerificate keys.




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
                <tr><td>bundle<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>YES</li><li>NO</li></ul></td>
        <td><div>Parse the certificate chain as a single file after linking the server certificate to its issuer's certificate within the file.</div><div>Default value = NO</div>        </td></tr>
                <tr><td>cert<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of and, optionally, path to the X509 certificate file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>certkey<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name for the certificate and private-key pair. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the certificate-key pair is created.</div><div>The following requirement applies only to the NetScaler CLI.</div><div>If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my cert" or 'my cert').</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>expirymonitor<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>ENABLED</li><li>DISABLED</li></ul></td>
        <td><div>Issue an alert when the certificate is about to expire.</div>        </td></tr>
                <tr><td>fipskey<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the FIPS key that was created inside the Hardware Security Module (HSM) of a FIPS appliance, or a key that was imported into the HSM.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>hsmkey<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the HSM key that was created in the External Hardware Security Module (HSM) of a FIPS appliance.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>inform<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td><ul><li>DER</li><li>PEM</li><li>PFX</li></ul></td>
        <td><div>Input format of the certificate and the private-key files. The three formats supported by the appliance are.</div><div>PEM - Privacy Enhanced Mail</div><div>DER - Distinguished Encoding Rule</div><div>PFX - Personal Information Exchange.</div><div>Default value = PEM</div>        </td></tr>
                <tr><td>key<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of and, optionally, path to the private-key file that is used to form the certificate-key pair. The certificate file should be present on the appliance's hard-disk drive or solid-state drive. Storing a certificate in any location other than the default might cause inconsistency in a high availability setup. /nsconfig/ssl/ is the default path.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>linkcertkeyname<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Name of the Certificate Authority certificate-key pair to which to link a certificate-key pair.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>notificationperiod<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Time, in number of days, before certificate expiration, at which to generate an alert that the certificate is about to expire.</div><div>Minimum value = 10</div><div>Maximum value = 100</div>        </td></tr>
                <tr><td>nsip<br/><div style="font-size: small;"></div></td>
    <td>yes</td>
    <td></td>
        <td></td>
        <td><div>The Nescaler ip address.</div>        </td></tr>
                <tr><td>passplain<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Pass phrase used to encrypt the private-key. Required when adding an encrypted private-key in PEM format.</div><div>Minimum length = 1</div>        </td></tr>
                <tr><td>password<br/><div style="font-size: small;"></div></td>
    <td>no</td>
    <td></td>
        <td></td>
        <td><div>Passphrase that was used to encrypt the private-key. Use this option to load encrypted private-keys in PEM format.</div>        </td></tr>
        </table>
    </br>



Examples
--------

 ::

    
    - name: Connect to netscaler appliance
        netscaler_service_group:
            nsip: "172.17.0.2"

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
        <td> config_updated </td>
        <td> determine if a change in the netscaler configuration happened </td>
        <td align=center> always </td>
        <td align=center> boolean </td>
        <td align=center> False </td>
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