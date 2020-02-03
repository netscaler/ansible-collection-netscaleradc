:orphan:

.. _citrix_adc_appfw_learningsettings_module:

citrix_adc_appfw_learningsettings - Configuration for learning settings resource.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.9

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Configuration for learning settings resource.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - contenttypeminthreshold

        *(str)*
      -
      - Minimum threshold to learn Content Type information.

        Minimum value = ``1``
    * - contenttypepercentthreshold

        *(str)*
      -
      - Minimum threshold in percent to learn Content Type information.

        Minimum value = ``0``

        Maximum value = ``100``
    * - cookieconsistencyminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn

        Minimum value = ``1``
    * - cookieconsistencypercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular cookie pattern for learning engine to learn that cookie.

        Minimum value = ``0``

        Maximum value = ``100``
    * - creditcardnumberminthreshold

        *(str)*
      -
      - Minimum threshold to learn Credit Card information.

        Minimum value = ``1``
    * - creditcardnumberpercentthreshold

        *(str)*
      -
      - Minimum threshold in percent to learn Credit Card information.

        Minimum value = ``0``

        Maximum value = ``100``
    * - crosssitescriptingautodeploygraceperiod

        *(str)*
      -
      - The number of minutes after the threshold hit alert the learned rule will be deployed.

        Minimum value = ``5``

        Maximum value = ``43200``
    * - crosssitescriptingminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn HTML scripting patterns.

        Minimum value = ``1``
    * - crosssitescriptingpercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular cross-site pattern for the learning engine to learn that cross-site scripting pattern.

        Minimum value = ``0``

        Maximum value = ``100``
    * - csrftagminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn request forgery (CSRF) tags.

        Minimum value = ``1``
    * - csrftagpercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular CSRF tag for the engine to learn that CSRF tag.

        Minimum value = ``0``

        Maximum value = ``100``
    * - fieldconsistencyminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn field information.

        Minimum value = ``1``
    * - fieldconsistencypercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular field consistency for the learning engine to learn that field consistency pattern.

        Minimum value = ``0``

        Maximum value = ``100``
    * - fieldformatautodeploygraceperiod

        *(str)*
      -
      - The number of minutes after the threshold hit alert the learned rule will be deployed.

        Minimum value = ``5``

        Maximum value = ``43200``
    * - fieldformatminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn field

        Minimum value = ``1``
    * - fieldformatpercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular web form field for the learning engine to recommend a field format for that form field.

        Minimum value = ``0``

        Maximum value = ``100``
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
    * - nsip
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - profilename

        *(str)*
      -
      - Name of the profile.

        Minimum length =  1
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - sqlinjectionautodeploygraceperiod

        *(str)*
      -
      - The number of minutes after the threshold hit alert the learned rule will be deployed.

        Minimum value = ``5``

        Maximum value = ``43200``
    * - sqlinjectionminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn HTML injection patterns.

        Minimum value = ``1``
    * - sqlinjectionpercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular HTML SQL injection for the learning engine to learn that HTML SQL injection pattern.

        Minimum value = ``0``

        Maximum value = ``100``
    * - starturlminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn start

        Minimum value = ``1``
    * - starturlpercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular start URL pattern the learning engine to learn that start URL.

        Minimum value = ``0``

        Maximum value = ``100``
    * - state
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - validate_certs
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.
    * - xmlattachmentminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn XML patterns.

        Minimum value = ``1``
    * - xmlattachmentpercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular XML attachment for the learning engine to learn that XML attachment pattern.

        Minimum value = ``0``

        Maximum value = ``100``
    * - xmlwsiminthreshold

        *(str)*
      -
      - Minimum number of application firewall sessions that the learning engine must observe to learn web interoperability (WSI) information.

        Minimum value = ``1``
    * - xmlwsipercentthreshold

        *(str)*
      -
      - Minimum percentage of application firewall sessions that must contain a particular pattern for the engine to learn a web services interoperability (WSI) pattern.

        Minimum value = ``0``

        Maximum value = ``100``



Examples
--------

.. code-block:: yaml+jinja
    
    - hosts: citrix_adc
    
      gather_facts: False
      tasks:
        - name: Setup learning settings
          delegate_to: localhost
          citrix_adc_appfw_learningsettings:
            nitro_user: nsroot
            nitro_pass: nsroot
            nsip: 192.168.1.2
            state: present
    
            profilename: test_profile
            starturlminthreshold: 100
            starturlpercentthreshold: 100
            cookieconsistencyminthreshold: 100
            cookieconsistencypercentthreshold: 100
            csrftagminthreshold: 100
            csrftagpercentthreshold: 100
            fieldconsistencyminthreshold: 100
            fieldconsistencypercentthreshold: 100
            crosssitescriptingminthreshold: 100
            crosssitescriptingpercentthreshold: 100
            sqlinjectionminthreshold: 100
            sqlinjectionpercentthreshold: 100
            fieldformatminthreshold: 100
            fieldformatpercentthreshold: 100
            creditcardnumberminthreshold: 100
            creditcardnumberpercentthreshold: 100
            contenttypeminthreshold: 100
            contenttypepercentthreshold: 100
            xmlwsiminthreshold: 100
            xmlwsipercentthreshold: 100
            xmlattachmentminthreshold: 100
            xmlattachmentpercentthreshold: 100


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
