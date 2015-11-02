import sys
import test

test.test('challenges/fast-cars2.py', [70, 70], ['no fast cars'])
test.test('challenges/fast-cars2.py', [71, 70], ['1 fast car'])
test.test('challenges/fast-cars2.py', [70, 71], ['1 fast car'])
test.test('challenges/fast-cars2.py', [71, 71], ['2 fast cars'])

print('Well done')
