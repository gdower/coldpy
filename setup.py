from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'coldpy', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='coldpy',
    version=version['__version__'],
    description='Python class for Catalogue of Life data packages',
    long_description=long_description,
    author='Geoff Ower',
    author_email='gdower@illinois.edu',
    url='https://github.com/gdower/coldpy',
    license='Apache-2.0',
    packages=['coldpy'],
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'],
    )
