:orphan:

.. _citrix_adm_get_bearer_token_module:

citrix_adm_get_bearer_token - Generate Citrix cloud bearer token
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Generate Citrix cloud bearer token




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - api_client_id

        *(str)*
      -
      - Id of API client
    * - api_client_secret

        *(str)*
      -
      - Secret of API client
    * - customer_id

        *(str)*
      -
      - Customer id for which to generate token
    * - endpoint

        *(str)*
      -
      - API endpoint for bearer token

        Can be any of the following

        api-ap-s.cloud.com

        api-eu.cloud.com

        api-us.cloud.com



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Get Citrix cloud bearer token
      delegate_to: localhost
      register: login_result
      citrix.adm.citrix_adm_get_bearer_token:
        customer_id: "{{ customer_id }}"
        api_client_id: "{{ api_client_id }}"
        api_client_secret: "{{ api_client_secret }}"
        endpoint: api-eu.cloud.com


Return Values
-------------
.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Key
      - Returned
      - Description
    * - access_token

        *(str)*
      - success
      - Bearer token

        **Sample:**

        eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2l
