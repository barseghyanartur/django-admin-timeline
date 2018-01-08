#pip install -r example/requirements.txt
rm builddocs.zip
rm builddocs -rf
#./scripts/uninstall.sh
#./scripts/install.sh
./scripts/prepare_docs.sh

sphinx-build -n -a -b html docs builddocs
cd builddocs && zip -r ../builddocs.zip . -x ".*" && cd ..
