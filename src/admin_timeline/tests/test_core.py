import logging
import os
import random
import unittest

import pytest

import radar

from six import text_type

from .helpers import _, log_info
from .base import NUM_ITEMS, WORDS, SENTENCES, change_date
from .data import TEST_PASSWORD, TEST_USERNAME, USERS_CREATED, TEST_USERS_DATA

__title__ = 'admin_timeline.tests.test_core'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

logger = logging.getLogger(__name__)


# Skipping from non-Django tests.
if os.environ.get("DJANGO_SETTINGS_MODULE", None):

    from django.conf import settings

    try:
        from django.utils.text import slugify
    except ImportError:
        from django.template.defaultfilters import slugify

    from django.contrib.admin.models import (
        LogEntry,
        ADDITION,
        # CHANGE,
        # DELETION
    )
    from django.contrib.auth.models import User
    from django.db import models, IntegrityError
    from django.contrib.contenttypes.models import ContentType

    # ************************************************************************
    # **************** Safe User import for Django > 1.5, < 1.8 **************
    # ************************************************************************
    from nine.user import User

    from foo.models import FooItem, Foo2Item, Foo3Item, Foo4Item

    def create_users():
        if not USERS_CREATED:

            for user_data_dict in TEST_USERS_DATA:
                user = User()

                for prop, value in user_data_dict.items():
                    setattr(user, prop, value)

                user.set_password(TEST_PASSWORD)
                try:
                    user.save()
                except IntegrityError as err:
                    logger.debug("{0} {1}".format(err, user))
                except Exception as err:
                    logger.debug("{0} {1}".format(err, user))

    MODEL_FACTORY = (
        FooItem,
        Foo2Item,
        Foo3Item,
        Foo4Item
    )

    CHANGE_MESSAGE_FACTORY = (
        'Changed title',
        'Changed slug',
        'Changed body',
        'Changed date_published',
    )

    def generate_data(num_items=NUM_ITEMS):
        create_users()

        class CustomLogEntry(models.Model):
            """Custom log entry."""

            action_time = models.DateTimeField(_('action time'))
            user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.CASCADE)
            content_type = models.ForeignKey(ContentType,
                                             blank=True,
                                             null=True,
                                             on_delete=models.CASCADE)
            object_id = models.TextField(_('object id'),
                                         blank=True,
                                         null=True)
            object_repr = models.CharField(_('object repr'), max_length=200)
            action_flag = models.PositiveSmallIntegerField(_('action flag'))
            change_message = models.TextField(_('change message'), blank=True)

            class Meta(object):
                """Class meta."""

                db_table = LogEntry._meta.db_table

        words = WORDS[:]

        users = User.objects.all()[:]

        random_date = radar.random_datetime()

        for index in range(num_items):
            # Saving an item to database
            foo_item_model_cls = MODEL_FACTORY[
                random.randint(0, len(MODEL_FACTORY) - 1)
            ]
            item = foo_item_model_cls()
            random_name = words[random.randint(0, len(words) - 1)]

            item.title = text_type(random_name).capitalize()
            item.body = text_type(
                SENTENCES[random.randint(0, len(SENTENCES) - 1)]
            )

            item.slug = slugify(item.title)
            random_date = radar.random_datetime() \
                if change_date() \
                else random_date
            item.date_published = random_date

            try:
                item.save()
                words.remove(random_name)

                if 0 == len(words):
                    words = WORDS[:]

            except Exception as err:
                logger.debug(err)

            # Create an item with content type
            try:
                # Creating a ``LogEntry`` for the item created.
                log_entry = CustomLogEntry()
                log_entry.action_time = item.date_published
                log_entry.user = users[random.randint(0, len(users) - 1)]
                log_entry.content_type = ContentType._default_manager \
                                                    .get_for_model(
                                                        foo_item_model_cls
                                                    )
                log_entry.object_id = item.pk
                log_entry.object_repr = text_type(item)

                log_entry.action_flag = ADDITION
                log_entry.save()
            except Exception as err:
                logger.debug(err)

            # Create an item without content type
            try:
                # Creating a ``LogEntry`` for the item created.
                log_entry = CustomLogEntry()
                log_entry.action_time = item.date_published
                log_entry.user = users[random.randint(0, len(users) - 1)]
                log_entry.object_repr = text_type(item)

                log_entry.action_flag = ADDITION
                log_entry.save()
            except Exception as err:
                logger.debug(err)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    from django.test import LiveServerTestCase

    from selenium import webdriver
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    from selenium.webdriver.support.wait import WebDriverWait
    # from selenium.common.exceptions import WebDriverException

    @pytest.mark.django_db
    class AdminTimelineViewsTest(LiveServerTestCase):
        """Tests of ``admin_timeline.views.log`` module."""

        pytestmark = pytest.mark.django_db

        @classmethod
        def setUpClass(cls):
            chrome_driver_path = getattr(
                settings,
                'CHROME_DRIVER_EXECUTABLE_PATH',
                None
            )
            chrome_driver_options = getattr(
                settings,
                'CHROME_DRIVER_OPTIONS',
                None
            )
            firefox_bin_path = getattr(settings, 'FIREFOX_BIN_PATH', None)
            phantom_js_executable_path = getattr(
                settings, 'PHANTOM_JS_EXECUTABLE_PATH', None
            )
            if chrome_driver_path is not None:
                cls.driver = webdriver.Chrome(
                    executable_path=chrome_driver_path,
                    chrome_options=chrome_driver_options
                )
            elif phantom_js_executable_path is not None:
                if phantom_js_executable_path:
                    cls.driver = webdriver.PhantomJS(
                        executable_path=phantom_js_executable_path
                    )
                else:
                    cls.driver = webdriver.PhantomJS()
            elif firefox_bin_path:
                binary = FirefoxBinary(firefox_bin_path)
                cls.driver = webdriver.Firefox(firefox_binary=binary)
            else:
                cls.driver = webdriver.Firefox()

            super(AdminTimelineViewsTest, cls).setUpClass()

            # Create user if doesn't exist yet.
            try:
                user = User._default_manager.get(username=TEST_USERNAME)
            except Exception as err:
                logger.debug(err)

                # Create a user account
                user = User()
                user.username = TEST_USERNAME
                user.set_password(TEST_PASSWORD)
                user.email = 'admin@dev.example.com'
                user.is_active = True
                user.is_staff = True
                user.is_superuser = True

                try:
                    user.save()
                except IntegrityError as err:
                    logger.debug(err)
                except Exception as err:
                    logger.debug(err)

            # Generate test data
            try:
                generate_data()
            except Exception as err:
                logger.debug(err)

        @classmethod
        def tearDownClass(cls):
            try:
                cls.driver.quit()
            except Exception as err:
                logger.debug(err)

            super(AdminTimelineViewsTest, cls).tearDownClass()

        def setUp(self):
            create_users()
            generate_data(num_items=10)

        @log_info
        def test_01_login(self):
            """Test login."""
            self.driver.get('{0}{1}'.format(self.live_server_url, '/admin/'))
            username_input = self.driver.find_element_by_name("username")
            username_input.send_keys(TEST_USERNAME)
            password_input = self.driver.find_element_by_name("password")
            password_input.send_keys(TEST_PASSWORD)
            self.driver.find_element_by_xpath(
                '//input[@value="Log in"]').click()

        @log_info
        def test_02_view(self):
            """Test view."""
            # create_users()
            # # Generate test data
            # try:
            #     generate_data(num_items=10)
            # except Exception as err:
            #     logger.debug(err)

            # Test login
            self.driver.get(
                '{0}{1}'.format(self.live_server_url, '/admin/timeline/')
            )
            username_input = self.driver.find_element_by_name("username")
            username_input.send_keys(TEST_USERNAME)
            password_input = self.driver.find_element_by_name("password")
            password_input.send_keys(TEST_PASSWORD)
            self.driver.find_element_by_xpath(
                '//input[@value="Log in"]').click()

            WebDriverWait(self.driver, timeout=5).until(
                lambda driver: driver.find_element_by_id('admin-timeline')
            )

            # Test view
            workflow = []

            container = self.driver.find_element_by_id('admin-timeline')
            self.assertTrue(container is not None)
            workflow.append(container)

            WebDriverWait(self.driver, timeout=5).until(
                lambda driver: driver.find_element_by_xpath(
                    '//li[@class="date-entry"]'
                )
            )

            item = self.driver.find_element_by_xpath(
                '//li[@class="date-entry"]'
            )
            self.assertTrue(item is not None)
            workflow.append(item)

            return workflow


if __name__ == "__main__":
    # Tests
    unittest.main()
