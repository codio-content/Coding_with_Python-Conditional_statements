
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import test

test.test('logical-ch/categories.py', [6], ['primary school'])
test.test('logical-ch/categories.py', [11], ['primary school'])
test.test('logical-ch/categories.py', [12], ['secondary school'])
test.test('logical-ch/categories.py', [18], ['secondary school'])
test.test('logical-ch/categories.py', [5], ['NA'])
test.test('logical-ch/categories.py', [19], ['NA'])

print('Well done')
