:orphan:

.. _citrix_adc_gslb_service_module:

citrix_adc_gslb_service - Manage gslb service entities in Citrix ADC.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage gslb service entities in Citrix ADC.



Requirements
~~~~~~~~~~~~
The below requirements are needed on the host that executes this module.

- nitro python sdk


Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - api_path

        *(str)*
      -
      - Base NITRO API path.

        Define only in case of an ADM service proxy call
    * - appflowlog

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Enable logging appflow flow information.
    * - bearer_token

        *(str)*
      -
      - Authentication bearer token.

        Needed when doing an ADM service proxy call.
    * - cip

        *(str)*
      - Choices:

          - enabled
          - disabled
      - In the request that is forwarded to the GSLB service, insert a header that stores the client's IP address. Client IP header insertion is used in connection-proxy based site persistence.
    * - cipheader

        *(str)*
      -
      - Name for the HTTP header that stores the client's IP address. Used with the Client IP option. If client IP header insertion is enabled on the service and a name is not specified for the header, the Citrix ADC appliance uses the name specified by the cipHeader parameter in the set ns param command or, in the GUI, the Client IP Header parameter in the Configure HTTP Parameters dialog box.

        Minimum length = 1
    * - clttimeout

        *(float)*
      -
      - Idle time, in seconds, after which a client connection is terminated. Applicable if connection proxy based site persistence is used.

        Minimum value = 0

        Maximum value = 31536000
    * - cnameentry

        *(str)*
      -
      - Canonical name of the GSLB service. Used in CNAME-based GSLB.

        Minimum length = 1
    * - comment

        *(str)*
      -
      - Any comments that you might want to associate with the GSLB service.
    * - downstateflush

        *(str)*
      - Choices:

          - enabled
          - disabled
      - Flush all active transactions associated with the GSLB service when its state transitions from UP to DOWN. Do not enable this option for services that must complete their transactions. Applicable if connection proxy based site persistence is used.
    * - hashid

        *(float)*
      -
      - Unique hash identifier for the GSLB service, used by hash based load balancing methods.

        Minimum value = ``1``
    * - healthmonitor

        *(bool)*
      -
      - Monitor the health of the GSLB service.
    * - instance_id

        *(str)*
      -
      - The id of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Citrix ADC instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - instance_name

        *(str)*
      -
      - The name of the target Citrix ADC instance when issuing a Nitro request through a Citrix ADM proxy.
    * - ipaddress

        *(str)*
      -
      - IP address for the GSLB service. Should represent a load balancing, content switching, or VPN virtual server on the Citrix ADC appliance, or the IP address of another load balancing device.
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - When performing a Proxy API call with ADM service set this to ``true``
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Citrix ADC instance.

        When true you must also define the following options: ``nitro_auth_token``

        When true and adm service is the api proxy the following option must also be defined: ``bearer_token``

        When true you must define a target ADC by defining any of the following parameters

        I(instance_ip)

        I(instance_id)

        I(instance_name)
    * - maxaaausers

        *(float)*
      -
      - Maximum number of SSL VPN users that can be logged on concurrently to the VPN virtual server that is represented by this GSLB service. A GSLB service whose user count reaches the maximum is not considered when a GSLB decision is made, until the count drops below the maximum.

        Minimum value = ``0``

        Maximum value = ``65535``
    * - maxbandwidth

        *(float)*
      -
      - Integer specifying the maximum bandwidth allowed for the service. A GSLB service whose bandwidth reaches the maximum is not considered when a GSLB decision is made, until its bandwidth consumption drops below the maximum.
    * - maxclient

        *(float)*
      -
      - The maximum number of open connections that the service can support at any given time. A GSLB service whose connection count reaches the maximum is not considered when a GSLB decision is made, until the connection count drops below the maximum.

        Minimum value = ``0``

        Maximum value = ``4294967294``
    * - monitor_bindings

        *(list)*
      -
      - Bind monitors to this gslb service

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - monitor_name
              -
              - Monitor name.
            * - weight
              -
              - Weight to assign to the monitor-service binding.

                A larger number specifies a greater weight.

                Contributes to the monitoring threshold, which determines the state of the service.

                Minimum value = ``1``

                Maximum value = ``100``

    * - monthreshold

        *(float)*
      -
      - Monitoring threshold value for the GSLB service. If the sum of the weights of the monitors that are bound to this GSLB service and are in the UP state is not equal to or greater than this threshold value, the service is marked as DOWN.

        Minimum value = ``0``

        Maximum value = ``65535``
    * - nitro_auth_token

        *(str)*

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the Citrix ADC node.
    * - nitro_protocol

        *(str)*
      - Choices:

          - http
          - https (*default*)
      - Which protocol to use when accessing the nitro API objects.
    * - nitro_timeout

        *(float)*
      - Default:

        *310*
      - Time in seconds until a timeout error is thrown when establishing a new session with Citrix ADC
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the Citrix ADC node.
    * - nsip

        *(str)*
      -
      - The ip address of the Citrix ADC appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - port

        *(int)*
      -
      - Port on which the load balancing entity represented by this GSLB service listens.

        Minimum value = 1

        Range 1 - 65535

        * in CLI is represented as 65535 in NITRO API
    * - publicip

        *(str)*
      -
      - The public IP address that a NAT device translates to the GSLB service's private IP address. Optional.
    * - publicport

        *(int)*
      -
      - The public port associated with the GSLB service's public IP address. The port is mapped to the service's private port number. Applicable to the local GSLB service. Optional.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - servername

        *(str)*
      -
      - Name of the server hosting the GSLB service.

        Minimum length = 1
    * - servicename

        *(str)*
      -
      - Name for the GSLB service. Must begin with an ASCII alphanumeric or underscore ``_`` character, and must contain only ASCII alphanumeric, underscore ``_``, hash ``#``, period ``.``, space, colon ``:``, at ``@``, equals ``=``, and hyphen ``-`` characters. Can be changed after the GSLB service is created.

        

        Minimum length = 1
    * - servicetype

        *(str)*
      - Choices:

          - HTTP
          - FTP
          - TCP
          - UDP
          - SSL
          - SSL_BRIDGE
          - SSL_TCP
          - NNTP
          - ANY
          - SIP_UDP
          - SIP_TCP
          - SIP_SSL
          - RADIUS
          - RDP
          - RTSP
          - MYSQL
          - MSSQL
          - ORACLE
      - Type of service to create.
    * - sitename

        *(str)*
      -
      - Name of the GSLB site to which the service belongs.

        Minimum length = 1
    * - sitepersistence

        *(str)*
      - Choices:

          - ConnectionProxy
          - HTTPRedirect
          - NONE
      - Use cookie-based site persistence. Applicable only to ``HTTP`` and ``SSL`` GSLB services.
    * - siteprefix

        *(str)*
      -
      - The site's prefix string. When the service is bound to a GSLB virtual server, a GSLB site domain is generated internally for each bound service-domain pair by concatenating the site prefix of the service and the name of the domain. If the special string NONE is specified, the site-prefix string is unset. When implementing HTTP redirect site persistence, the Citrix ADC appliance redirects GSLB requests to GSLB services by using their site domains.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



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
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - diff

        *(dict)*
      - failure
      - List of differences between the actual configured object and the configuration specified in the module

        **Sample:**

        { 'targetlbvserver': 'difference. ours: (str) server1 other: (str) server2' }
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
