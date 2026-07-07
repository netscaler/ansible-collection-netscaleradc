import argparse
import copy
import os
import sys

from jinja2 import Template

HERE = os.path.dirname(os.path.abspath(__file__))

# Map from field name patterns (in readwrite_arguments) to the prerequisite resource
# that must be created before the test resource can be added.
PREREQ_MAP = {
    "vservername": {
        "resource": "lbvserver",
        "state": "present",
        "params": {
            "name": "test_prereq_lb",
            "servicetype": "HTTP",
            "ipv46": "192.0.2.10",
            "port": 80,
        },
    },
    "servicegroupname": {
        "resource": "servicegroup",
        "state": "present",
        "params": {
            "servicegroupname": "test_prereq_sg",
            "servicetype": "HTTP",
        },
    },
    "servicename": {
        "resource": "service",
        "state": "present",
        "params": {
            "name": "test_prereq_svc",
            "ipaddress": "192.0.2.1",
            "port": 80,
            "servicetype": "HTTP",
        },
    },
    "sslprofile": {
        "resource": "sslprofile",
        "state": "present",
        "params": {
            "name": "test_prereq_sslprofile",
        },
    },
    "lbprofilename": {
        "resource": "lbprofile",
        "state": "present",
        "params": {
            "lbprofilename": "test_prereq_lbprofile",
        },
    },
    "netprofile": {
        "resource": "netprofile",
        "state": "present",
        "params": {
            "name": "test_prereq_netprofile",
        },
    },
}

CREDS = """\
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    nitro_protocol: "{{ nitro_protocol }}"
    validate_certs: "{{ validate_certs }}"
    save_config: "{{ save_config }}\""""


def _render_task(task_name, resource, state, params):
    lines = [f"- name: {task_name}"]
    lines.append("  delegate_to: localhost")
    lines.append(f"  netscaler.adc.{resource}:")
    lines.append(f"    nsip: \"{{{{ nsip }}}}\"")
    lines.append(f"    nitro_user: \"{{{{ nitro_user }}}}\"")
    lines.append(f"    nitro_pass: \"{{{{ nitro_pass }}}}\"")
    lines.append(f"    nitro_protocol: \"{{{{ nitro_protocol }}}}\"")
    lines.append(f"    validate_certs: \"{{{{ validate_certs }}}}\"")
    lines.append(f"    save_config: \"{{{{ save_config }}}}\"")
    lines.append(f"    state: {state}")
    for k, v in params.items():
        if isinstance(v, str):
            lines.append(f"    {k}: {v}")
        else:
            lines.append(f"    {k}: {v}")
    return "\n".join(lines)


def infer_prerequisites(readwrite_arguments):
    """Return ordered list of prerequisite dicts inferred from resource field names."""
    seen = set()
    prereqs = []
    for field_name in readwrite_arguments:
        if field_name in PREREQ_MAP and field_name not in seen:
            seen.add(field_name)
            prereqs.append(PREREQ_MAP[field_name])
    return prereqs


def generate_setup_yaml(prereqs):
    """Render tasks/setup.yaml content from a list of prerequisite dicts."""
    if not prereqs:
        return None
    lines = ["---"]
    for prereq in prereqs:
        task = _render_task(
            f"Setup | Create {prereq['resource']}",
            prereq["resource"],
            prereq["state"],
            prereq["params"],
        )
        lines.append(task)
    return "\n".join(lines) + "\n"


def generate_teardown_yaml(prereqs):
    """Render tasks/teardown.yaml content (prereqs in reverse order, state: absent)."""
    if not prereqs:
        return None
    lines = ["---"]
    for prereq in reversed(prereqs):
        absent_params = {k: v for k, v in prereq["params"].items()}
        task = _render_task(
            f"Teardown | Delete {prereq['resource']}",
            prereq["resource"],
            "absent",
            absent_params,
        )
        lines.append(task)
    return "\n".join(lines) + "\n"


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

    # Strip trailing whitespace from every line and ensure file ends with a newline.
    yaml_content = "\n".join(line.rstrip() for line in yaml_content.splitlines()) + "\n"

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


def main(module_name, module_specific_params, bindings, readwrite_arguments=None, with_setup=False):
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

    # write target_dir/aliases
    with open(target_dir + os.sep + "aliases", "w") as aliases_file:
        aliases_file.write("gather_facts/no\n")
        aliases_file.write("netscaler/cpx/\n")
        aliases_file.write("netscaler/vpx/\n")

    # optionally generate setup.yaml and teardown.yaml from inferred prerequisites
    if with_setup and readwrite_arguments:
        prereqs = infer_prerequisites(readwrite_arguments)
        setup_content = generate_setup_yaml(prereqs)
        teardown_content = generate_teardown_yaml(prereqs)
        if setup_content:
            with open(target_tasks_dir + os.sep + "setup.yaml", "w") as f:
                f.write(setup_content)
            with open(target_tasks_dir + os.sep + "teardown.yaml", "w") as f:
                f.write(teardown_content)
            print(f"Generated setup.yaml and teardown.yaml for {len(prereqs)} prerequisite(s).")
        else:
            print("No prerequisites detected; skipping setup.yaml / teardown.yaml.")

    print(f"Generated test target: tests/integration/targets/{module_name}/")


def _cli_main():
    """CLI entry point: generate test scaffolding for a resource from the NITRO_RESOURCE_MAP."""
    parser = argparse.ArgumentParser(
        description="Generate integration test scaffolding for a netscaler.adc module."
    )
    parser.add_argument("--resource", required=True, help="Resource name (e.g. authorizationaction)")
    parser.add_argument("--setup", action="store_true", help="Also generate setup.yaml / teardown.yaml")
    args = parser.parse_args()

    # Load NITRO_RESOURCE_MAP dynamically
    map_path = os.path.join(HERE, "..", "..", "..", "plugins", "module_utils", "nitro_resource_map.py")
    map_path = os.path.abspath(map_path)
    namespace = {}
    with open(map_path) as f:
        exec(compile(f.read(), map_path, "exec"), namespace)  # nosec: B102
    resource_map = namespace.get("NITRO_RESOURCE_MAP", {})

    if args.resource not in resource_map:
        print(f"ERROR: '{args.resource}' not found in NITRO_RESOURCE_MAP. Add the map entry first.", file=sys.stderr)
        sys.exit(1)

    entry = resource_map[args.resource]
    primary_key = entry.get("primary_key", "name")

    # Build minimal module_specific_params from primary key
    module_specific_params = {}
    if primary_key:
        module_specific_params[primary_key] = f"test_{args.resource}"

    bindings = {}
    for b in entry.get("bindings", []):
        bindings[b] = {
            "mode": "desired",
            "binding_members": [],
        }

    main(
        module_name=args.resource,
        module_specific_params=module_specific_params,
        bindings=bindings if bindings else None,
        readwrite_arguments=entry.get("readwrite_arguments", {}),
        with_setup=args.setup,
    )


if __name__ == "__main__":
    # If called with --resource flag, use the CLI entry point.
    # Otherwise run the original hardcoded example.
    if "--resource" in sys.argv:
        _cli_main()
    else:
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
