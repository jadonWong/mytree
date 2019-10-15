# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='mytree',
    version='1.0',
    description='one function achieves file tree',
    keywords='python tree directory',
    url='https://github.com/jadonWong/mytree',
    author='jadonWong',
    author_email='jdongwong@gmail.com',
    classifiers=[],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['docopt'],
    entry_points={
        'console_scripts':['mytree = bin.mytree:main']
    }
)