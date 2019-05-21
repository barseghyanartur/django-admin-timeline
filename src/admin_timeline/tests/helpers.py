from __future__ import print_function

import logging
import os

__title__ = 'admin_timeline.tests.helpers'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

logger = logging.getLogger(__name__)


def project_dir(base):
    return os.path.join(os.path.dirname(__file__), base).replace('\\', '/')


PROJECT_DIR = project_dir

LOG_INFO = True


def log_info(func):
    """Log some useful info."""
    if not LOG_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        logger.debug('\n\n{0}'.format(func.__name__))
        logger.debug('============================')
        if func.__doc__:
            logger.debug('""" {0} """'.format(func.__doc__.strip()))
        logger.debug('----------------------------')
        if result is not None:
            logger.debug(result)
        logger.debug('\n++++++++++++++++++++++++++++')

        return result
    return inner


def _(val):
    """Return value as is."""
    return val
