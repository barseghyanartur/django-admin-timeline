# Django settings for resato_portal project.
import os

from .core import PROJECT_DIR

DEBUG = True
DEBUG_TOOLBAR = True
# TEMPLATE_DEBUG = DEBUG
DEBUG_TEMPLATE = DEBUG
DEV = False

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        # Or path to database file if using sqlite3.
        'NAME': PROJECT_DIR(os.path.join('..', '..', 'db', 'example.db')),
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        # Empty for localhost through domain sockets or '127.0.0.1' for
        # localhost through TCP.
        'HOST': '',
        # Set to empty string for default.
        'PORT': '',
    }
}

INTERNAL_IPS = ('127.0.0.1',)

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = PROJECT_DIR(os.path.join('..', '..', 'tmp'))

DEFAULT_FROM_EMAIL = '<no-reply@example.com>'

ADMIN_TIMELINE_NUMBER_OF_ENTRIES_PER_PAGE = 4

os.environ.setdefault(
    'ADMIN_TIMELINE_SOURCE_PATH',
    '/home/artur/bbrepos/django-admin-timeline-dev/src'
)

CHROME_DRIVER_EXECUTABLE_PATH = os.environ.get('CHROME_BIN', None)
if not CHROME_DRIVER_EXECUTABLE_PATH:
    CHROME_DRIVER_EXECUTABLE_PATH = '/usr/local/share/chromedriver'

# CHROME_DRIVER_OPTIONS = [
#     '-headless',  # '--headless' if using chrome instead of firefox
#     '-no-sandbox',
#     '-single-process',
# ]
# FIREFOX_BIN_PATH = '/usr/lib/firefox47/firefox'
# PHANTOM_JS_EXECUTABLE_PATH = ''
# ADMIN_TIMELINE_SIMPLE_FILTER_FORM = True
