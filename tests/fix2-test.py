import sys
import test

test.test('challenges/fix2.py', ['Bingo'], ['Hit!'])
test.test('challenges/fix2.py', ['BingoX'], ['Missed'])

print('Well done')
