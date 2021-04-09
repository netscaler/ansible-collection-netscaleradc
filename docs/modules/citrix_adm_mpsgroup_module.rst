:orphan:

.. _citrix_adm_mpsgroup_module:

citrix_adm_mpsgroup - Manage Citrix ADM user groups.
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 1.0.0

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage Citrix ADM user groups.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - allow_application_only

        *(bool)*
      -
      - Checks if only application centic page is needed.
    * - application_names

        *(list)*
      -
      - All Application names that are part of this group.This includes selected appnames as well as which are result of defined regex.
    * - apply_all_bound_entities

        *(bool)*
      -
      - Apply for all bound entities (TRUE|FALSE).
    * - assign_all_apps

        *(bool)*
      -
      - Assign All Applications (YES|NO).
    * - assign_all_autoscale_groups

        *(bool)*
      -
      - Assign All Autoscale groups (YES|NO).
    * - assign_all_devices

        *(bool)*
      -
      - Assign All Instances (YES|NO).
    * - assign_all_selected_device_apps

        *(bool)*
      -
      - Assign All Application from selected instances (YES|NO).
    * - authscope_props

        *(list)*
      -
      - Authorized Scope Properties.
    * - autoscale_groups_id

        *(list)*
      -
      - Autoscale groups belong to this groupp.
    * - bound_entity_selected

        *(str)*
      -
      - Which bound entiy is selected VSERVER(0),SERVICE(1),SERVICEGROUP(2),SERVER(3).
    * - description

        *(str)*
      -
      - Description of Group.

         Minimum length =  1

         Maximum length =  1024
    * - enable_session_timeout

        *(bool)*
      -
      - Enables session timeout for group.
    * - id

        *(str)*
      -
      - Id is system generated key for all the system groups.
    * - instance_ip

        *(str)*

        *(added in 2.6.0)*
      -
      - The target Netscaler instance ip address to which all underlying NITRO API calls will be proxied to.

        It is meaningful only when having set ``mas_proxy_call`` to ``true``
    * - mas_proxy_call

        *(bool)*

        *(added in 2.6.0)*
      - Default:

        *False*
      - If true the underlying NITRO API calls made by the module will be proxied through a Citrix ADM node to the target Netscaler instance.

        When true you must also define the following options: ``nitro_auth_token``, ``instance_ip``.
    * - name

        *(str)*
      -
      - Group Name.

         Minimum length =  1

         Maximum length =  64
    * - nitro_auth_token

        *(str)*

        *(added in 2.6.0)*
      -
      - The authentication token provided by a login operation.
    * - nitro_pass

        *(str)*
      -
      - The password with which to authenticate to the netscaler node.
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
      - Time in seconds until a timeout error is thrown when establishing a new session with Netscaler
    * - nitro_user

        *(str)*
      -
      - The username with which to authenticate to the netscaler node.
    * - nsip

        *(str)*
      -
      - The ip address of the netscaler appliance where the nitro API calls will be made.

        The port can be specified with the colon (:). E.g. 192.168.1.1:555.
    * - permission

        *(str)*
      -
      - Permission for the group (admin/read-only).

         Minimum length =  1

         Maximum length =  128
    * - role

        *(str)*
      -
      - Role (admin|nonadmin).
    * - roles

        *(list)*
      -
      - Roles assigned to the group.
    * - save_config

        *(bool)*
      - Default:

        *True*
      - If true the module will save the configuration on the netscaler node if it makes any changes.

        The module will not save the configuration on the netscaler node if it made no changes.
    * - select_individual_entity

        *(bool)*
      -
      - Select Individual Entity Type.
    * - session_timeout

        *(str)*
      -
      - Session timeout for the Group.
    * - session_timeout_unit

        *(str)*
      -
      - Session timeout unit for the Group.
    * - standalone_instances_id

        *(list)*
      -
      - Stand alone instances belong to this groupp.
    * - state

        *(str)*
      - Choices:

          - present (*default*)
          - absent
      - The state of the resource being configured by the module on the netscaler node.

        When present the resource will be created if needed and configured according to the module's parameters.

        When absent the resource will be deleted from the netscaler node.
    * - tenant_id

        *(str)*
      -
      - Id of the tenant.

         Minimum length =  1

         Maximum length =  128
    * - users

        *(list)*
      -
      - Users belong to the group.
    * - validate_certs

        *(bool)*
      - Default:

        *yes*
      - If ``no``, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.



Examples
--------

.. code-block:: yaml+jinja
    
    - name: Setup mpsuser
      delegate_to: localhost
      citrix_adm_mpsgroup:
        mas_ip: 192.168.1.1
        mas_user: nsroot
        mas_pass: nsroot
    
        state: present
    
        name: test_mpsgroup
        permission: read-only
        allow_application_only: true
        session_timeout: 10
        session_timeout_unit: Minutes
        description: some description
        assign_all_apps: true
        enable_session_timeout: true
        assign_all_devices: false
        role: admin
        roles:
          - admin
        application_names_without_regex: []
        application_names: []
        application_names_with_regex: []
        standalone_instances_id: []


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
    * - mpsgroup

        *(dict)*
      - success
      - Dictionary containing the attributes of the created mpsgroup
    * - msg

        *(str)*
      - failure
      - Message detailing the failure reason

        **Sample:**

        Action does not exist
