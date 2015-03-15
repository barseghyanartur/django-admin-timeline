reset
./scripts/uninstall.sh
./scripts/install_django_1_8.sh

python example/example/manage.py test admin_timeline --settings=settings_django_1_8 --traceback -v 3