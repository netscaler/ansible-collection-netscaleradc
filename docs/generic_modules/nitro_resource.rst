Using the citrix_adc_nitro_resource module
##########################################

The ``citrix_adc_nitro_resource`` module is a generic module
that implements the creation, update and deletion of NITRO API resources
in a generic manner.

It accepts the same parameters for connecting to ADC as the other modules.

Its two main parameters that determine what and how it will be configured
are ``workflow`` and ``resource``.

The ``workflow`` parameter will accept a dictionary that has several keys
which will differentiate the execution of the module.

The ``resource`` parameter is a dictionary with the attributes of the NITRO
resource being configured.

By providing different values for these parameters we can leverage the same
module to create a number of NITRO API resources without handling each
resource in its own specialized module.

Workflow explained
~~~~~~~~~~~~~~~~~~

The basis for this reusability is the fact that NITRO objects have enough similarities
in the operations they provide so that an algorithm can be applied to many endpoints
successfully just by adjusting some key values.

A sample workflow dictionary is shown below.

.. code-block:: yaml

          lbgroup_workflow:
            lifecycle: object
            endpoint: lbgroup
            primary_id_attribute: name
            resource_missing_errorcode: 258
            non_updateable_attributes:
              - newname


The most important parameter is ``lifecycle``.
This determines the main workflow which will be followed, slightly adjusted
by the rest of the parameters.

We provide a list of workflows for use with users' playbooks in our main github repository_.

.. _repository: https://github.com/citrix/citrix-adc-ansible-modules

Currently the following lifecycles are supported

- object
- binding
- bindings_list
- non_updateable_object

The following sections detail each type of lifecycle.

``object`` lifecycle
~~~~~~~~~~~~~~~~~~~~

The ``object`` lifecycle is usually relevant to NITRO objects
that can be created independent of other NITRO objects and have create,
update and delete operations.

An example definition is shown below

.. code-block:: yaml

          lbgroup_workflow:
            lifecycle: object
            endpoint: lbgroup
            primary_id_attribute: name
            resource_missing_errorcode: 258
            allow_recreate: true
            non_updateable_attributes:
              - newname

The  ``endpoint`` parameter defines part of the url that will be used.
``primary_id_attribute`` identifies which of the resource's attribute
is the one that uniquely identifies the object.
``resource_missing_errorcode`` is the NITRO error code we get when we try
to retrieve an object that does not exist. This is used to determine if
the object exists without the error code aborting execution of the module.
``non_updateable_attributes`` is a list of attributes that if they are part of
a PUT request will cause the request to fail.

``allow_recreate`` is a boolean parameter that determines what will happen
if a non updatable attribute differs. When it is ``true`` the object will be
deleted and recreated with the configured values.
If it is ``false`` then the module will fail execution warning about the attribute.

To further explain the execution of the module we will use the following
example.

.. code-block:: yaml

        - hosts: citrix_adc

          gather_facts: False
          vars_files:
            - workflows.yaml

          tasks:
            - name: Setup nitro resource lb group
              delegate_to: localhost
              citrix_adc_nitro_resource:
                nsip: "{{ nsip }}"
                nitro_user: "{{ nitro_user }}"
                nitro_pass: "{{ nitro_pass }}"
                state: present

                workflow:
                    lifecycle: object
                    endpoint: lbgroup
                    primary_id_attribute: name
                    resource_missing_errorcode: 258
                    allow_recreate: true
                    non_updateable_attributes:
                      - newname

                resource:
                  name: mylbgroup
                  timeout: 150


When the ``state`` is ``present`` the resource will be created or updated
if it already exists.

The existence of the resource is determined by the value of the ``name`` attribute
since it is the one identified by the ``primary_id_attribute`` parameter
of the workflow dictionary.

The equality of the existing object on ADC with the configured object present
in the playbook is determined by comparing all the attributes present in the
playbook.

If an object has more attributes than what is present in the playbook, defaults
are used as determined by the NITRO API on the target ADC.

