import sys
import test

test.test('challenges/simple.py', [100], [True])
test.test('challenges/simple.py', [101], [True])
test.test('challenges/simple.py', [99], [False])

print('Well done')
