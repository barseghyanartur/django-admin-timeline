import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'readme.rst')).read()
except:
    readme = ''

template_dir = "src/admin_timeline/templates/admin_timeline"
templates = [os.path.join(template_dir, f) for f in os.listdir(template_dir)]

static_dir = "src/admin_timeline/static"
static_files = [os.path.join(static_dir, f) for f in os.listdir(static_dir)]

version = '0.8'

setup(
    name = 'django-admin-timeline',
    version = version,
    description = ("Facebook-like timeline for Django admin"),
    long_description = readme,
    classifiers = [
        "Framework :: Django",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = 'django-admin-timeline, django, app, python',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://bitbucket.org/barseghyanartur/django-admin-timeline',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    package_data = {'admin_timeline': templates + static_files},
    include_package_data = True,
)
