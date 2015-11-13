#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "bool-input.py"
run_python_test "True True" 'cold and rainy'  
run_python_test "True False" 'cold and dry' 
run_python_test "False True" 'warm and rainy' 
run_python_test "False False" 'warm and dry' 
end_python_test

