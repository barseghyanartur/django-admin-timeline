mkdir -p examples/media/ examples/static/ example/db/
python setup.py install
./examples/simple/manage.py collectstatic --noinput
./examples/simple/manage.py migrate --noinput
