import sys
import test

test.test('challenges/fast-cars1.py', [70, 70], ['ok'])
test.test('challenges/fast-cars1.py', [71, 70], ['fast cars'])
test.test('challenges/fast-cars1.py', [70, 71], ['fast cars'])
test.test('challenges/fast-cars1.py', [71, 71], ['fast cars'])

print('Well done')
