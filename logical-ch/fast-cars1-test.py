
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import test

test.test('logical-ch/fast-cars1.py', [70, 70], ['ok'])
test.test('logical-ch/fast-cars1.py', [71, 70], ['fast cars'])
test.test('logical-ch/fast-cars1.py', [70, 71], ['fast cars'])
test.test('logical-ch/fast-cars1.py', [71, 71], ['fast cars'])

print 'Well done'
