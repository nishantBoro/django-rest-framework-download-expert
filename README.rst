Django rest framework Download Expert
=====================================

.. image:: https://badge.fury.io/py/django-rest-framework-download-expert.svg
    :target: https://badge.fury.io/py/django-rest-framework-download-expert

This module provides a simple way to serve files for download in django rest framework using Apache module Xsendfile.

It also has an additional feature of serving downloads only to users belonging to a particular group. This feature might 
be useful for developers trying to give certain features to a group of users only.For example, a site where users belong to 
either a 'Premium' or 'Free' group. Apache modules like mod_ratelimit can be installed to limit download speed for users
belonging to 'Free' group.

To use this package in production make sure you have:

* Apache web server installed with Mod WSGI configured

* Apache module Xsendfile installed and configured

Installation
------------

Install with pip:

.. code-block:: python

    pip install django-rest-framework-download-expert


Add the following app to your `INSTALLED_APPS`

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'download_expert',
    )


Configuration
-------------

Include the path to your directory containing the file(s) which needs to be served for download by adding the following field in settings.py:

.. code-block:: python

    ...
    SERVE_FILES_FROM = '/home/<user>/<project-name>/<folder-name>/' # just an example location on your remote server. The <folder-name> could be anywhere on the server. However, I recommend keeping it somewhere inside your 'home/<user>/<project-name>/' directory.


**Setup your urls.py with some URL's:**

The file(s) would be available for download by sending requests to this url's.
For example,

.. code-block:: python

    ...
    from django.urls import re_path
    from . import views

    urlpatterns = [
        ...
        re_path(r'^downloads/$', views.Downloads.as_view(), name='downloads'), # mandatory to put $ at the end of the url
    ]
    
**Setup your views.py:**

For example,

.. code-block:: python

    from rest_framework.permissions import IsAuthenticated
    from rest_framework.views import APIView
    from download_expert.permissions import IsGroupUser
    from download_expert.xsendfile import base_xsendfile
    
    
    class Downloads(APIView):

        permission_classes = (IsAuthenticated, IsGroupUser,) # optional attribute. This module can work with any 3rd party authentication module
        group_name = 'some_group' 

        def get(self, request):
            response = base_xsendfile(request)
            return response

* permission_classes can set to IsGroupUser to allow only users belonging to a particular group to download the file. This lookup group can be set by defining an attribute 'group_name' in the view class. The module will look for the group name defined in 'group_name' attribute and check if the requested user belongs to this group.

**Making requests for a file:**

This package uses query string URL's to serve a particular file for download.
The two queries available are: 'name' and'type'.
For example, if we define a pattern re_path(r'^downloads/$', views.Downloads.as_view(), name='downloads'),  in the urls.py,
and make a GET request http://site-name.com/downloads/?name=some_file&type=rar , the module will check if this file exists in the
directory defined in settings.py(SERVE_FILES_FROM attribute) and if its true, the file we be served for download.

Of course, the view will throw a permission error if the user doesn't have the permissions defined in permission_classes.

Best example use of this module:
--------------------------------

Let's say there are two groups, 'Premium' and 'Free'. We want to allow users belonging to 'Premium' group to download files at
full speed but those belonging to 'Free' group should be limited to a certain download speed.

**urls.py:**

.. code-block:: python

    ...
    from django.urls import re_path
    from . import views

    urlpatterns = [
    ...
    re_path(r'^downloads/p/$', views.PremiumUser.as_view(), name='premium'),
    re_path(r'^downloads/f/$', views.FreeUser.as_view(), name='free'),
    ]

**views.py:**

.. code-block:: python

    from rest_framework.permissions import IsAuthenticated
    from rest_framework.views import APIView
    from download_expert.permissions import IsGroupUser
    from download_expert.xsendfile import base_xsendfile


    class PremiumUser(APIView):

        permission_classes = (IsAuthenticated, IsGroupUser,)
        group_name = 'Premium'

        def get(self, request):
            response = base_xsendfile(request)
            return response


    class FreeUser(APIView):
        permission_classes = (IsAuthenticated, IsGroupUser)
        group_name = 'Free'

        def get(self, request):
            response = base_xsendfile(request)
            return response

Now  install the apache module mod_ratelimit and configure it to set download speed limit for the url ending with: '../downloads/f/'.
When an user belonging to 'Free' group makes a GET request to http://site-name.com/downloads/f/?name=some_file&type=rar ,
the user experiences a slower download speed. And when the same user tries to access http://site-name.com/downloads/p/?name=some_file&type=rar the request is denied cause the user is not a 'Premium' Group member.
