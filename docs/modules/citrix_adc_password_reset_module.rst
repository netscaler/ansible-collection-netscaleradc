:orphan:

.. _citrix_adc_password_reset_module:

citrix_adc_password_reset - Perform default password reset.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Perform default password reset.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - new_password

        *(str)*
      -
      - New password for target ADC
    * - nitro_protocol

        *(str)*
      - Choices:

          - http
          - https
      - Which protocol to use when accessing the nitro API objects.
    * - nsip

        *(str)*
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - password

        *(str)*
      -
      - Default password of target ADC
    * - username

        *(str)*
      -
      - Username we want to reset password for
    * - validate_certs

        *(bool)*
      -
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Password reset
      delegate_to: localhost
      citrix_adc_password_reset:
        nsip: 10.10.11.2
        username: nsroot
        nitro_protocol: https
        validate_certs: no
        password: nsroot
        new_password: verysecret


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

        Non zero nitro errorcode 278
