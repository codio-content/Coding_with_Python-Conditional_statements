
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import test

test.test('03-ch-if-1/true-false.py', ['true'], [1])
test.test('03-ch-if-1/true-false.py', ['false'], [0])

print('Well done')
