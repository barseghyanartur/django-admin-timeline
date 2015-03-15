reset
./scripts/uninstall.sh
./scripts/install_django_1_6.sh

python example/example/manage.py test admin_timeline --traceback -v 3