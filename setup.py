from setuptools import find_packages, setup

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="ems-optim",
    version="0.1.5",
    description="Energy Management System Python library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ems-optim.readthedocs.io/",
    author="Energy Team",
    author_email="example@email.com",
    license="MIT",
    classifiers=[ # Tags for referencing on Pypi
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    #include_package_data=True,
    install_requires=["pandas","pyyaml","mysql-connector-python","mysqlclient"],
)