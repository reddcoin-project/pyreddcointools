#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pyreddcointools',
      version='1.1.42',
      description='Python Reddcoin Tools',
      author='Vitalik Buterin, John Nash',
      author_email='vbuterin@gmail.com, john@redd.ink',
      url='http://github.com/reddink/pyreddcointools',
      packages=['pyreddcointools'],
      scripts=['pybtctool'],
      include_package_data=True,
      data_files=[("", ["LICENSE"]), ("pyreddcointools", ["pyreddcointools/english.txt"])],
      )