So if in our example a lbgroup with the name ``mylbgroup`` does not exist it will
be created with the initial attributes set as shown.

If the lbgroup exists but the ``timeout`` parameter has a different value on the
target ADC then it will be updated.

Any other attributes the ``lbgroup`` NITRO object may have are not taken into account.

When the ``state`` parameter is set to ``absent`` then the object will either be deleted
if it already exists or there will be no NITRO call if it does not exist.

For the existence only the ``primary_id_attribute`` is checked.
So in our example if there exists a lbgroup with name ``mylbgroup`` it will be deleted.
In this case all other attribute values are irrelevant.

Idempotency and check mode
**************************

The ``citrix_adc_nitro_resource`` module tries to execute with idempotency
and also supports check mode.

Nevertheless there is a caveat with that statement.

Idempotency, and conversely correct operation of the check mode, depends
on the final values the NITRO object will have once configured on the target
ADC.

If for example numeric value is stored as string but in the playboook parameter
is given as an integer then subsequent runs of the same playbook will update the
object and report so in the cli output.

So in our previous example if the lbgroup ``timeout`` value is stored as a string
while it is defined as an integer the playbook execution will not be idempotent.

One way around this would be to coerce the value to be string like so

.. code-block:: yaml

          timeout: !!str 150

If you find you execute the same playbook but each time it reports updates then
running ``ansible-playbook``  with the ``-vvv`` option and looking at the output
will give you a clue as to what is going on under the hood.

You should see a debug message like the following.

.. code-block:: text

        "Attribute \"port\" differs. Playbook parameter: (<class 'str'>) 8080. Retrieved NITRO object: (<class 'int'>) 8080",

There may also be other reasons for idempotency failure.

Scanning through the detailed output of the playbook run will give clues as to
what was the difference that prompted an update.

``binding`` lifecycle
~~~~~~~~~~~~~~~~~~~~~

The ``binding`` lifecycle is usually relevant to NITRO objects
that implement bindings between two other NITRO objects.

These objects are the way the ``bind`` nscli commands are
implemented in NITRO API.

We will be using the following example for this section.


.. code-block:: yaml

    - name: Setup lbgroup lbvserver binding
      delegate_to: localhost
      citrix_adc_nitro_resource:
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
        state: "{{ state }}"

        workflow: 
          lifecycle: binding
          endpoint: lbgroup_lbvserver_binding
          bound_resource_missing_errorcode: 258
          primary_id_attribute: name
          delete_id_attributes:
            - vservername

        resource:
          name: mylbgroup
          vservername: resource-lb-vserver

The  ``endpoint`` parameter defines part of the url that will be used.
``bound_resource_missing_errorcode`` defines the NITRO error code that
will be returned when the bound object is not already configured.

As we said this type of object implement the ``bind`` nscli commands.
As in the ``bind`` command there is a main object that other object are
bound to.

In NITRO API when determining if the binding should be created we
retrieve a list of existing bindings from this main object.
This parameter value allows us to not abort execution when the main
object does not exist.

This is useful for the module when running in check mode and you want
to identify if the particular binding should be created.

If at the time of creation the main object still does not exist then
the module will fail.

``primary_id_attribute`` identifies the attribute that is used as the
main id for the binding. It is used to identify existence of a binding
object and retrieving the existing bindings from the main object.

``delete_id_attributes`` is a list of attributes that will be used
to identify the binding object as distinct from other bindings to
the same main object. The name comes from the fact that these attributes
must be present on the url when doing a DELETE operation.

To determine existence of a binding we compare the set of attribute
values for ``primary_id_attribute`` and ``delete_id_attributes`` that
are present in the resource dictionary.

It is a good practice to define as many of the ``delete_id_attributes`` for
the binding as possible since this will avoid falsely determining the existence
of a binding.

If we find that an existing binding has the same values for these attributes
then we mark the binding as existing.

