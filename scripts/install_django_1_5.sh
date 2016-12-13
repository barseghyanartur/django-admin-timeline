pip install -r examples/requirements/django_1_5.txt
mkdir -p examples/media/ examples/static/ examples/db/
python setup.py install
./examples/simple/manage.py collectstatic --noinput
./examples/simple/manage.py migrate --noinput
