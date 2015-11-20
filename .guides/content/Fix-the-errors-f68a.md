{Check It!|assessment}(test-1180993407)

|||guidance
## Solution

- the else is missing a `:`
- the equals comparison is a `=` instead of `==`

```python
import sys
str = sys.argv[1]

if str == 'there':
  print(0)
else:
  print(1)
```
|||