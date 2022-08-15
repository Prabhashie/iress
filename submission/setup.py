"""
file name:      setup.py
author:         Sachinthana Pathiranage
date created:   11/08/2022
purpose:        Setup package imports
version:        1.0
"""

# imports
from setuptools import setup, find_packages  

setup(name = 'utils', packages = find_packages())
setup(name = 'classes', packages = find_packages())
setup(name = 'src', packages = find_packages())