import sys
import test

test.test('challenges/categories.py', [6], ['primary school'])
test.test('challenges/categories.py', [11], ['primary school'])
test.test('challenges/categories.py', [12], ['secondary school'])
test.test('challenges/categories.py', [18], ['secondary school'])
test.test('challenges/categories.py', [5], ['NA'])
test.test('challenges/categories.py', [19], ['NA'])

print('Well done')
