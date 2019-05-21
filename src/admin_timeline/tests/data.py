__title__ = 'admin_timeline.tests.test_core'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = '2013-2019 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = (
    'TEST_USERNAME',
    'TEST_PASSWORD',
    'USERS_CREATED',
    'TEST_USERS_DATA',
)

TEST_USERNAME = 'admin'
TEST_PASSWORD = 'test'
USERS_CREATED = False
TEST_USERS_DATA = [
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
