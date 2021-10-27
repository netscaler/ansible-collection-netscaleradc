:orphan:

.. _citrix_adc_appfw_settings_module:

citrix_adc_appfw_settings - Manage Citrix ADC Web Application Firewall settings.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADC Web Application Firewall settings.
- The module uses the NITRO API to make configuration changes to WAF settings on the target Citrix ADC.
- The NITRO API reference can be found at https://developer-docs.citrix.com/projects/netscaler-nitro-api/en/latest
- Note that due to NITRO API limitations this module will always report a changed status even when configuration changes have not taken place.




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
    * - bearer_token

        *(str)*
      -
      - Authentication bearer token.

        Needed when doing an ADM service proxy call.
    * - ceflogging

        *(bool)*
      -
      - Enable CEF format logs.
    * - clientiploggingheader

        *(str)*
      -
      - Name of an HTTP header that contains the IP address that the client used to connect to the protected site or service.
    * - cookiepostencryptprefix

        *(str)*
      -
      - String that is prepended to all encrypted cookie values.

        Minimum length =  1
    * - defaultprofile

        *(str)*
      -
      - Profile to use when a connection does not match any policy. Default setting is APPFW_BYPASS, which unmatched connections back to the Citrix ADC without attempting to filter them further.

        Minimum length =  1
    * - entitydecoding

        *(bool)*
      -
      - Transform multibyte (double- or half-width) characters to single width characters.
    * - geolocationlogging

        *(bool)*
      -
      - Enable Geo-Location Logging in CEF format logs.
    * - importsizelimit

        *(str)*
      -
      - Cumulative total maximum number of bytes in web forms imported to a protected web site. If a user to upload files with a total byte count higher than the specified limit, the application firewall the request.

        Minimum value = ``1``

        Maximum value = ``268435456``
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
    * - is_cloud

        *(bool)*
      - Default:

        *False*
      - When performing a Proxy API call with ADM service set this to ``true``
    * - learnratelimit

        *(str)*
      -
      - Maximum number of connections per second that the application firewall learning engine examines to new relaxations for learning-enabled security checks. The application firewall drops any connections this limit from the list of connections used by the learning engine.

        Minimum value = ``1``

        Maximum value = ``1000``
    * - logmalformedreq

        *(bool)*
      -
      - Log requests that are so malformed that application firewall parsing doesn't occur.
    * - malformedreqaction

        *(list)*
      - Choices:

          - none
          - block
          - log
          - stats
      - flag to define action on malformed requests that application firewall cannot parse.
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
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the Citrix ADC node if it makes any changes.

        The module will not save the configuration on the Citrix ADC node if it made no changes.
    * - sessioncookiename

        *(str)*
      -
      - Name of the session cookie that the application firewall uses to track user sessions.

        Must begin with a letter or number, and can consist of from 1 to 31 letters, numbers, and the hyphen and underscore (_) symbols.

        The following requirement applies only to the Citrix ADC CLI:

        If the name includes one or more spaces, enclose the name in double or single quotation marks (for "my cookie name" or 'my cookie name').

        Minimum length =  1
    * - sessionlifetime

        *(str)*
      -
      - Maximum amount of time (in seconds) that the application firewall allows a user session to remain regardless of user activity. After this time, the user session is terminated. Before continuing to the protected web site, the user must establish a new session by opening a designated start URL.

        Minimum value = ``0``

        Maximum value = ``2147483647``
    * - sessionlimit

        *(str)*
      -
      - Maximum number of sessions that the application firewall allows to be active, regardless of user After the max_limit reaches, No more user session will be created .

        Minimum value = ``0``

        Maximum value = ``500000``
    * - sessiontimeout

        *(str)*
      -
      - Timeout, in seconds, after which a user session is terminated. Before continuing to use the protected site, the user must establish a new session by opening a designated start URL.

        Minimum value = ``1``

        Maximum value = ``65535``
    * - signatureautoupdate

        *(bool)*
      -
      - Flag used to enable/disable auto update signatures.
    * - signatureurl

        *(str)*
      -
      - URL to download the mapping file from server.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the Citrix ADC node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the Citrix ADC node.
    * - undefaction

        *(str)*
      -
      - Profile to use when an application firewall policy evaluates to undefined (UNDEF).

        An UNDEF event indicates an internal error condition. The APPFW_BLOCK built-in profile is the default You can specify a different built-in or user-created profile as the UNDEF profile.

        Minimum length =  1
    * - useconfigurablesecretkey

        *(bool)*
      -
      - Use configurable secret key in AppFw operations.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: setup basic settings
      delegate_to: localhost
      citrix_adc_appfw_settings:
        nitro_user: nsroot
        nitro_pass: nsroot
        nsip: 172.18.0.2
        state: present
        defaultprofile: APPFW_BYPASS
        undefaction: APPFW_BLOCK
        sessiontimeout: "1000"
        learnratelimit: "500"
        sessionlifetime: "2000"
        sessioncookiename: cookie_name
        clientiploggingheader: header_name
        importsizelimit: "268435456"
        signatureautoupdate: on
        signatureurl: http://signature.url
        cookiepostencryptprefix: prepend
        logmalformedreq: on
        geolocationlogging: on
        ceflogging: on
        entitydecoding: on
        useconfigurablesecretkey: on
        sessionlimit: "10000"


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
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
