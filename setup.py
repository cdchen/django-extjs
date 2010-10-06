# -*- coding: utf-8 -*-


from setuptools import setup, find_packages, findall

setup(
    name='django-extjs',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    author='revolunet',
    url='http://github.com/revolunet/django-extjs',
)
