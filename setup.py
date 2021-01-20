# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in procuremonkey/__init__.py
from procuremonkey import __version__ as version

setup(
	name='procuremonkey',
	version=version,
	description='A simple app to expedite the E5a ordering prcocess.',
	author='Martin Bieker',
	author_email='martin.bieker@udo.edu',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
