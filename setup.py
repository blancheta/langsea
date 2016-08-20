#!/usr/bin/ebv python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import langsea

setup(
	name='langsea',
	version=langsea.__version__,
	packages=find_packages(),
	author="Alexandre Blanchet",
	author_email="alexandreblanchet44@gmail.com",
	description="Help to use the Langsea API in your Python script",
	long_description=open('README.rst').read(),
	include_package_data=True,
	install_requires=[
		'markdown',
	],
	url='http://github.com/blancheta/langsea',
	classifiers=[
		"Programming Language :: Python",
		"Development Status :: 1 - Base",
		"License :: OSI Approved",
		"Natural Language :: French",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.4",
		"Topic :: Communications, Visual language",
	],
	license="WTFPL",
)
