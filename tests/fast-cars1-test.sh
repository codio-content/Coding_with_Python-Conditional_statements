#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "fast-cars1.py"
run_python_test '70 70' 'ok'
run_python_test '71 70' 'fast cars'
run_python_test '70 71' 'fast cars'
run_python_test '71 71' 'fast cars'
end_python_test
