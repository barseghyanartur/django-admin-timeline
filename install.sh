mkdir -p example/media/ example/static/ example/db/
python setup.py install
./example/example/manage.py collectstatic --noinput
./example/example/manage.py syncdb --noinput
