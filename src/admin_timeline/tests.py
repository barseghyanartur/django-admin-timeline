from __future__ import print_function

__title__ = 'admin_timeline.tests'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2014 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'

import unittest
import os

PROJECT_DIR = lambda base : os.path.join(os.path.dirname(__file__), base).replace('\\','/')

PRINT_INFO = True

TEST_USERNAME = 'admin'
TEST_PASSWORD = 'test'
USERS_CREATED = False

def print_info(func):
    """
    Prints some useful info.
    """
    if not PRINT_INFO:
        return func

    def inner(self, *args, **kwargs):
        result = func(self, *args, **kwargs)

        print('\n\n{0}'.format(func.__name__))
        print('============================')
        if func.__doc__:
            print('""" {0} """'.format(func.__doc__.strip()))
        print('----------------------------')
        if result is not None:
            print(result)
        print('\n++++++++++++++++++++++++++++')

        return result
    return inner

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import random

import sys

PY3 = sys.version_info[0] == 3

if PY3:
    from string import punctuation
else:
    from string import translate, maketrans, punctuation

import radar

FACTORY = """
    Sed dictum in tellus non iaculis. Aenean ac interdum ipsum. Etiam tempor quis ante vel rhoncus. Nulla
    facilisi. Curabitur iaculis consequat odio ut imperdiet? Integer accumsan; nisl vitae fermentum malesuada,
    sapien nulla sodales orci, et elementum lacus purus vel purus! Nullam orci neque, tristique in porta id,
    pretium ac sem. Fusce non est risus. Fusce convallis tellus augue, quis volutpat tellus dapibus sagittis.
    Integer lacinia commodo risus vel cursus. Etiam vitae dui in dolor porta luctus sed id elit. Nulla et est
    nec magna facilisis sagittis. Praesent tincidunt dictum lectus, sed aliquam eros. Donec placerat tortor ut
    lorem facilisis congue. Quisque ac risus nibh. Etiam ultrices nibh justo; sed mollis ipsum dapibus vitae.Ut
    vitae molestie erat. Mauris ac justo quis ante posuere vehicula. Vivamus accumsan mi volutpat diam lacinia,
    vitae semper lectus pharetra. Cras ultrices arcu nec viverra consectetur. Cras placerat ante quis dui
    consequat cursus. Nulla at enim dictum, consectetur ligula eget, vehicula nisi. Suspendisse eu ligula vitae
    est tristique accumsan nec adipiscing risus.Donec tempus dui eget mollis fringilla. Fusce eleifend lacus lectus,
    vel ornare felis lacinia ut. Morbi vel adipiscing augue. Vestibulum ante ipsum primis in faucibus orci luctus et
    ultrices posuere cubilia Curae; Cras mattis pulvinar lacus, vitae pulvinar magna egestas non. Aliquam in urna
    quis leo feugiat faucibus. Aliquam erat volutpat. Maecenas non mauris libero. Suspendisse nisi lorem, cursus a
    tristique a, porttitor in nisl. Mauris pellentesque gravida mi non mattis. Cras mauris ligula, interdum semper
    tincidunt sed, ornare a ipsum. Nulla ultrices tempus tortor vitae vehicula.Etiam at augue suscipit, vehicula
    sapien sit amet; eleifend orci. Etiam venenatis leo nec cursus mattis. Nulla suscipit nec lorem et lobortis.
    Donec interdum vehicula massa sed aliquam. Praesent eleifend mi sed mi pretium pellentesque. In in nisi tincidunt,
    commodo lorem quis; tincidunt nisl. In suscipit quam a vehicula tincidunt! Fusce vitae varius nunc. Proin at
    ipsum ac tellus hendrerit ultricies. Phasellus auctor hendrerit sapien viverra facilisis. Suspendisse lacus erat,
    cursus at dolor in, vulputate convallis sapien. Etiam augue nunc, lobortis vel viverra sit amet, pretium et
    lacus.Pellentesque elementum lectus eget massa tempus elementum? Nulla nec auctor dolor. Aliquam congue purus
    quis libero fermentum cursus. Etiam quis massa ac nisl accumsan convallis vitae ac augue. Mauris neque est,
    posuere quis dolor non, volutpat gravida tortor. Cum sociis natoque penatibus et magnis dis parturient montes,
    nascetur ridiculus mus. Vivamus ullamcorper, urna at ultrices aliquam, orci libero gravida ligula, non pulvinar
    sem magna sed tortor. Sed elementum leo viverra ipsum aliquet convallis. Suspendisse scelerisque auctor sapien.
    Mauris enim nisl, sollicitudin at rhoncus vitae, convallis nec mauris. Phasellus sollicitudin dui ut luctus
    consectetur. Vivamus placerat, neque id sagittis porttitor, nunc quam varius dolor, sit amet egestas nulla
    risus eu odio. Mauris gravida eleifend laoreet. Aenean a nulla nisl. Integer pharetra magna adipiscing, imperdiet
    augue ac, blandit felis. Cras id aliquam neque, vel consequat sapien.Duis eget vulputate ligula. Aliquam ornare
    dui non nunc laoreet, non viverra dolor semper. Aenean ullamcorper velit sit amet dignissim fermentum! Aenean urna
    leo, rutrum volutpat mauris nec, facilisis molestie tortor. In convallis pellentesque lorem, a lobortis erat
    molestie et! Ut sed sem a odio aliquam elementum. Morbi pretium velit libero, adipiscing consequat leo dignissim
    eu. Mauris vestibulum feugiat risus; quis pharetra purus tincidunt quis. Morbi semper tincidunt lorem id iaculis.
    Quisque non pulvinar magna. Morbi consequat eleifend neque et iaculis. Fusce non laoreet urna. Donec ut nunc
    ultrices, fringilla nunc ut, tempor elit. Phasellus semper sapien augue, in gravida neque egestas at.
    Integer dapibus lacus vitae luctus sagittis! Suspendisse imperdiet tortor eget mattis consectetur. Aliquam viverra
    purus a quam lacinia euismod. Nunc non consequat mi; ac vehicula lacus. Pellentesque accumsan ac diam in fermentum!
    Maecenas quis nibh sed dolor adipiscing facilisis. Aenean vel arcu eu est fermentum egestas vulputate eget purus.
    Sed fermentum rhoncus dapibus. Quisque molestie magna eu accumsan lobortis. Vestibulum cursus euismod posuere.
    Aliquam eu dapibus urna. Nulla id accumsan justo. Vivamus vitae ullamcorper tellus. Class aptent taciti sociosqu
    ad litora torquent per conubia nostra, per inceptos himenaeos.Donec pulvinar tempus lectus vitae ultricies.
    Vestibulum sagittis orci quis risus ultricies feugiat. Nunc feugiat velit est, at aliquam massa tristique eu.
    Aenean quis enim vel leo vestibulum volutpat in non elit. Quisque molestie tincidunt purus; ac lacinia mauris
    rhoncus in. Nullam id arcu at mauris varius viverra ut vitae massa. In ac nunc ipsum. Proin consectetur urna sit
    amet mattis vulputate. Nullam lacinia pretium tempus. Aenean quis ornare metus, tempus volutpat neque. Mauris
    volutpat scelerisque augue; at lobortis nulla rhoncus vitae. Mauris at lobortis turpis. Vivamus et ultrices lacus.
    Donec fermentum neque in eros cursus, ac tincidunt sapien consequat. Curabitur varius commodo rutrum. Nulla
    facilisi. Ut feugiat dui nec turpis sodales aliquam. Quisque auctor vestibulum condimentum. Quisque nec eros
    lorem. Curabitur et felis nec diam dictum ultrices vestibulum ac eros! Quisque eu pretium lacus. Morbi bibendum
    sagittis rutrum. Nam eget tellus quam. Nullam pharetra vestibulum justo. Donec molestie urna et scelerisque
    laoreet? Sed consectetur pretium hendrerit. Quisque erat nulla, elementum sit amet nibh vel, posuere pulvinar
    nulla. Donec elementum adipiscing dictum! Nam euismod semper nisi, eu lacinia felis placerat vel! Praesent eget
    dapibus turpis, et fringilla elit. Maecenas quis nunc cursus felis fringilla consequat! Cum sociis natoque
    penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed ullamcorper libero quis nisl sollicitudin,
    ut pulvinar arcu consectetur. Donec nisi nibh, condimentum et lectus non, accumsan imperdiet ipsum. Maecenas vitae
    massa eget lorem ornare dignissim. Nullam condimentum mauris id quam tincidunt venenatis. Aenean mattis viverra
    sem, vitae luctus velit rhoncus non. Vestibulum leo justo, rhoncus at aliquam et, iaculis sed dolor. Integer
    bibendum vitae urna in ornare! Cras accumsan nulla eu libero tempus, in dignissim augue imperdiet. Vivamus a
    lacinia odio. Curabitur id egestas eros. Integer non rutrum est. In nibh sem, tempus ac dignissim vel, ornare ac
    mi. Nulla congue scelerisque est nec commodo. Phasellus turpis lorem, sodales quis sem id, facilisis commodo
    massa. Vestibulum ultrices dolor eget purus semper euismod? Fusce id congue leo. Quisque dui magna, ullamcorper
    et leo eget, commodo facilisis ipsum. Curabitur congue vitae risus nec posuere. Phasellus tempor ligula in nisl
    pellentesque mattis. Sed nunc turpis, pharetra vel leo ac, lacinia cursus risus. Quisque congue aliquet volutpat.
    Integer dictum est quis semper tristique. Donec feugiat vestibulum tortor, id fringilla nisi lobortis eu. Nam
    hendrerit egestas sem, non mollis tortor iaculis quis. Phasellus id aliquet erat. Nunc facilisis nisi dolor,
    quis semper dui euismod vel. Cras convallis bibendum tortor malesuada tincidunt. Sed urna quam, pellentesque
    eget eleifend ac, consequat bibendum urna. Sed fringilla elit hendrerit leo blandit laoreet eget quis quam!
    Morbi eu leo a dolor aliquet dictum. Suspendisse condimentum mauris non ipsum rhoncus, sit amet hendrerit augue
    gravida. Quisque facilisis pharetra felis faucibus gravida. In arcu neque, gravida ut fermentum ut, placerat eu
    quam. Nullam aliquet lectus mauris, quis dignissim est mollis sed. Ut vestibulum laoreet eros quis cursus. Proin
    commodo eros in mollis mollis. Mauris bibendum cursus nibh, sit amet eleifend mauris luctus vitae. Sed aliquet
    pretium tristique. Morbi ultricies augue a lacinia porta. Nullam mollis erat non imperdiet imperdiet. Etiam
    tincidunt fringilla ligula, in adipiscing libero viverra eu. Nunc gravida hendrerit massa, in pellentesque nunc
    dictum id.
    """

