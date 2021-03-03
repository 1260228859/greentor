# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
setup(
    name="greentor",
    version="0.1",
    packages=find_packages(),
    install_requires=['greenlet'],
    author="Timmy",
    author_email="zhu327@gmail.com",
    description="Greenlet support to tornado. inspired by motor and gevent",
    license="MIT",
    keywords="tornado Greenlet async",
    url="https://github.com/zhu327/greentor", )
