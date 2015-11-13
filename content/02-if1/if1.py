
# This is the input value variable, much like in Flode
# 
# We use int() to make sure the python interpreter knows that 
# we want to treat the command line argument as a number and 
# not as a string.
# 
import sys
number = int(sys.argv[1])

# 
# Check to see if our number is larger than 100
# 
if number > 100:
  print('Big')
else:
  print('Small')
  