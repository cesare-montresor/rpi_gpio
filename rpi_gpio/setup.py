#!/usr/bin/env python
import os

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_reqs(*fns):
    lst = []
    for fn in fns:
        for package in open(os.path.join(CURRENT_DIR, fn)).readlines():
            package = package.strip()
            if not package:
                continue
            lst.append(package.strip())
    return lst
    
d = generate_distutils_setup(
    version='0.0.1',
    packages=['rpi_gpio'],
    package_dir={'': 'src'},
    install_requires=get_reqs('pip-requirements.txt'),
)

setup(**d)
