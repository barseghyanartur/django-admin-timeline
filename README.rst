=====================
django-admin-timeline
=====================
A Facebook-like timeline app for Django admin. It's very similar to built-in
feature `Daily progress`, but then has a nicer templates and infinite scroll
implemented. Actions are broken up by day, then by action. Filtering
by user (multiple select) and content type (multiple select) is implemented.

.. image:: https://img.shields.io/pypi/v/django-admin-timeline.svg
   :target: https://pypi.python.org/pypi/django-admin-timeline
   :alt: PyPI Version

.. image:: https://img.shields.io/travis/barseghyanartur/django-admin-timeline/master.svg
   :target: http://travis-ci.org/barseghyanartur/django-admin-timeline
   :alt: Build Status

.. image:: https://img.shields.io/badge/license-GPL--2.0--only%20OR%20LGPL--2.1--or--later-blue.svg
   :target: https://github.com/barseghyanartur/django-admin-timeline/#License
   :alt: GPL-2.0-only OR LGPL-2.1-or-later

Prerequisites
=============
Future
------
Starting from ``django-admin-timeline`` 1.7:

- Django 1.8, 1.9, 1.10, 1.11, 2.0, 2.1 and 2.2
- Python 2.7, 3.5, 3.6 and 3.7

Present
-------
Current version of ``django-admin-timeline`` (1.6.x) has the following
prerequisites:

- Django 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 2.0
- Python 2.7, 3.3, 3.4, 3.5, 3.6

Dropping support of Django 1.4, 1.5, 1.6 and 1.7 has been announced in
version 1.6. As of 1.6 everything is still backwards compatible with
versions 1.4, 1.5, 1.6 and 1.7, but in future versions compatibility with
these versions will be wiped out.

Dropping support of Python 2.6 and 3.3 has been announced in version 1.6.
As of 1.6 everything is still backwards compatible with Python 2.6 and 3.3,
but in future versions compatibility with these versions will be wiped out.

Installation
============
(1) Install in your virtual environment

    Latest stable version from PyPI:

    .. code-block:: sh

        pip install django-admin-timeline

    Latest stable version from BitBucket:

    .. code-block:: sh

        pip install https://bitbucket.org/barseghyanartur/django-admin-timeline/get/stable.tar.gz

    Latest stable version from GitHub:

    .. code-block:: sh

        pip install https://github.com/barseghyanartur/django-admin-timeline/archive/stable.tar.gz

(2) Add ``admin_timeline`` to your ``INSTALLED_APPS`` in the
    global ``settings.py``.

    .. code-block:: python

        INSTALLED_APPS = (
            # ...
            'admin_timeline',
           # ...
        )

(3) Collect the static files by running (see the Troubleshooting section in
    case of problems):

    .. code-block:: sh

        ./manage.py collectstatic

(4) Override app settings in your global ``settings`` module (see the
    ``apps.admin_timeline.defaults`` for the list of settings). As for now,
    most important of those is ``NUMBER_OF_ENTRIES_PER_PAGE`` - number of
    entries displayed per page (for both non-AJAX and AJAX requests).

(5) Add the following lines to the global ``urls`` module:

    .. code-block:: python

        # Admin timeline URLs. Should be placed BEFORE the Django admin URLs.
        url(r'^admin/timeline/', include('admin_timeline.urls')),
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

Grab and run the latest ``django_admin_timeline_example_app_installer.sh``:

.. code-block:: sh

    wget -O - https://raw.github.com/barseghyanartur/django-admin-timeline/stable/examples/django_admin_timeline_example_app_installer.sh | bash

Open your browser and test the app.

- URL: http://127.0.0.1:8001/admin/timeline/
- Admin username: admin
- Admin password: test

If quick installer doesn't work for you, see the manual steps on running the
`example project
<https://github.com/barseghyanartur/django-admin-timeline/tree/stable/examples>`_.

Troubleshooting
===============
If somehow static files are not collected properly (missing
``admin_timeline.js`` and ``admin_timeline.css`` files), install the latest
stable version from source.

.. code-block:: sh

    pip install https://github.com/barseghyanartur/django-admin-timeline/archive/stable.tar.gz

Usage
=====
After following all installation steps, you should  be able to access the
``django-admin-timeline`` by:

.. code-block:: text

    http://127.0.0.1:8000/admin/timeline/

An example application is available. See the `example directory
<https://github.com/barseghyanartur/django-admin-timeline/tree/stable/examples>`_.

Configuration and tweaks
========================
If you have way to many log entries and fetching all content types and users
isn't an option, set the ``ADMIN_TIMELINE_SIMPLE_FILTER_FORM`` to ``True``
in your settings. It will then change your multiple choice widgets into
plain char fields (comma separated ids are allowed).

Testing
=======
Project is covered by test (functional- and browser-tests).
To test with all supported Python/Django versions type:

.. code-block:: sh

    tox

To test against specific environment, type:

.. code-block:: sh

    tox -e py36-django111

To test just your working environment type:

.. code-block:: sh

    ./runtests.py

It's assumed that you have all the requirements installed. If not, first
install the test requirements:

.. code-block:: sh

    pip install -r examples/requirements/testing.txt

Browser tests
-------------
For browser tests you may choose between Firefox, headless Firefox and
PhantomJS. PhantomJS is faster, headless Firefox is fast as well, but
normal Firefox tests tell you more (as you see what exactly happens on the
screen). Both cases require some effort and both have disadvantages regarding
the installation (although once you have them installed they work perfect).

Latest versions of Firefox are often not supported by Selenium. Current
version of the Selenium for Python (2.53.6) works fine with Firefox 47.
Thus, instead of using system Firefox you could better use a custom one.

For PhantomJS you need to have NodeJS installed.

Set up Firefox 47
~~~~~~~~~~~~~~~~~
1. Download Firefox 47 from
   `this
   <https://ftp.mozilla.org/pub/firefox/releases/47.0.1/linux-x86_64/en-GB/firefox-47.0.1.tar.bz2>`__
   location and unzip it into ``/usr/lib/firefox47/``

2. Specify the full path to your Firefox in ``FIREFOX_BIN_PATH``
   setting. Example:

   .. code-block:: python

       FIREFOX_BIN_PATH = '/usr/lib/firefox47/firefox'

   If you set to use system Firefox, remove or comment-out the
   ``FIREFOX_BIN_PATH`` setting.

After that your Selenium tests would work.

Set up headless Firefox
~~~~~~~~~~~~~~~~~~~~~~~
1. Install ``xvfb`` package which is used to start Firefox in headless mode.

   .. code-block:: sh

        sudo apt-get install xvfb

2. Run the tests using headless Firefox.

   .. code-block:: sh

        ./scripts/runtests.sh

   Or run tox tests using headless Firefox.

   .. code-block:: sh

        ./scripts/tox.sh

Setup PhantomJS
~~~~~~~~~~~~~~~
You could also run tests in headless mode (faster). For that you will need
PhantomJS.

1. Install PhantomJS and dependencies.

   .. code-block:: sh

       curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh
       sudo bash nodesource_setup.sh
       sudo apt-get install nodejs
       sudo apt-get install build-essential libssl-dev
       sudo npm -g install phantomjs-prebuilt

2. Specify the ``PHANTOM_JS_EXECUTABLE_PATH`` setting. Example:

   .. code-block:: python

       PHANTOM_JS_EXECUTABLE_PATH = ""

   If you want to use Firefox for testing, remove or comment-out the
   ``PHANTOM_JS_EXECUTABLE_PATH`` setting.

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
