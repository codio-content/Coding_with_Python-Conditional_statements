#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "fast-cars2.py"
run_python_test '70 70' 'no fast cars'
run_python_test '71 70' '1 fast car'
run_python_test '70 71' '1 fast car'
run_python_test '71 71' '2 fast cars'
end_python_test
