import os
from distutils.core import setup

setup(
    name = 'django-ensembl',
    version = '0.01',
    description = 'Ensembl models for Django',
    author = 'James Casbon',
    author_email = 'casbon@gmail.com',
    url = '',
    packages = ['ensembl'],
    data_files = [],
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific'],
)
