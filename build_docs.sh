pip install -r example/requirements.txt
rm builddocs.zip
rm builddocs -rf
./uninstall.sh
./install.sh
cat README.rst SCREENSHOTS.rst docs/documentation.rst.distrib > docs/index.rst
sphinx-build -n -a -b html docs builddocs
cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..