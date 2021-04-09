import setuptools


def parse_requirements() -> tuple:
    """Parse requirements.txt for install_requires"""
    requirements = read('requirements.txt')
    return tuple(requirements.split('\n'))


setuptools.setup(
    name='project_test',
    packages=setuptools.find_packages(exclude=('tests', )),
    python_requires='~=3.7',
    install_requires=parse_requirements(),
)