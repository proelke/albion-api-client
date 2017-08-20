"""A setuptools based setup module."""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='albion-api-client',
    version='0.1.1',
    description='An API client for Albion Online written in Python.',
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
    keywords=['api', 'ablion', 'online'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
)
