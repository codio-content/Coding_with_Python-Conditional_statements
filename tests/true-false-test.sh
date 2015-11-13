#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "true-false.py"
run_python_test "true" '1'  
run_python_test "false" '0' 
end_python_test




