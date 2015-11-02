import sys
import test

test.test('challenges/neq.py', ['BingoX'], ['Missed'])
test.test('challenges/neq.py', ['Bingo'], ['Hit!'])

print('Well done')
