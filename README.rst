Package
===================================
django-admin-timeline

Description
===================================
A Facebook-like timeline app for Django admin. It's very similar to built-in feature `Daily progress`, but then
has a nicer templates and infinite scroll implemented. Actions are broken up by day, then by action. Filtering
by user (multiple select) and content type (multiple select) is implemented.

Prerequisites
===================================
- Django 1.5.+
- Python 2.7.+, 3.3.+

Installation
===================================
1. Install in your virtual environemnt

Latest stable version from PyPI:

    $ pip install django-admin-timeline

Latest stable version from bitbucket:

    $ pip install -e hg+http://bitbucket.org/barseghyanartur/django-admin-timeline@stable#egg=django-admin-timeline

Latest stable version from github:

    $ pip install -e git+https://github.com/barseghyanartur/django-admin-timeline@stable#egg=django-admin-timeline

3. Add `admin_timeline` to your `INSTALLED_APPS` in the global settings.py.

>>> INSTALLED_APPS = (
>>>     # ...
>>>     'admin_timeline',
>>>     # ...
>>> )

4. Collect the static files by running (see the Troubleshooting section in case of problems):

    $ ./manage.py collectstatic

5. Override app settings in your global `settings` module (see the ``apps.admin_timeline.defaults`` for the list of
   settings). As for now, most important of those is ``NUMBER_OF_ENTRIES_PER_PAGE`` - number of entries displayer per
   page (for both non-AJAX and AJAX requests).

6. Add the following lines to the global ``urls`` module:

>>> # Admin timeline URLs. Should be placed BEFORE the Django admin URLs.
>>> (r'^admin/timeline/', include('admin_timeline.urls')),
>>> url(r'^admin/', include(admin.site.urls)),

Troubleshooting
===================================
If somehow static files are not collected properly (missing admin_timeline.js and admin_timeline.css files), install
the latest stable version from source.

    $ pip install -e hg+http://bitbucket.org/barseghyanartur/django-admin-timeline@stable#egg=django-admin-timeline

Usage
===================================
After following all installation steps, you should  be able to access the admin-timeline by:

    http://127.0.0.1:8000/admin/timeline/

An example application is available. See the http://bitbucket.org/barseghyanartur/django-admin-timeline/src
(example directory).

License
===================================
GPL 2.0/LGPL 2.1

Support
===================================
For any issues contact me at the e-mail given in the `Author` section.

Author
===================================
Artur Barseghyan <artur.barseghyan@gmail.com>
