=====================
django-admin-timeline
=====================
A Facebook-like timeline app for Django admin. It's very similar to built-in
feature `Daily progress`, but then has a nicer templates and infinite scroll
implemented. Actions are broken up by day, then by action. Filtering
by user (multiple select) and content type (multiple select) is implemented.

Prerequisites
=============
Present
-------
Starting from ``django-admin-timeline`` 1.7:

- Django 1.8, 1.9, 1.10
- Python 2.7, 3.4, 3.5

Past
----
Current version of ``django-admin-timeline`` (1.6) has the following
prerequisites:

- Django 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10
- Python >=2.6.8, 2.7, 3.3, 3.4, 3.5

Dropping support of Django 1.4, 1.5, 1.6 and 1.7 has been announced in
version 1.6. As of 1.6 everything is still backwards compatible with
versions 1.4, 1.5, 1.6 and 1.7, but in future versions compatibility with
these versions will be wiped out.

Dropping support of Python 2.6 and 3.3 has been announced in version 1.6.
As of 1.6 everything is still backwards compatible with Python 2.6 and 3.3,
but in future versions compatibility with these versions will be wiped out.

Installation
============
1. Install in your virtual environment

Latest stable version from PyPI:

.. code-block:: sh

    pip install django-admin-timeline

Latest stable version from bitbucket:

.. code-block:: sh

    pip install -e hg+http://bitbucket.org/barseghyanartur/django-admin-timeline@stable#egg=django-admin-timeline

Latest stable version from github:

.. code-block:: sh

    pip install https://github.com/barseghyanartur/django-admin-timeline/archive/stable.tar.gz

3. Add ``admin_timeline`` to your ``INSTALLED_APPS`` in the
   global ``settings.py``.

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'admin_timeline',
       # ...
    )

4. Collect the static files by running (see the Troubleshooting section in
   case of problems):

.. code-block:: sh

    ./manage.py collectstatic

5. Override app settings in your global `settings` module (see the
   ``apps.admin_timeline.defaults`` for the list of settings). As for now, most
   important of those is ``NUMBER_OF_ENTRIES_PER_PAGE`` - number of entries
   displayed per page (for both non-AJAX and AJAX requests).

6. Add the following lines to the global ``urls`` module:

.. code-block:: python

    # Admin timeline URLs. Should be placed BEFORE the Django admin URLs.
    (r'^admin/timeline/', include('admin_timeline.urls')),
    url(r'^admin/', include(admin.site.urls)),

Demo
====
Live demo
---------
See the `live demo app
<https://django-admin-timeline.herokuapp.com/admin/timeline/>`_ on Heroku.

Credentials:

- username: admin
- password: test

Run demo locally
----------------
In order to be able to quickly evaluate the ``django-admin-timeline``, a demo
app (with a quick installer) has been created (works on Ubuntu/Debian, may
work on other Linux systems as well, although not guaranteed). Follow the
instructions below for having the demo running within a minute.

Grab the latest ``django_admin_timeline_example_app_installer.sh``:

.. code-block:: sh

    wget https://raw.github.com/barseghyanartur/django-admin-timeline/stable/example/django_admin_timeline_example_app_installer.sh

Assign execute rights to the installer and run the
``django_admin_timeline_example_app_installer.sh``:

.. code-block:: sh

    chmod +x django_admin_timeline_example_app_installer.sh

    ./django_admin_timeline_example_app_installer.sh

Open your browser and test the app.

- URL: http://127.0.0.1:8001/admin/timeline/
- Admin username: admin
- Admin password: test

If quick installer doesn't work for you, see the manual steps on running the
`example project
<https://github.com/barseghyanartur/django-admin-timeline/tree/stable/example>`_.

Troubleshooting
===============
If somehow static files are not collected properly (missing admin_timeline.js
and admin_timeline.css files), install the latest stable version from source.

.. code-block:: sh

    $ pip install -e hg+http://bitbucket.org/barseghyanartur/django-admin-timeline@stable#egg=django-admin-timeline

Usage
=====
After following all installation steps, you should  be able to access the
``django-admin-timeline`` by:

    http://127.0.0.1:8000/admin/timeline/

An example application is available. See the following directory:

https://github.com/barseghyanartur/django-admin-timeline/tree/stable/example

License
=======
GPL 2.0/LGPL 2.1

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
