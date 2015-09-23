
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import test

test.test('boolean-ch/simple.py', [100], [True])
test.test('boolean-ch/simple.py', [101], [True])
test.test('boolean-ch/simple.py', [99], [False])

print('Well done')
