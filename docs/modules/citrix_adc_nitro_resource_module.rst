:orphan:

.. _citrix_adc_nitro_resource_module:

citrix_adc_nitro_resource - Manage NITRO resources
++++++++++++++++++++++++++++++++++++++++++++++++++

.. versionadded:: 2.9.1

.. contents::
   :local:
   :depth: 2

Synopsis
--------
- Manage NITRO resources
- Implements full lifecycle of nitro resource.




Parameters
----------

.. list-table::
    :widths: 10 10 60
    :header-rows: 1

    * - Parameter
      - Choices/Defaults
      - Comment
    * - resource
      -
      - Dictionary containing the resource attributes

        Contents of the dictionary differ depending on which specific NITRO object is configured.
    * - state
      - Choices:

          - present
          - absent
      - state of the resource
    * - workflow

        *(str)*
      -
      - Workflow options

        .. list-table::
            :widths: 10 10 60
            :header-rows: 1

            * - Suboption
              - Choices/Defaults
              - Comment

            * - allow_recreate
              -
              - Whether to allow deletion and recreation of the resource

                Relevant only for the object lifecycle
            * - delete_id_attributes
              -
              - Attributes list which identify the resource uniquely when deleting
            * - endpoint
              -
              - NITRO endpoint for the object
            * - lifecycle
              - Choices:

                  - object
                  - binding
                  - bindings_list
                  - non_updateable_object
              - Describe the lifecycle type of this object

                The lifecyle value determines how the resource will be identified as existing or non existing whether the attributes of the object need to be updated if existing and how to create and delete a particular object.
            * - non_updateable_attributes

                *(list)*
              -
              - Non updateable attributes
            * - primary_id_attribute
              -
              - Primary id attribute
            * - resource_missing_errorcode
              -
              - NITRO response code that is returned when the resource cannot be retrieved




Examples
--------

.. code-block:: yaml+jinja
    


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
