import pyaml
import oyaml as yaml
import os


def create_directory(dir_path, nested=False):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path) if not nested else os.makedirs(dir_path)


def yamlstr_to_yaml(output_yamlfile, yamlstr):
    with open(output_yamlfile, 'w') as fw:
        load_data = yaml.load(yamlstr)
        yaml_data = pyaml.dump(load_data)
        fw.write(yaml_data)


def python_to_yaml(output_yamlfile, pydata):
    with open(output_yamlfile, 'w') as fw:
        yaml_data = pyaml.dump(pydata)
        fw.write(yaml_data)
