#!/usr/bin/python

import sys
import os.path
import shutil



def main():
    try:
        import ansible
    except ImportError:
        print('Could not load ansible module')
        sys.exit(1)

    # Find ansible installation path
    ansible_path = os.path.dirname(os.path.abspath(os.path.realpath(ansible.__file__)))

    # Check to see if appropriate directories exist
    module_utils_path = os.path.join(ansible_path, 'module_utils')
    if not os.path.exists(module_utils_path):
        print('Module utils directory (%s) does not exist' % module_utils_path)
        sys.exit(1)
    if not os.path.isdir(module_utils_path):
        print('Module utils path (%s) is not a directory' % module_utils_path)
        sys.exit(1)

    extra_modules_path = os.path.join(ansible_path, 'modules', 'extras')
    if not os.path.exists(module_utils_path):
        print('Extra modules directory (%s) does not exist' % extra_modules_path)
        sys.exit(1)
    if not os.path.isdir(module_utils_path):
        print('Extra modules path (%s) is not a directory' % extra_modules_path)
        sys.exit(1)

    here = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
    ansible_modules_sourcedir = os.path.join(here, 'ansible-modules')

    # Collect files to copy
    ansible_module_files = []
    for filename in os.listdir(ansible_modules_sourcedir):
        if filename.endswith('.py'):
            ansible_module_files.append(filename)

    # Copy netscaler.py to module_utils
    if not 'netscaler.py' in ansible_module_files:
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
        #print('Copying %s to %s' % (file, netscaler_module_dir))
        source = os.path.join(ansible_modules_sourcedir, file)
        destination = os.path.join(netscaler_module_dir, file)
        if os.path.exists(destination):
            print('Overwriting %s' % destination)
        else:
            print('Copying %s' % destination)
        shutil.copy(source, destination)





if __name__ == '__main__':
    main()
