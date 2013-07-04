Installation
============================
$ pip install -r requirements.txt

$ cp local_settings.example local_settings.py

$ ./manage.py syncdb --noinput

$ ./manage.py collectstatic --noinput

$ ./manage.py generate_test_data

$ ./manage.py runserver

Usage
============================
After following all installation steps, you should  be able to access the admin-timeline by:

    http://127.0.0.1:8000/admin/timeline/

Admin credentials:

    admin:admin
