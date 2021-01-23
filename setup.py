# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
import os


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


def take_package_name(name):
    if name.startswith("-e"):
        return name[name.find("=")+1:name.rfind("-")]
    else:
        return name.strip()

def load_requires_from_file(filepath):
    with open(filepath) as fp:
        return [take_package_name(pkg_name) for pkg_name in fp.readlines()]


setup(
    name='lazmodn3-instagram-type',
    version='1.0.0',
    description='parse instagram api __a response',
    long_description=readme,
    author='lazmond3',
    author_email='moikilo00@gmail.com',
    url='https://github.com/lazmond3/pylib-instagram-type.git',
    install_requires=["lazmond3-pylib-debug"],
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
