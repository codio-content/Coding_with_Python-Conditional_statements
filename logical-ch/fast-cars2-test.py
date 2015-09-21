
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import test

test.test('logical-ch/fast-cars2.py', [70, 70], ['no fast cars'])
test.test('logical-ch/fast-cars2.py', [71, 70], ['1 fast car'])
test.test('logical-ch/fast-cars2.py', [70, 71], ['1 fast car'])
test.test('logical-ch/fast-cars2.py', [71, 71], ['2 fast cars'])

print 'Well done'
