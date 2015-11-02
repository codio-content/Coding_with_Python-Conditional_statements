import sys
import test

test.test('challenges/bool-input.py', [True, True], ['cold and rainy'])
test.test('challenges/bool-input.py', [True, False], ['cold and dry'])
test.test('challenges/bool-input.py', [False, True], ['warm and rainy'])
test.test('challenges/bool-input.py', [False, False], ['warm and dry'])

print('Well done')
