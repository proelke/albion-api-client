"""A setuptools based setup module."""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='albion_api_client',
    version='0.1.0',
    description='An API client for Albion Online written in Python.',
    long_description=long_description,
    url='https://github.com/proelke/albion-api-client',
    author='Patrick Roelke',
    author_email='proelke@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='api ablion online',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
)