For binding equality the process is the same as the ``object`` lifecycle.

We compare all the present attributes to the same attributes of the configured
object. If there is a mismatch in any of these we update the binding.
Note that ``binding`` objects do not have an update NITRO API operation, so
updating one means deleting the existing binding and recreating it with
the configured attributes.

For ``state`` ``absent`` we determine the existence as before and if we find
there is a configured binding on the target ADC we delete it.


``bindings_list`` lifecycle
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``bindings_list`` lifecycle is not a new kind of object
rather than an iteration on the ``binding`` lifecycle.

It accepts a list of bindings as a resource and then
tries to limit the bindings of the main object to that
exact list, deleting extraneous bindings, creating missing ones
and updating ones that are different.

We will be using the following example in explaining the operation

.. code-block:: yaml

      - name: Setup lbgroup lbvserver binding
        delegate_to: localhost
        citrix_adc_nitro_resource:
          nsip: "{{ nsip }}"
          nitro_user: "{{ nitro_user }}"
          nitro_pass: "{{ nitro_pass }}"
          state: "{{ state }}"

          workflow: 
            lifecycle: bindings_list
            binding_workflow: 
              lifecycle: binding
              endpoint: lbgroup_lbvserver_binding
              bound_resource_missing_errorcode: 258
              primary_id_attribute: name
              delete_id_attributes:
                - vservername

          resource:
            bindings_list:
              - name: mylbgroup
                vservername: resource-lb-vserver-1
              - name: mylbgroup
                vservername: resource-lb-vserver-2


As seen in the sample we have the workflow dictionary
slightly modified for this kind of lifecycle.

We set ``lifecycle`` to the ``bindings_list`` value and then
in the ``binding_workflow`` we provide the same dictionary
we would provide for a single ``binding`` lifecycle call.

In ``resource`` we provide the list of bindings in the ``bindings_list``
dictionary key.

Handling of the creation, update and deletion of each item in the list
is the same as if we were doing ``bidning`` lifecycle calls for each one.

The extra step is that the module in this lifecycle will first get
a list of existing bindings for the main object and then try to match
this list exactly to what we have in our configured list.


``non_updateable_object`` lifecycle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``non_updateable_object`` is a lifecycle similar
to the ``object`` lifecycle.

It applies to standalone NITRO API objects.
The main difference is that these objects do not have an
update NITRO operation so if an update is needed then
the object is first deleted and then recreated.

A sample playbook is shown below.

.. code-block:: yaml

      - name: Setup lbroute
        delegate_to: localhost
        citrix_adc_nitro_resource:
          nsip: "{{ nsip }}"
          nitro_user: "{{ nitro_user }}"
          nitro_pass: "{{ nitro_pass }}"
          state: "{{ state }}"

          workflow:
            lifecycle: non_updateable_object
            endpoint: lbroute
            primary_id_attribute: network
            resource_missing_errorcode: 258
            delete_id_attributes:
              - netmask
              - td

          resource:
            network: 193.168.1.0
            netmask: 255.255.255.0
            gatewayname: lbroute-gw-lbvserver


``primary_id_attribute`` is used to determine the existence of the object
in combination with ``delete_id_attributes``.
Existence is the same as in the ``binding`` lifecycle. That is
we gather all existing ``primary_id_attribute`` and ``delete_id_attributes`` values
we have in the playbook and compare them to the existing objects on the target ADC.

``endpoint`` identifies the NITRO object and part of the url used.

As noted previously there is no real update operation as in the ``object`` lifecycle.
An update is implemented by deleting and recreating the object.


Other operations
~~~~~~~~~~~~~~~~

The ``citrix_adc_nitro_resource`` module does not perform any other actions on resources.

For example you cannot use this module to disable a server on the target ADC.

For advanced scenarios where there is the need to manage a NITRO object with the ``citrix_adc_nitro_resource``
module and apply some other operations as well on the same object
we recommend using the ``citrix_adc_nitro_request`` module.
