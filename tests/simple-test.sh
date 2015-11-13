#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "simple.py"
run_python_test '100' 'True'
run_python_test '101' 'True'
run_python_test '99' 'False'
end_python_test

