#!/usr/bin/bash python
import sys
import os
import subprocess
import json
from pip._internal.operations.freeze import freeze
import yaml

pakage = []

for i in freeze():
	pakage.append(i)


def jsonfile():
    file = open("report.json", "w")
    p = json.dumps({
        "Version": sys.version[:5],
        "Virtual environment": sys.prefix,
        "python executable location": sys.executable,
        "Pip location": os.popen('which pip').read()[:-1],
        "Python path": sys.base_prefix,
        "Installed packages: name, version": str(pakage)
        }, indent=4)
    file.write(p)
    file.close()


def yamlfile():
    p = dict(
        Version=str(sys.version[:5]),
        Virtual_environment=str(sys.prefix),
        python_executable_location=str(sys.executable),
        Pip_location="12",
        Python_path=sys.prefix,
        Installed_packages_name_version=pakage)
    with open('data.yml', 'w') as outfile:
        yaml.dump(p, outfile, default_flow_style=False)


jsonfile()
yamlfile()



