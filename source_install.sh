pip install -e hg+https://bitbucket.org/barseghyanartur/django-admin-timeline#egg=admin_timeline
./example/example/manage.py collectstatic --noinput
./example/example/manage.py syncdb --noinput
