reset
./scripts/uninstall.sh
./scripts/install_django_1_7.sh

python example/example/manage.py test admin_timeline --settings=settings_django_1_7 --traceback -v 3