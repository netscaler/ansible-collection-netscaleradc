Netscaler Ansible Docs
======================

This project implements a set of Ansible modules for the Citrix Netscaler.
Users of these modules can create, edit, update, and delete configuration
objects on a Netscaler. For more information on the basic principals that the
modules use, see the :doc:`usage/index`.

The code is licensed under the GPL and the authoritative repository is on
`github`_

.. _github: https://github.com/citrix/netscaler-ansible-modules

The main documentation for the modules is organized into several sections
listed below.

.. toctree::
   :maxdepth: 2
   :caption: User Documentation

   usage/getting_started
   usage/speeding_up_execution
   usage/rolling_upgrades
   usage/rolling_upgrades_vpx
   usage/citrix_adm_application_delays_explained

.. toctree::
   :maxdepth: 2
   :caption: Using generic ansible modules

   generic_modules/intro
   generic_modules/template_ns_conf
   generic_modules/nitro_api_calls
   generic_modules/nitro_resource

.. toctree::
   :maxdepth: 2
   :caption: Module Documentation

   general
   modules/list_of_all_modules
   modules/list_of_network_modules

.. toctree::
   :maxdepth: 2
   :caption: Developer Documentation

   development/development-utilities
