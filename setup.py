from setuptools import setup, find_packages
from os import path

import leancloud


here = path.abspath(path.dirname(__file__))

setup(
    name='leancloud-sdk',
    version=leancloud.__version__,
    description='LeanCloud Python SDK',

    url='https://leancloud.cn/',

    author='asaka',
    author_email='lan@leancloud.rocks',

    license='LGPL',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='Leancloud SDK',

    packages=find_packages(exclude=['docs', 'tests*']),

    test_suite='nose.collector',

    install_requires=[
        'arrow',
        'iso8601',
        'qiniu',
        'requests',
        'six',
        'werkzeug',
    ],

    extras_require={
        'dev': ['sphinx'],
        'test': ['nose', 'coverage', 'wsgi_intercept'],
    },
)
