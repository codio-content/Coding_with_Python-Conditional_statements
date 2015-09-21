
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

import test

test.test('03-ch-if-1/1-0.py', [1], ['On'])
test.test('03-ch-if-1/1-0.py', [0], ['Off'])

print 'Well done'
