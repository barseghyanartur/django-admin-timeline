Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: none

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

1.8
---
2021-01-25

- Drop Python 2.7 support.
- Drop Python 3.5 support.
- Tested against Python 3.8.
- Tested against Django 2.2, 3.0 and 3.1.

1.7.2
-----
2019-05-21

- Minor fixes in ajax views.

1.7.1
-----
2019-05-21

- Added ``ADMIN_TIMELINE_SIMPLE_FILTER_FORM`` setting for to be used when
  you have way to many log entries and fetching all content types and users
  isn't an option.

1.7
---
2019-05-20

- Drop support for Python 3.4.
- Tested against Python 3.7.
- Added Django 2.1 and 2.2 support.
- Dropping support for Django 1.9 and 1.10.

1.6.2
-----
2018-01-08

- Django 2.0 support.

1.6.1
-----
2017-08-08

- Django 1.11 support.
- Fix error on log entries without content type. #6
- Fix templates style blocks not calling base template super. #7

1.6
---
2016-12-13

Announcing dropping support of Python versions 2.6 and 3.3, as well as
Django versions 1.4, 1.5, 1.6 and 1.7. As of ``django-admin-timeline`` 1.6
everything is still backwards compatible with these versions, but in future
versions it will be wiped out.

- Django 1.9 and 1.8 compatibility.
- pep8 fixes.

1.5.4
-----
2015-10-02

- Fix broken admin URLs for entries on Django 1.4/1.5.

1.5.3
-----
2015-09-08

- Fix broken loader image.

1.5.2
-----
2015-09-08

- Django 1.4 fixes.

1.5.1
-----
2015-03-16

- Fix improperly resolved URLs of the content types.
- Fix broken image loader URL.
- Replace checkboxes with jQuery multiple-select plugin checkboxes.
- Update the jQuery version used to 1.11.12.

1.5
---
2015-03-15

- Django 1.8 support.
- Support for wheel packages.
- Refactored JavaScript.
- Mention Heroku demo in documentation.
- Minor speed-ups and improvements.

1.4
---
2014-10-31

- Django 1.4 support added.
- Django 1.7 support added.

1.3
---
2013-11-23

- Removed the `six` dependancy.
- Tests updated. Django 1.6 proclaimed to be supported.
- Quick demo installer added.

1.2
---
2013-10-09

- Added support for Python 2.6.8.

1.1
---
2013-10-08

- Tests added. Tiny improvements/refactoring.

1.0
---
2013-09-09

- Python 3.3 support
