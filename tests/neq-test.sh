#!/bin/bash
. /home/codio/workspace/tests/python-test-lib.sh

start_python_test "neq.py"
run_python_test "BingoX" 'Missed'  
run_python_test "Bingo" 'Hit!' 
run_python_test "XBingo" 'Missed' 
end_python_test


