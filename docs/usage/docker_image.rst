Netscaler ansible docker image
##############################

To make the running of netscaler ansible modules easier a ready
to run image exists which does not require
any software packages installed on the host other than the docker engine.

It is suitable for running quickly and easily simple playbooks that are using
ansible modules and core ansible modules.

The image is not suitable for running any arbitraty ansible playbook since
many non core modules require extra dependencies which this docker
image does not have installed.

Installation
~~~~~~~~~~~~

The installation is quite simple.

.. code-block:: bash

    docker pull giorgosnikolopoulos/netscaler-ansible:latest

Usage
~~~~~

The entrypoint of the docker image is the ``ansible-playbook`` command.

This means that it can be used as drop in replacement of this command.

Running

.. code-block:: bash

    docker run --rm giorgosnikolopoulos/netscaler-ansible:latest

Will output the help for the command ``ansible-playbook``

To run a playbook we need to map a directory of the host to a directory
of the docker container so that the inventory and playbook files are
accessible from inside the docker container.

So provided we have in the current directory an inventory file and a playbook
by running the following

.. code-block:: bash

    docker run --rm -v $(pwd):/pwd giorgosnikolopoulos/netscaler-ansible -i inventory playbook.yml

The playbook will be executed.

Of course the container needs to have also access to the NetScaler
node being configured otherwise the execution will fail.


Example
~~~~~~~

Following is an example of how to use the container along
with a NetScaler CPX deployment.

We will use ``docker-compose`` to setup our testbed using the following
compose ``docker-compose.yaml`` file.

.. code-block:: yaml

    version: '2'

    services:
      cpx:
        image: giorgosnikolopoulos/cpx:12.0-41.22
        ports:
          - '22'
          - '80'
          - '443'
          - '161'
        environment:
          EULA: 'yes'
        ulimits:
          core: -1
        tty: true
        stdin_open: true
        privileged: true

      netscaler-ansible:
        image: giorgosnikolopoulos/netscaler-ansible:latest
        tty: true
        stdin_open: true
        volumes:
          - .:/pwd
        links:
          - cpx

Note that in addition to instantiating the cpx and netscaler-ansible
containers we also map the current directory to the working directory
of the netscaler-ansible container and we also create a link to the cpx
container.

This has the effect that the host's current directory is exposed as it is
inside the docker container and that there is a network reference to the
cpx container which can be used instead of the ip address of the container.

For our example we will use the following ``inventory.txt`` file.

.. code-block:: ini

    [netscaler]

    netscaler_cpx nsip=cpx nitro_user=nsroot nitro_pass=nsroot

For our sample playbook we will use the following ``play.yaml``

.. code-block:: yaml

    ---

    - hosts: netscaler
      gather_facts: false

      tasks:
        - name: lb vserver
          delegate_to: localhost
          netscaler_lb_vserver:
            nsip: "{{ nsip }}"
            nitro_user: "{{ nitro_user }}"
            nitro_pass: "{{ nitro_pass }}"


            name: lb-vserver-1
            servicetype: HTTP
            ipv46: 6.92.2.2
            port: 80

        - name: cs action
          delegate_to: localhost
          netscaler_cs_action:
            nsip: "{{ nsip }}"
            nitro_user: "{{ nitro_user }}"
            nitro_pass: "{{ nitro_pass }}"

            name: action1
            targetlbvserver: lb-vserver-1

These files are located in the same directory as the ``docker-compose.yaml``
file.

First we bring the containers up.

.. code-block:: bash

    docker-compose up -d

Verify that the containers are setup by running


.. code-block:: bash

    docker-compose ps

You should see that the cpx container is up and running
and that the netscaler-ansible container has exited.

From this point on we can use the ``docker-compose run netscaler-ansible`` command
to run our playbooks.

To run the sample playbook run:

.. code-block:: bash

    docker-compose run netscaler-ansible -i inventory.txt play.yaml

You should see the output of the playbook run just as if you had
run ``ansible-playbook`` normally.

Any valid ``ansible-playbook`` option can be passed on the command line to
the ``netscaler-ansible`` container.

When you no longer need the testbed you can tear it down by running:

.. code-block:: bash

    docker-compose stop
    docker-compose rm
