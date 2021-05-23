#!/usr/bin/env python

from distutils.core import setup
from pkgutil import walk_packages

import govnsiblecli
def find_packages(path, prefix=""):
    yield prefix
    prefix = prefix + "."
    for _, name, ispkg in walk_packages(path, prefix):
        if ispkg:
            yield name

print(list(find_packages(govnsiblecli.__path__, govnsiblecli.__name__)),)

setup(
    name='Govnsible',
    version='0.1dev',
    packages=list(find_packages(govnsiblecli.__path__, govnsiblecli.__name__)),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    scripts=[
        'govnsible'
    ],
    long_description=open('README.md').read(),
)