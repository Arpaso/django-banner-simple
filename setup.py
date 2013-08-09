### -*- coding: utf-8 -*- ####################################################
"""
Configuration file used by setuptools. It creates 'egg', install all dependencies.
"""

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

#Dependencies - python eggs
install_requires = [
        'setuptools',
        'Django',
        'django-native-tags',
        'sorl-thumbnail >= 10.12',
]

#Execute function to handle setuptools functionality
setup(name="django-banner-simple",
    version="0.1",
    description="Simple banner system",
    long_description=read('README.rst'),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=True,
    install_requires=install_requires,
    author='Arpaso',
    author_email='arvid@arpaso.com',
    url='https://github.com/Arpaso/django-banner-simple',
    download_url='https://github.com/Arpaso/django-banner-simple/tarball/0.1',
    classifiers=(
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ),
)
