#!/usr/bin/bash python
from setuptools import setup, find_packages

setup(
    name='monitor',
    packages=find_packages(),
    version="1.0",
    author="Siarhei Barysevich",
    author_email="siarhei_barysevich@epam.com",
    description="app for monitoring system info",
    license="MIT",
    install_requires=['psutil==5.6.3'],
    package_data={'monitor': ['config.ini'],},
    include_package_data=True
    )
