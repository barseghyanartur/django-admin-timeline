mkdir -p examples/media/ examples/static/ example/db/
python setup.py develop
./examples/simple/manage.py collectstatic --noinput
./examples/simple/manage.py migrate --noinput
