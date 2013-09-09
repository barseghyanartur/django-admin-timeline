__title__ = 'admin_timeline.defaults'
__version__ = '1.0'
__build__ = 0x00000a
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__all__ = ('NUMBER_OF_ENTRIES_PER_PAGE', 'LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT', 'SINGLE_LOG_ENTRY_DATE_FORMAT', \
           'DEBUG')

NUMBER_OF_ENTRIES_PER_PAGE = 35 # Number of entries per page. Used in both non-AJAX and AJAX driven views.

LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT = "l j F Y" # Headings (per day basis) date format in timeline.
SINGLE_LOG_ENTRY_DATE_FORMAT = "g:i:s A" # Single log entry date format in timeline.

DEBUG = False # Personal debug mode, which has nothing to do with global settings.DEBUG