Using generic Ansible modules
#############################

The Citrix ADC Ansible modules try to accomodate the
most frequently changing items of the ADC configuration.
Things that change from day to day operations.

In this section we investigate how to leverage Ansible standard
modules to configure Citrix ADC to cover the cases where the user
needs to use Ansible for a ADC configuration entity that
does not have a specialized Ansible module.

We make use of the Ansible uri module mainly to issue NITRO API
requests to Citrix ADC.

The solutions we present here do have drawbacks compared to the use
of specialized Citrix ADC Ansbile modules, such as not having a check mode
operation, having to check for NITRO errors and handle them accordingly,
and also having to account for particularities that a configuration entity may have.

All these issues are taken care of in the Citrix ADC specific modules but in the solutions
we present here the user has to deal with all of these.

References
==========

NITRO API reference
~~~~~~~~~~~~~~~~~~~
https://developer-docs.citrix.com/projects/citrix-adc-nitro-api-reference/en/latest/
