import os

from setuptools import find_packages, setup

setup(
    name='import_monster',
    packages=find_packages(exclude=('tests', )),
    python_requires='~=3.7',
    install_requires=parse_requirements(),
)