{Check It!|assessment}(test-2697509729)

|||guidance
## Solution
```python

# Get our boolean values from the command line
import sys
isCold= sys.argv[1] == 'True'
isRainy= sys.argv[2] == 'True'

# Your code goes here

if isCold:                   # is it cold?
  if isRainy:                # is it rainy?
    print('cold and rainy')
  else:                      # cold, but not rainy
    print('cold and dry')
else:                        # not cold, so must be warm
  if isRainy:                # is it rainy?
    print('warm and rainy')
  else:
    print('warm and dry')
```
|||