if PY3:
    split_words = lambda f: list(set(f.lower().translate(str.maketrans("", "", punctuation)).split()))
else:
    split_words = lambda f: list(set(translate(f.lower(), maketrans(punctuation, ' ' * len(punctuation))).split()))

split_sentences = lambda f: f.split('?')
change_date = lambda: bool(random.randint(0, 1))

WORDS = split_words(FACTORY)
SENTENCES = split_sentences(FACTORY)
NUM_ITEMS = 50

_ = lambda s: s

# Skipping from non-Django tests.
if os.environ.get("DJANGO_SETTINGS_MODULE", None):

    from django.conf import settings

    try:
        from django.utils.text import slugify
    except ImportError:
        from django.template.defaultfilters import slugify

    from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
    from django.contrib.auth.models import User
    from django.db import IntegrityError
    from django.contrib.contenttypes.models import ContentType
    from django.db import models

    # *************************************************************************
    # **************** Safe User import for Django > 1.5, < 1.8 ***************
    # *************************************************************************
    from nine.user import User

    from foo.models import FooItem, Foo2Item, Foo3Item, Foo4Item

    def create_users():
        if not USERS_CREATED:
            data = [
                {
                    u'email': u'admin.v4@foreverchild.info',
                    u'first_name': u'',
                    u'is_active': True,
                    u'is_staff': True,
                    u'is_superuser': True,
                    u'last_name': u'',
                    u'username': TEST_USERNAME
                },
                {
                    u'email': u'artur.barseghyan@gmail.com',
                    u'first_name': u'Artur',
                    u'is_active': True,
                    u'is_staff': True,
                    u'is_superuser': False,
                    u'last_name': u'Barseghyan',
                    u'username': u'arturbarseghyan'
                },
                {
                    u'email': u'john.doe@example.com',
                    u'first_name': u'John',
                    u'is_active': True,
                    u'is_staff': True,
                    u'is_superuser': False,
                    u'last_name': u'Doe',
                    u'username': u'john.doe'
                },
                {
                    u'email': u'johnatan@example.com',
                    u'first_name': u'Johnatan',
                    u'is_active': True,
                    u'is_staff': True,
                    u'is_superuser': False,
                    u'last_name': u'Livingstone',
                    u'username': u'johnatan'
                },
                {
                    u'email': u'oscar@example.com',
                    u'first_name': u'Oscar',
                    u'is_active': True,
                    u'is_staff': True,
                    u'is_superuser': False,
                    u'last_name': u'',
                    u'username': u'oscar'
                },
                {
                    u'email': u'charlie@example.com',
                    u'first_name': u'Charlie',
                    u'is_active': True,
                    u'is_staff': True,
                    u'is_superuser': False,
                    u'last_name': u'Big Potatoe',
                    u'username': u'charlie'
                }
            ]

            for user_data_dict in data:
                user = User()

                for prop, value in user_data_dict.items():
                    setattr(user, prop, value)

                #print(user.__dict__)
                #print("set password {0} for user {1}".format(TEST_PASSWORD, user.username))
                user.set_password(TEST_PASSWORD)
                try:
                    user.save()
                except IntegrityError as err:
                    print("{0} {1}".format(err, user))
                except Exception as err:
                    print("{0} {1}".format(err, user))

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
            action_time = models.DateTimeField(_('action time'))
            user = models.ForeignKey(User)
            content_type = models.ForeignKey(ContentType, blank=True, null=True)
            object_id = models.TextField(_('object id'), blank=True, null=True)
            object_repr = models.CharField(_('object repr'), max_length=200)
            action_flag = models.PositiveSmallIntegerField(_('action flag'))
            change_message = models.TextField(_('change message'), blank=True)

            class Meta:
                db_table = LogEntry._meta.db_table

        words = WORDS

        users = User.objects.all()[:]

        random_date = radar.random_datetime()

        for index in range(num_items):
            # Saving an item to database
            FooItemModel = MODEL_FACTORY[random.randint(0, len(MODEL_FACTORY) - 1)]
            i = FooItemModel()
            random_name = words[random.randint(0, len(words) - 1)]

            if PY3:
                i.title = str(random_name).capitalize()
                i.body = str(SENTENCES[random.randint(0, len(SENTENCES) - 1)])
            else:
                i.title = unicode(random_name).capitalize()
                i.body = unicode(SENTENCES[random.randint(0, len(SENTENCES) - 1)])

            i.slug = slugify(i.title)
            random_date = radar.random_datetime() if change_date() else random_date
            i.date_published = random_date

            try:
                i.save()
                words.remove(random_name)

                if 0 == len(words):
                    words = WORDS

            except Exception as e:
                print(e)

            try:
                # Creating a ``LogEntry`` for the item created.
                l = CustomLogEntry()
                l.action_time = i.date_published
                l.user = users[random.randint(0, len(users) - 1)]
                l.content_type = ContentType._default_manager \
                                            .get_for_model(FooItemModel)
                l.object_id = i.pk

                if PY3:
                    l.object_repr = str(i)
                else:
                    l.object_repr = unicode(i)

                l.action_flag = ADDITION
                l.save()
            except Exception as e:
                print(e)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    from django.test import LiveServerTestCase
    #from django.contrib.auth.models import User

    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.support.wait import WebDriverWait

    class AdminTimelineViewsTest(LiveServerTestCase): #unittest.TestCase
        """
        Tests of ``admin_timeline.views.log`` module.
        """

        @classmethod
        def setUpClass(cls):
            cls.selenium = WebDriver()
            super(AdminTimelineViewsTest, cls).setUpClass()

            # Create user if doesn't exist yet.
            try:
                u = User._default_manager.get(username=TEST_USERNAME)
            except Exception as e:
                print(e)

                # Create a user account
                u = User()
                u.username = TEST_USERNAME
                u.set_password(TEST_PASSWORD)
                u.email = 'admin@dev.example.com'
                u.is_active = True
                u.is_staff = True
                u.is_superuser = True

                try:
                    u.save()
                except IntegrityError as e:
                    print(e)
                except Exception as e:
                    print(e)

            # Generate test data
            try:
                generate_data()
            except Exception as e:
                print(e)

        @classmethod
        def tearDownClass(cls):
            try:
                cls.selenium.quit()
            except Exception as e:
                print(e)

            super(AdminTimelineViewsTest, cls).tearDownClass()

        @print_info
        def test_01_login(self):
            """
            Test login.
            """
            create_users()
            self.selenium.get('{0}{1}'.format(self.live_server_url, '/admin/'))
            username_input = self.selenium.find_element_by_name("username")
            username_input.send_keys(TEST_USERNAME)
            password_input = self.selenium.find_element_by_name("password")
            password_input.send_keys(TEST_PASSWORD)
            #import ipdb; ipdb.set_trace()
            self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

        @print_info
        def test_02_view(self):
            """
            Test view.
            """
            create_users()
            # Generate test data
            try:
                generate_data(num_items=10)
            except Exception as e:
                print(e)

            # Test login
            self.selenium.get('{0}{1}'.format(self.live_server_url, '/admin/timeline/'))
            username_input = self.selenium.find_element_by_name("username")
            username_input.send_keys(TEST_USERNAME)
            password_input = self.selenium.find_element_by_name("password")
            password_input.send_keys(TEST_PASSWORD)
            #import ipdb; ipdb.set_trace()
            self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

            WebDriverWait(self.selenium, timeout=5).until(
                lambda driver: driver.find_element_by_id('admin-timeline')
                )

            # Test view
            workflow = []

            container = self.selenium.find_element_by_id('admin-timeline')
            self.assertTrue(container is not None)
            workflow.append(container)

            item = self.selenium.find_element_by_xpath('//li[@class="date-entry"]')
            self.assertTrue(item is not None)
            workflow.append(item)

            return workflow


if __name__ == "__main__":
    # Tests
    unittest.main()
