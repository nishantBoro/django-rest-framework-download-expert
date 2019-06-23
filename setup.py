import os
from setuptools import find_packages, setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rest-framework-download-expert',
    version='0.1',
    packages=find_packages(),
    license='MIT',  
    description="A simple tool to serve files for download in django-rest-framework using Apache module xsendfile"
    long_description=open('README.rst').read(),
    url='https://github.com/nishant-boro/django-rest-framework-download-expert',
    author='Nishant Boro',
    author_email='nishant4317@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
	install_requires=[
        'djangorestframework>=3.0.1',
    ],
	include_package_data=True,
    zip_safe=False,
)