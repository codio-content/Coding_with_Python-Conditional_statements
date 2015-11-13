#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "fix1.py"
run_python_test "hello" '1'  
end_python_test




