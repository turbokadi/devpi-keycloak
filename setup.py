#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__author__ = 'MoJoh <cryptoweirdo@protonmail.com>'

def get_version(path):
    fn = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        path, "__init__.py")
    with open(fn) as f:
        for line in f:
            if '__version__' in line:
                parts = line.split("=")
                return parts[1].split("'")[1]

setup(
    name='devpi-keycloak',
    version=get_version('devpi_keycloak'),
    author='MoJoh',
    author_email='cryptoweirdo@protonmail.com',
    license='MIT',
    url='http://github.com/turbokadi/devpi-keycloak',
    keywords='devpi keycloak auth module',
    description='Devpi plugin to auth via Keycloak SSO service',
    long_description=open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.rst')), 'r').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Intended Audience :: System Administrators",
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet'
    ],
    packages=['devpi_keycloak'],
    entry_points={
        'devpi_server': [
            "devpi-keycloak = devpi_keycloak.main"]},
    install_requires=[
        'devpi-server>=4.0.0',
        'keycloak-basic>=1.2.1'
    ],
    platforms='any',
)