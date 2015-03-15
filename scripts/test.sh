pip install selenium --upgrade
# Core tests
./scripts/uninstall.sh
reset
./scripts/install.sh
reset
python src/admin_timeline/tests.py

# Django tests
pip install -r example/requirements.txt
python example/example/manage.py test admin_timeline