#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='python-spark',
      version='0.1',
      url='https://github.com/alexcrawley/python-spark-api',
      author="Alex Crawley",
      description="API wrapper for Spark Cloud REST services",
      long_description=open('README.rst').read(),
      keywords="",
      license='BSD',
      packages=find_packages(exclude=['tests*']),
      include_package_data=True,
      install_requires=[
          'requests',
          'purl>=0.8',
      ],
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          'Development Status :: 1 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: Unix',
          'Programming Language :: Python']
      )