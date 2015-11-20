{Check It!|assessment}(test-484914084)

|||guidance
## Solution

- on the `if` line, we have are missing `!=`
- the `if` line is missing the `:`

```python
# Get our input from the command line
import sys
string = sys.argv[1]

# Your code goes here
if string != 'Bingo':
  print('Missed')
else:
  print('Hit!')
```
|||