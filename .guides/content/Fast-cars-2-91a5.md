{Check It!|assessment}(test-393850037)

|||guidance
## Solution
```python

# Get our car speeds from the command line
import sys
speed1 = int(sys.argv[1])
speed2 = int(sys.argv[2])

# Write your code below

# Test for both fast cars
if speed1 > 70 and speed2 > 70:
  print('2 fast cars')
# Test for 1 or the other 
elif speed1 > 70 or speed2 > 70:
  print('1 fast car')
# So both must be 70 or less
else:
  print('no fast cars')
```
|||