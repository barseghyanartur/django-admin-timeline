import os
from setuptools import setup, find_packages

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
except:
    readme = ''

template_dir = "src/admin_timeline/templates/admin_timeline"
templates = [os.path.join(template_dir, f) for f in os.listdir(template_dir)]

static_dir = "src/admin_timeline/static"
static_files = [os.path.join(static_dir, f) for f in os.listdir(static_dir)]

version = '1.3'

setup(
    name = 'django-admin-timeline',
    version = version,
    description = ("Facebook-like timeline for Django admin"),
    long_description = readme,
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
    ],
    keywords = 'django-admin-timeline, django, app, python',
    author = 'Artur Barseghyan',
    author_email = 'artur.barseghyan@gmail.com',
    url = 'https://bitbucket.org/barseghyanartur/django-admin-timeline',
    package_dir = {'':'src'},
    packages = find_packages(where='./src'),
    license = 'GPL 2.0/LGPL 2.1',
    package_data = {
        'admin_timeline': templates + static_files
    },
    include_package_data = True,
    install_requires = [
        'radar==0.3',
    ]
)
