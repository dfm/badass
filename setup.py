#!/usr/bin/env python

import os
import sys
from setuptools import setup

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name="badass",
    version="3.12159",
    author="Dan Foreman-Mackey",
    author_email="danfm@nyu.edu",
    url="https://github.com/dfm/badass",
    py_modules=["badass"],
    description="Betterize your Python.",
    long_description=open("README.rst").read(),
    package_data={"": ["README.rst", "LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
