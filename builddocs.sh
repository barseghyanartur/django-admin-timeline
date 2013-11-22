pip install -r example/requirements.txt
rm builddocs.zip
rm builddocs -rf
./install.sh
sphinx-build -n -a -b html docs builddocs
cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..