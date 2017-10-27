# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Gyfit Bot',
    version='0.0.0',
    description='Reddit bot that turns short youtube videos into gifs and posts them on gyfcat',
    long_description=readme,
    author=['Simon Chawla', 'Jack Arthur Harrhy'],
    author_email='chawblah@gmail.com',
    url='https://github.com/SimonChaw/Gyfit-Bot',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
