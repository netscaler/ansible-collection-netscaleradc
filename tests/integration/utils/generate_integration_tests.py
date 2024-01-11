import os

from jinja2 import Template

HERE = os.path.dirname(os.path.abspath(__file__))


def generate_yaml(module_name, module_specific_params, template_str):
    template = Template(template_str)
    yaml_content = template.render(
        module_name=module_name,
        nsip="{{ nsip }}",
        nitro_user="{{ nitro_user }}",
        nitro_pass="{{ nitro_pass }}",
        nitro_protocol="{{ nitro_protocol }}",
        validate_certs="{{ validate_certs }}",
        save_config="{{ save_config }}",
        module_specific_params=module_specific_params,
    )

    return yaml_content


def read_template_str(filename):
    with open(filename, "r") as template_file:
        return template_file.read()


def generate_tasks_main_yaml(module_name, module_specific_params):
    template_str = read_template_str(
        HERE + os.sep + "integration_test_tasks_main_yaml.j2"
    )
    yaml_content = generate_yaml(module_name, module_specific_params, template_str)
    return yaml_content


def main(module_name, module_specific_params):
    tasks_main_yaml = generate_tasks_main_yaml(module_name, module_specific_params)

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
        aliases_file.write("gather_facts: no\n")


if __name__ == "__main__":
    module_name = "ntpserver"
    module_specific_params = {
        "servername": "pool.ntp.org",
        "preferredntpserver": '"YES"',
    }
    main(module_name, module_specific_params)
