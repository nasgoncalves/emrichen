#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='emrichen',
    version='0.0.1',
    description='YAML preprocessor',
    long_description='',
    license='MIT',
    author='Santtu Pajukanta',
    author_email='santtu@pajukanta.fi',
    url='http://github.com/japsu/emrichen',
    packages = find_packages(exclude=["tests"]),
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'emrichen = emrichen.__main__:main',
        ]
    },
    install_requires=["PyYAML", "pyaml"],
    tests_require=["pytest"],
    setup_requires=["pytest-runner"],
)
