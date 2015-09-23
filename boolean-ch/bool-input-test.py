
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import test

test.test('boolean-ch/bool-input.py', [True, True], ['cold and rainy'])
test.test('boolean-ch/bool-input.py', [True, False], ['cold and dry'])
test.test('boolean-ch/bool-input.py', [False, True], ['warm and rainy'])
test.test('boolean-ch/bool-input.py', [False, False], ['warm and dry'])

print('Well done')
