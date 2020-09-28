# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='my-leetcode-notes-python',
    version='0.1.0',
    description='leet code notes (python)',
    long_description=readme,
    author='leizh',
    author_email='leizh@gmail.com',
    url='https://github.com/leizhnxp/my-leetcode-notes-py.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

