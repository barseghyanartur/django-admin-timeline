wget -O django_admin_timeline_example_app_installer.tar.gz https://github.com/barseghyanartur/django-admin-timeline/archive/stable.tar.gz
virtualenv admin_timeline
source admin_timeline/bin/activate
mkdir django_admin_timeline_example_app_installer/
tar -xvf django_admin_timeline_example_app_installer.tar.gz -C django_admin_timeline_example_app_installer
cd django_admin_timeline_example_app_installer/django-admin-timeline-stable/example/example/
pip install Django
pip install -r ../requirements.txt
pip install -e git+https://github.com/barseghyanartur/django-admin-timeline@stable#egg=django-admin-timeline
mkdir ../media/
mkdir ../media/static/
mkdir ../static/
mkdir ../db/
mkdir ../logs/
mkdir ../tmp/
cp local_settings.example local_settings.py
./manage.py syncdb --noinput --traceback -v 3
./manage.py migrate --noinput
./manage.py collectstatic --noinput --traceback -v 3
./manage.py generate_test_data --traceback -v 3
./manage.py runserver 0.0.0.0:8001 --traceback -v 3