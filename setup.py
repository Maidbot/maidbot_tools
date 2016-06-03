#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['maidbot_tools', 'maidbot_tools.commands'],
    package_dir={'': 'src'},
    scripts=['scripts/maid']
)

setup(**d)
