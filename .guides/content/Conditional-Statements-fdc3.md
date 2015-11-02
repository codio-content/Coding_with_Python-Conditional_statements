This Unit covers the concept of conditional statements in Python.

Here's a good example.

```python
if number >= 10 and number < 100: # if number is two digits
  print('2 digit number')         # output 2 digit result
elif number >= 100:               # otherwise, if number more than 2 digits
  print('multi digit number')     # output multi digit result
else:                             # otherwise 
  print('1 digit number')         # must be 1 digit
```

> *If number is greater than or equal to 10 **and** number is less than 100, **then** output '2 digit number' **otherwise if** number is greater than or equal to 100 output 'multi digit number' **otherwise** output '1 digit number'*
