Take a look at the Flode chart on the left. This contains 2 conditional blocks where you can see `and` and `or` being used.

Below is the equivalent Python code. Try different values for `number`.

```python
number = -10  # Change the value of number and step through 

if number >= 10 and number < 100: # Example of 'and'
  output('2 digit number')
else:
  output('1 digit number')

if number < 0 and number >= 1000: # Example of 'or'
  output('Invalid number')
else:
  output('OK')
```
