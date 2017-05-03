#!/usr/bin/python

import tempfile
import urllib
import os.path
import tarfile
import subprocess

tempdir  = tempfile.mkdtemp()
print('Saving all files under directory %s' % tempdir)


print('Downloading nitro sdk tarball')
toplevel_tarball = os.path.join(tempdir, 'ns-11.0-65.31-sdk.tar.gz')
urllib.urlretrieve('http://downloadns.citrix.com.edgesuite.net/11872/ns-11.0-65.31-sdk.tar.gz', toplevel_tarball)

def unpack_tarball(tar_archive, member):
    tarball = os.path.join(tempdir, tar_archive)
    with tarfile.open(tarball, 'r') as tar:
        member = tar.getmember(member)
        tar.extractall(tempdir, members=[member])

print('Unpacking top level tarball')
unpack_tarball('ns-11.0-65.31-sdk.tar.gz', 'ns-11.0-65.31-nitro-python.tgz')

print('Unpacking python tarball')
unpack_tarball('ns-11.0-65.31-nitro-python.tgz', 'ns_nitro-python_ion_65_31.tar')

print('Unpacking sdk')
with tarfile.open(os.path.join(tempdir, 'ns_nitro-python_ion_65_31.tar'), 'r') as tar:
    tar.extractall(path=tempdir)

print('Running python sdk install script')
os.chdir(os.path.join(tempdir,'nitro-python-1.0'))
subprocess.check_call(['python', 'setup.py', 'install'])

print('Install complete. You may remove left over files under %s' % tempdir)
