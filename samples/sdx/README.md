## Provision VPX on a SDX through ADM service

This playbook replicates the functionality of provisioning a VPX on a SDX through ADM service.

The manual procedure is to go to ADM GUI and select menu item Infrastructure -> Instances -> Citrix ADC.
Then select the SDX tab under which there should at least exist one SDX instance select that instance and
select from the "Select Action" drop down box "Provision VPX".

For the playbook to run you need to first generate an API client secret from the
IAM -> API access page.

This will be used in the playbook to generate the Authentication Bearer token which will be
used to authenticate subsequent module invocation to the ADM service.

The playbook also utilizes some facts modules to get information needed for the VPX provisioning
in a more user friendly way.

The facts we collect are about the datacenter to get its id, the configuration template to select an
initial configuration job for the newly created VPX and the ADM agent to get its id.

All these facts are used in the citrix\_adm\_provision\_vpx module.
In this module we define the provisioning profile along with the nitro data to
pass to the SDX for creating the VPX.

The nitro data are specific to the SDX appliance and should be reviewed to correspond to what the
actual SDX instance expects.
One way to do this is to run the operation manually one time and through the web browser developer
utilities record the exact POST data used.
Then the user can modify them to its liking for subsequent automatic runs.
