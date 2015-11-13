#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "fix2.py"
run_python_test "XBingo" 'Missed'  
run_python_test "Bingo" 'Hit!'  
run_python_test "BingoX" 'Missed'  
end_python_test




