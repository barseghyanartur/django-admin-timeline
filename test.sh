# Core tests
./uninstall.sh
reset
./install.sh
reset
python src/admin_timeline/tests.py

# Django tests
pip install -r example/requirements.txt
python example/example/manage.py test admin_timeline