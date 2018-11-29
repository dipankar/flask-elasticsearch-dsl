"""
Flask-ElasticSearch-dsl
-------------

Flask plugin that enables elasticsearch-dsl
"""
from setuptools import setup


setup(
    name='Flask-ElasticSearch-dsl',
    version='1.0',
    url='http://example.com/flask_elasticsearch-dsl/',
    license='BSD',
    author='Dipankar Sarkar',
    author_email='dipankarsarkar@gmail.com',
    description='Flask plugin to enable elasticsearch-dsl',
    long_description=__doc__,
    py_modules=['flask_elasticsearch-dsl'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'elasticsearch-dsl'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

