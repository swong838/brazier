import os
from setuptools import setup

setup(
	name='brazier',
	version='0.0.1',
	author='Scott Wong',
	author_email='swong@digitalchemy.net',
	description=(
		'Fun project to screw around with a Raspberry Pi Zero W'
		'and a high powered RGB LED'),
	license='BSD',
	packages=['brazier', 'tests']
)
