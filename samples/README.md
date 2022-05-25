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
