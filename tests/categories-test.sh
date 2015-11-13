#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "categories.py"
run_python_test '6' 'primary school'
run_python_test '11' 'primary school'
run_python_test '12' 'secondary school'
run_python_test '18' 'secondary school'
run_python_test '5' 'NA'
run_python_test '19' 'NA'
end_python_test

