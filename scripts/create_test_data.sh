#!/usr/bin/env bash
cd examples/simple/
./manage.py generate_test_data --traceback -v 3 "$@"
