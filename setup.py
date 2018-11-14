#!/usr/bin/env python

import os
from setuptools import setup

# load __version__
version_file = 'trimesh/version.py'
exec(open(version_file).read())

# load README.md as long_description
long_description = ''
if os.path.exists('README.md'):
    with open('README.md', 'r') as f:
        long_description = f.read()

# call the magical setuptools setup
setup(name='pypocketing',
      version=__version__,
      description='Generate 2D toolpaths from polygons',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Michael Dawson-Haggerty',
      author_email='mikedh@kerfed.com',
      license='MIT',
      url='http://github.com/mikedh/pypocketing',
      keywords='graphics mesh geometry 3D',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Natural Language :: English',
          'Topic :: Scientific/Engineering'],
      packages=['pocketing'],
      install_requires=['numpy',
                        'scipy',
                        'trimesh'],
      )
