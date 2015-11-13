#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "eq.py"
run_python_test "100" 'Hit'  
run_python_test "101" 'Miss' 
end_python_test




