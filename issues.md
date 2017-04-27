# Known issues with netscaler ansible modules


## netscaler cs action

*  "targetvserver". Requires sslvpn feature which is unavailable in CPX

### Read write options missing from module arguments

* "targetvsever". Option is not supported in cpx and could not be tested
* "newname". Renaming function is not supported 


## netscaler cs policy

* "logaction". Could not configure a valid log action to test this argument
* "newname". Renaming function is not supported 

## netscaler cs vserver

* "sitedomainttl". Value is not correctly set. It remains 0 regardless at what value it is set.
* "cookietimeout". Value is not correctly set. It remains 0 regardless at what value it is set.
* "cookiedomain". Missing from nitro response object.
* "backupip". Missing from nitro response object.
* "ttl". Value is not correctly set. It remains 0.0 regardless at what value it is set.
* "domainname". Missing from nitro response object
* "targettype". Attribute is missing from nitro response object.
* "persistenceid". Attribute is missing from nitro response object.
* "state". Attribute is missing from nitro response object.
* "backupvserver". Could not instantiate a valid backup vserver in CPX testbed. Got "nitro exception errorcode=258,message=No such resource [backupVServer, backup-server]"
*  "listenpriority". Could not give a valid value. Got  "nitro exception errorcode=1354,message=Error in binding listen priority to normal vserver"
* "newname". Renaming function is not supported 

## netscaler lb monitor

* "metric". Could not setup snmp parameters for test.
* "metrictable". Could not setup snmp parameters for test.
* "metricthreshold". Could not setup snmp parameters for test.
* "metricweight". Could not setup snmp parameters for test.
* "hostname". Cannot set value properly.
* "kcdaccount". Could not setup kcd account to test parameter.
* "sslprofile". Not supported by nitro config object.
* "servicename". Set through binding object.
* "servicegroupname". Set through binding object.

## netscaler lb vserver

* "rule". Missing from nitro response object.
* "resrule". Missing from nitro response object.
* "state". Missing from nitro response object.
* "backupvserver". Could not set up backup vserver.
* "persistavpno". Missing from nitro response object.
* "td". Could not configure traffic domain.
* "lbprofilename". There is no configuration object for lb profile.
* "redirectfromport". Attribute not supported by the nitro object.
* "httpsredirecturl". Attribute not supported by the nitro object.
* "weight". Set through bindings.
* "servicename". Set through bindings
* "redirurlflags". Attribute not supported by the nitro object.
* "newname". Renaming function is not supported 

## netscaler service

* "pathmonitor". Requires clustering not supported with CPX testbed
* "pathmonitorindv". Requires clustering not supported with CPX testbed
* "serverid". Missing from nitro response. Value is set with attribute "customserverid"
* "state". Missing from nitro response object.
* "td". Could not configure traffic domain.
* "weight". Missing from nitro response object.
* "monitor\_name\_svc". Missing from nitro response object
* "riseapbrstatsmsgcode". Not set according to value. Remains 0.
* "delay". Not set according to value. Remains 0.
* "all". Missing from nitro response object.
* "Internal". Missing from nitro response object.
* "servername". Could not setup server for test
* "monconnectionclose". Attribute not supported by nitro config object.
* "newname". Rename function is not supported

## netscaler servicegroup

* "td". Could not configure traffic domain.
* "servername". Could not setup server for test
* "port". Set through members bindings.
* "weight". Set through members bindings.
* "customserverid". Could not setup CPX for testing this attribute.
* "serverid". Could not setup CPX for testing this attribute.
* "hashid". Could not setup CPX for testing this attribute.
* "monitor\_name\_svc". Attribute not present in nitro config object.
* "dup\_weight". Attribute not present in nitro config object.
* "riseapbrstatsmsgcode". Fails to set value.
* "delay". Fails to set value.
* "includemembers". Fails to set value.
* "newname". Rename function is not supported
* "monconnectionclose". Attribute not supported by nitro config object.

## netscaler ssl certkey

* "nodomaincheck". Not in the nitro response object.
* "bundle". Not in the nitro response object.
* "linkcertkeyname". Not in the nitro response object.
* "hsmkey". Did not have hardware module to test.
* "fipskey". Did not have hardware module to test.
