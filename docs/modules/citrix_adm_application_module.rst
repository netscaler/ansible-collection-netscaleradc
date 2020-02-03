:orphan:

.. _citrix_adm_application_module:

citrix_adm_application - Manage applications on Citrix ADM.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.9

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage applications on Citrix ADM.
- Note that due to limitations on the underlying NITRO API an update is always forced when I(state=present).




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - app_category

        *(str)*
      -
      - Application Category.

        Minimum length = 1

        Maximum length = 255
    * - app_components

        *(list)*
      -
      - Application components.
    * - app_criteria

        *(list)*
      -
      - Application criteria.
    * - application_ids

        *(list)*
      -
      - Application IDs that are part of this application.
    * - application_managed

        *(bool)*
      -
      - Managed field.
    * - check_create

        *(bool)*
      - Default:

        *True*
      - Check if the application was created on the target citrix adm.

        Return the created application in the module results.
    * - check_create_delay

        *(int)*
      - Default:

        *10*
      - Time in seconds to wait between the create/update operation and retrieval of the created application.

        This delay should be non zero as the newly created/updated application might not be immediately available to be fetched by the target Citrix ADM.
    * - curclntconnections

        *(str)*
      -
      - curclntconnections Value across all vips of the app.
    * - cursrvrconnections

        *(str)*
      -
      - cursrvrconnections Value across all vips of the app.
    * - family

        *(str)*
      -
      - Application Family.

        Minimum length = 1

        Maximum length = 255
    * - force_delete

        *(bool)*
      -
      - force delete.
    * - id

        *(str)*
      -
      - Id is system generated key..
    * - instance_ip

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a MAS node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - name

        *(str)*
      -
      - Application Name.

        Maximum length = 1024
    * - nitro_auth_token

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass
      -
      - The password with which to authenticate to the netscaler node.
    * - nitro_protocol
      - Choices:

          - http (*default*)
          - https
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
    * - nitro_user
      -
      - The username with which to authenticate to the netscaler node.
    * - no_of_auth

        *(str)*
      -
      - Number of AUTH VIPs.
    * - no_of_cr

        *(str)*
      -
      - Number of CR VIPs.
    * - no_of_cs

        *(str)*
      -
      - Number of CS VIPs.
    * - no_of_gslb

        *(str)*
      -
      - Number of GSLB VIPs.
    * - no_of_gslbsvc

        *(str)*
      -
      - Number of LB VIPs.
    * - no_of_haproxy_be

        *(str)*
      -
      - Number of Banckends.
    * - no_of_haproxy_fe

        *(str)*
      -
      - Number of Frontends.
    * - no_of_lb

        *(str)*
      -
      - Number of LB VIPs.
    * - no_of_svc

        *(str)*
      -
      - Number of Services.
    * - no_of_svcgrp

        *(str)*
      -
      - Number of Service Groups.
    * - no_of_svr

        *(str)*
      -
      - Number of Servers.
    * - no_of_vpn

        *(str)*
      -
      - Number of VPN VIPs.
    * - nsip
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - poll_after_delete

        *(bool)*
      - Default:

        *False*
      - Poll the instances after deleting an application to update the application list immediately.

        By default Citrix ADM will poll every 30 minutes.
    * - poll_delay

        *(int)*
      - Default:

        *10*
      - Time in seconds to wait between the delete operation and the subsequent poll operation.

        This is only relevant when ``state`` is set to ``absent`` and ``poll_after_delete`` is set to ``true``.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - state
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - stylebook_params

        *(str)*
      -
      - Stylebook Parameter.
    * - throughput_avg

        *(str)*
      -
      - Sum of throughput across all vips of the app.
    * - validate_certs
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    vars:
      stylebook_params:
        name: "basic-lb-config"
        namespace: "com.example.stylebooks"
        version: "0.1"
        configpack_payload:
          parameters:
            name: "playbook5_test_application_name"
            ip: "192.168.5.2"
            lb-alg: "ROUNDROBIN"
            svc-servers:
              - "192.168.5.3"
            svc-port: "80"
          targets:
            - id: "6a28b48b-e7c0-4770-b499-3ddb85b47561"
    
    tasks:
      - name: Login to citrix_adm
        delegate_to: localhost
        register: login_result
        citrix_adm_login:
          mas_ip: 192.168.1.1
          mas_user: nsroot
          mas_pass: nsroot
    
      - name: Setup application
        delegate_to: localhost
        citrix_adm_application:
          mas_ip: 192.168.1.1
          nitro_auth_token: "{{ login_result.session_id }}"
    
          state: present
    
          app_category: test_category
          name: playbook5_test_application_name-lb_10.78.60.209_lb
          stylebook_params: "{{ stylebook_params | to_json }}"


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - application

        *(dict)*
      - success
      - Dictionary containing all the attributes of the created application
    * - loglines

        *(list)*
      - always
      - list of logged messages by the module

        **Sample:**

        ['message 1', 'message 2']
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
