import copy
import os

from jinja2 import Template

HERE = os.path.dirname(os.path.abspath(__file__))


def generate_yaml(module_name, module_specific_params, bindings, template_str):
    total_bindings = {}
    if bindings:
        total_bindings["desired"] = copy.deepcopy(bindings)
        # change the mode in bindings to unbind and store it in total_bindings["unbind"]
        total_bindings["unbind"] = copy.deepcopy(bindings)
        for key in total_bindings["unbind"]:
            total_bindings["unbind"][key]["mode"] = "unbind"
        total_bindings["unbind"] = copy.deepcopy(bindings)
        for key in total_bindings["unbind"]:
            total_bindings["unbind"][key]["mode"] = "unbind"
        total_bindings["bind"] = copy.deepcopy(bindings)
        for key in total_bindings["bind"]:
            total_bindings["bind"][key]["mode"] = "bind"

    template = Template(template_str)
    yaml_content = template.render(  # nosec: B106
        module_name=module_name,
        nsip="{{ nsip }}",
        nitro_user="{{ nitro_user }}",
        nitro_pass="{{ nitro_pass }}",
        nitro_protocol="{{ nitro_protocol }}",
        validate_certs="{{ validate_certs }}",
        save_config="{{ save_config }}",
        module_specific_params=module_specific_params,
        bindings=total_bindings,
    )

    return yaml_content


def read_template_str(filename):
    with open(filename, "r") as template_file:
        return template_file.read()


def generate_tasks_main_yaml(module_name, module_specific_params, bindings):
    if bindings:
        template_file = "integration_test_tasks_main_with_bindings_yaml.j2"
    else:
        template_file = "integration_test_tasks_main_yaml.j2"
    template_str = read_template_str(HERE + os.sep + template_file)
    yaml_content = generate_yaml(
        module_name, module_specific_params, bindings, template_str
    )
    return yaml_content


def main(module_name, module_specific_params, bindings):
    tasks_main_yaml = generate_tasks_main_yaml(
        module_name, module_specific_params, bindings
    )

    # mkdir -p HERE + ../targets/module_name/tasks
    target_dir = HERE + os.sep + ".." + os.sep + "targets" + os.sep + module_name
    target_tasks_dir = target_dir + os.sep + "tasks"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    if not os.path.exists(target_tasks_dir):
        os.makedirs(target_tasks_dir)

    # write tasks_main.yaml to target_dir + /main.yaml
    with open(target_tasks_dir + os.sep + "main.yaml", "w") as tasks_main_yaml_file:
        tasks_main_yaml_file.write(tasks_main_yaml)

    # write target_dir/aliases to target_dir/aliases and below is the content
    # abcdefghijklmnopqrstuvwxyz

    with open(target_dir + os.sep + "aliases", "w") as aliases_file:
        aliases_file.write("gather_facts/no\n")
        aliases_file.write("netscaler/cpx/\n")
        aliases_file.write("netscaler/vpx/\n")


if __name__ == "__main__":
    module_name = "lbvserver"
    module_specific_params = {
        "name": "lb1",
        "servicetype": "HTTP",
        "ipv46": "10.10.10.11",
        "port": "80",
        "lbmethod": "LEASTCONNECTION",
    }
    bindings = {
        "lbvserver_servicegroup_binding": {
            "mode": "desired",
            "binding_members": [
                {
                    "name": "lb1",
                    "servicename": "sg1",
                },
            ],
        },
        "lbvserver_service_binding": {
            "mode": "desired",
            "binding_members": [
                {
                    "name": "lb1",
                    "servicename": "s1",
                    "weight": 10,
                },
                {
                    "name": "lb1",
                    "servicename": "s2",
                    "weight": 20,
                },
            ],
        },
    }

    main(module_name, module_specific_params, bindings)
