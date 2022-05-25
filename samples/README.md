# Running the examples
Generally:

```
ansible-playbook  -i inventory.txt   <playbook yml>
```
# Specifying the ip / login / password of the NetScaler
This can be done in two ways: in the inventory file, or inline inside the playbook. What is in the playbook will take precedence over the inventory file


## The inventory file
The inventory file is where you can specify the IP / login / password of a NetScaler. For example, if you are running a NetScaler CPX on the same host where you are executing the playbook:

```
$ docker port cpx 80
32773

$ cat inventory.txt
[netscaler]
127.0.0.1 nsip=127.0.0.1:32773 nitro_user=nsroot nitro_pass=nsroot validate_certs=no

$ cat lb_vserver.yml

      local_action: 
        nsip: "{{ nsip }}"
        nitro_user: "{{ nitro_user }}"
        nitro_pass: "{{ nitro_pass }}"
```

## In the playbook

```
      local_action: 
        nsip: 127.0.0.1:32773
        nitro_user: nsroot
        nitro_pass: nsroot
```

## Samples directory contents

| ADC Use Case | Configuration Examples |
| ------------ | ---------------------- |
| Web Application Firewall (WAF) | appfw\_signatures\_custom\_import <br /> appfw\_confidfield <br /> appfw\_fieldtype <br /> appfw\_global\_bindings <br /> appfw\_htmlerrorpage <br /> appfw\_jsoncontenttype <br /> appfw\_learningdata\_delete <br /> appfw\_learningdata\_export <br /> appfw\_learningdata\_get <br /> appfw\_learningdata\_reset <br /> appfw\_learningsettings <br /> appfw\_policy <br /> appfw\_policylabel <br /> appfw\_profile <br /> appfw\_settings <br /> appfw\_signatures <br /> appfw\_wsdl <br /> appfw\_xmlcontenttype <br /> appfw\_xmlerrorpage <br /> appfw\_xmlschema <br /> |
| Core ADC features | citrix\_adc\_servicegroup\_dsapi <br /> save\_conifg\_handler\_server <br /> server <br /> server2 <br /> service <br /> servicegroup <br /> servicegroup2 <br /> |
| Content Switching | content\_switch\_ssl\_lb\_mon <br /> cs\_action <br /> cs\_action\_expr <br /> cs\_vserver <br /> cs\_vserver\_appfw\_policy\_setup <br /> |
| DNS | dnsnsrec <br /> dnssoarec <br /> |
| Global Load Server Balancing (GSLB) | gslb\_basic <br /> gslb\_full <br /> gslb\_service <br /> gslb\_service\_disable <br /> gslb\_site <br /> gslb\_vserver <br /> |
| ADM Proxy Calls | proxied\_server |
| Generic Module nitro\_info | nitro\_info <br /> |
| Generic Module nitro\_request | adc\_login <br /> add\_or\_update\_server <br /> add\_or\_update\_simpleacl <br /> add\_server\_idempotent <br /> count <br /> delete <br /> delete\_all\_cs\_vsevers <br /> delete\_by\_args <br /> delete\_simpleacl <br /> do\_action <br /> enable\_feature <br /> get <br /> get\_all <br /> get\_by\_args <br /> get\_filtered <br /> log <br /> mas\_get\_all <br /> mas\_login <br /> rename <br /> save\_config <br /> switch\_partition <br /> uri-nitro-api-calls <br /> |
| Generic Module nitro\_resource | create\_and\_disable\_server <br /> object <br /> object\_by\_args <br /> object\_with\_bindings <br /> object\_with\_bindings\_list <br /> parameter\_object <br /> |
| NS | nsip <br /> nspartition <br /> nspartition\_switch <br /> |
| SSL A+ certified | ssl-aplus-certified-via-citrix-adc |
| SSL | ssl\_certkey <br /> sslcipherlist <br /> sslprofile\_sslcipher\_binding <br /> sslvserver\_sslcertkey\_binding <br /> sslvserver\_sslcipher\_binding <br /> |
| System | system\_file |
| Various | password\_reset <br /> citrix\_adc\_connection\_plugin <br /> |


| ADM Use Case | Configuration Examples |
| ------------ | ---------------------- |
| ADM resources | citrix\_adm\_application <br /> citrix\_adm\_configuration\_template\_facts <br /> citrix\_adm\_dns\_domain\_entry <br /> citrix\_adm\_login <br /> citrix\_adm\_managed\_device <br /> citrix\_adm\_mps\_agent\_facts <br /> citrix\_adm\_mps\_datacenter\_facts <br /> citrix\_adm\_mpsgroup <br /> citrix\_adm\_mpsuser <br /> citrix\_adm\_ns\_device\_profile <br /> citrix\_adm\_ns\_facts <br /> citrix\_adm\_poll\_instances <br /> citrix\_adm\_provision\_vpx <br /> citrix\_adm\_rba\_policy <br /> citrix\_adm\_rba\_policy\_full <br /> citrix\_adm\_rba\_role <br /> citrix\_adm\_service\_login <br /> citrix\_adm\_service\_logout <br /> citrix\_adm\_stylebook <br /> citrix\_adm\_stylebook\_lookup <br /> citrix\_adm\_tenant\_facts <br /> |
