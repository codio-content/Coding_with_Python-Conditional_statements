#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "1-0.py"
run_python_test "1" 'On'  
run_python_test "0" 'Off' 
end_python_test


