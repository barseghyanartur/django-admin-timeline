__title__ = 'admin_timeline.defaults'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'NUMBER_OF_ENTRIES_PER_PAGE', 'LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT',
    'SINGLE_LOG_ENTRY_DATE_FORMAT', 'DEBUG'
)

# Number of entries per page. Used in both non-AJAX and AJAX driven views.
NUMBER_OF_ENTRIES_PER_PAGE = 35

# Headings (per day basis) date format in timeline.
LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT = "l j F Y"

# Single log entry date format in timeline.
SINGLE_LOG_ENTRY_DATE_FORMAT = "g:i:s A" 

# Personal debug mode, which has nothing to do with global settings.DEBUG
DEBUG = False
