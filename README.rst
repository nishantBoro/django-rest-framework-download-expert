Django rest framework Download Expert
=====================================

This module shows a simple way to serve files for download in django rest framework using Apache module Xsendfile.

It also has an additional feature of serving downloads only to users belonging to a particular group. This feature might 
be useful for developers trying to give certain features to a group of users only.For example, a site where users belong to 
either a 'Premium' or 'Free' group. Apache modules like mod_ratelimit can be installed to limit download speed for users
belonging to 'Free' group.

To use this package in production make sure you have:

* Apache web server installed with Mod WSGI configured

* Apache module Xsendfile installed and configured

Installation
------------

Install dependencies:

.. code-block:: python

    virtualenv <env-name>
    source <env_name>/bin/activate
    pip install requirements.txt


Configuration
-------------

Include the path to your directory containing the file(s) which needs to be served for download by adding the following field in settings.py:

.. code-block:: python

    ...
    SERVE_FILES_FROM = '/home/<user>/<project-name>/<folder-name>/' # just an example location on your remote server. The <folder-name> could be anywhere on the server. However, I recommend keeping it somewhere inside your 'home/<user>/<project-name>/' directory.


**Setup your urls.py with some URL's:**


