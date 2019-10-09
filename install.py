#!/usr/bin/python
#
# Copyright (c) 2017 Citrix Systems
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import os.path
import shutil
import re


def main():
    try:
        import ansible
    except ImportError:
        print('Could not load ansible module')
        sys.exit(1)

    # Parse ansible version
    m = re.match(r'^(\d)\.(\d+).*$', ansible.__version__)
    if m is None:
        raise Exception('Cannot parse ansible version')

    major = int(m.group(1))
    minor = int(m.group(2))

    # Find ansible installation path
    ansible_path = os.path.dirname(os.path.abspath(os.path.realpath(ansible.__file__)))
    print('Ansible path is %s' % ansible_path)

    # Check to see if appropriate directories exist
    if (major, minor) == (2, 4):
        module_utils_path = os.path.join(ansible_path, 'module_utils')
    else:
        module_utils_path = os.path.join(ansible_path, 'module_utils', 'network', 'netscaler')
    if not os.path.exists(module_utils_path):
        print('Module utils directory (%s) does not exist' % module_utils_path)
        sys.exit(1)
    if not os.path.isdir(module_utils_path):
        print('Module utils path (%s) is not a directory' % module_utils_path)
        sys.exit(1)

    # Set modules path according to ansible version
    if major < 2 or major == 2 and minor <= 2:
        extra_modules_path = os.path.join(ansible_path, 'modules', 'extras', 'network')
    else:
        extra_modules_path = os.path.join(ansible_path, 'modules', 'network')

    if not os.path.exists(extra_modules_path):
        print('Extra modules directory (%s) does not exist' % extra_modules_path)
        sys.exit(1)
    print('Ansible extras path is %s' % extra_modules_path)

    if not os.path.isdir(extra_modules_path):
        print('Extra modules path (%s) is not a directory' % extra_modules_path)
        sys.exit(1)


    # Initialize needed paths
    here = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
    ansible_modules_sourcedir = os.path.join(here, 'ansible-modules')


    if not os.path.exists(module_utils_path):
        print('Documentation fragments directory (%s) does not exist' % document_fragments_path)
        sys.exit(1)
    if not os.path.isdir(module_utils_path):
        print('Documentation fragments directory (%s) is not a directory' % document_fragments_path)
        sys.exit(1)


    # Copy documentation fragments
    document_fragments_paths = [
        os.path.join(ansible_path, 'utils', 'module_docs_fragments'),
        os.path.join(ansible_path, 'plugins', 'doc_fragments'),
    ]

    for document_fragments_path in document_fragments_paths:
        if os.path.exists(document_fragments_path) and os.path.isdir(document_fragments_path):
            print('Copying documentation fragments to %s' % document_fragments_path)
            shutil.copy(os.path.join(here, 'documentation_fragments', 'netscaler.py'), os.path.join(document_fragments_path, 'netscaler.py'))
            break
    else:
        print("Warning could not find installation path for document fragments. This is not crucial for correct module operation.")

    # Collect files to copy
    ansible_module_files = []
    for filename in os.listdir(ansible_modules_sourcedir):
        if filename.endswith('.py'):
            ansible_module_files.append(filename)

    # Copy netscaler.py to module_utils
    if 'netscaler.py' not in ansible_module_files:
        print('Could not find netscaler module utils file')
        sys.exit(1)

    print('Copying netscaler.py to %s' % module_utils_path)
    shutil.copy(os.path.join(ansible_modules_sourcedir, 'netscaler.py'), os.path.join(module_utils_path, 'netscaler.py'))

    ansible_module_files.remove('netscaler.py')

    # Make netscaler module directory
    netscaler_module_dir = os.path.join(extra_modules_path, 'netscaler')
    if not os.path.exists(netscaler_module_dir):
        print('Creating directory %s' % netscaler_module_dir)
        os.mkdir(netscaler_module_dir)

    # Copy module files
    for file in ansible_module_files:
        # print('Copying %s to %s' % (file, netscaler_module_dir))
        source = os.path.join(ansible_modules_sourcedir, file)
        destination = os.path.join(netscaler_module_dir, file)
        if os.path.exists(destination):
            print('Overwriting %s' % destination)
        else:
            print('Copying %s' % destination)
        shutil.copy(source, destination)

    # Try to find the units test directory
    # and copy our units tests to the appropriate directory
    unit_tests_dir = os.path.join(ansible_path, '..', '..', 'test', 'units')
    if os.path.exists(unit_tests_dir):
        print('Found unit tests dir under %s' % unit_tests_dir)
        netscaler_unit_tests_dir = os.path.join(unit_tests_dir, 'modules', 'network', 'netscaler')
        if os.path.exists(netscaler_unit_tests_dir):
            print('Cleaning up previous netscaler tests')
            shutil.rmtree(netscaler_unit_tests_dir)
        os.mkdir(netscaler_unit_tests_dir)

        local_units_dir = os.path.join(here, 'test', 'units')
        for file in os.listdir(local_units_dir):
            if not file.endswith('.py'):
                continue
            print('Copying unit test file %s' % file)
            shutil.copy(
                src=os.path.join(local_units_dir, file),
                dst=os.path.join(netscaler_unit_tests_dir, file)
            )
    else:
        print('Warning. Could not install unit tests. You will not be able to run the unit tests for the modules.')
        print('This does not affect normal module functionality.')

    # Install connection plugin

    print('Installing Citrix ADC connection plugin')
    install_path = os.path.join(ansible_path, 'plugins', 'connection')
    source_file = os.path.join(here, 'ansible-plugins', 'ssh_citrix_adc.py')
    shutil.copy(source_file, install_path)


if __name__ == '__main__':
    main()
