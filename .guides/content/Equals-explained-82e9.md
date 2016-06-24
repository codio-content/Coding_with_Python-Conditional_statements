The "equals" condition is used in many programming languages. 

In Python (and many other programming languages) `=` is the *assignment operator*, not a comparison operator. That means you use `==` to compare things and `=` to set variables. 

In summary, you use `==` and **not** `=`.

Have a look at the Flode chart on the left. Below is the Python code equivalent:

```python
if number == 100:
  print('Is 100')
else:
  print('Is not 100')
```

Have a close look at the Python code below to make sure you understand it.

```python
number = 10  # assign 10 to the variable number
number == 10 # test to see if number is equal to 10
```

Accidentally confusing `=` and `==` is a common beginner's mistake. So be careful when you are using equals signs. 