"""
Override the following values in your global ``settings`` module by adding
`ADMIN_TIMELINE_` prefix to the values. When it comes to importing the values,
import them from ``admin_timeline.settings`` module (without the
`ADMIN_TIMELINE_` prefix).

``NUMBER_OF_ENTRIES_PER_PAGE``: Number of entries per page.

``SINGLE_LOG_ENTRY_DATE_FORMAT``: Date format for the single log entry. Default
value is "g:i:s A".

``LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT``: Day headings date format. Default
value is "l j F Y".

``DEBUG``
"""

__title__ = 'admin_timeline.settings'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'NUMBER_OF_ENTRIES_PER_PAGE', 'SINGLE_LOG_ENTRY_DATE_FORMAT',
    'LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT', 'DEBUG',
)

from admin_timeline.conf import get_setting

NUMBER_OF_ENTRIES_PER_PAGE = get_setting('NUMBER_OF_ENTRIES_PER_PAGE')
SINGLE_LOG_ENTRY_DATE_FORMAT = get_setting('SINGLE_LOG_ENTRY_DATE_FORMAT')
LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT = get_setting(
    'LOG_ENTRIES_DAY_HEADINGS_DATE_FORMAT'
    )

DEBUG = get_setting('DEBUG')
