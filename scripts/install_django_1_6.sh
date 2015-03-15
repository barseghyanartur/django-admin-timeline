#pip install -r example/requirements.txt --allow-all-external --allow-unverified django-admin-tools
#cd ..
pip install -r example/requirements_django_1_6.txt
mkdir -p example/media/ example/static/ example/db/
python setup.py install
./example/example/manage.py collectstatic --noinput
./example/example/manage.py syncdb --noinput
