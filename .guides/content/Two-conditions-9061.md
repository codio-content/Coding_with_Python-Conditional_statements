Now let's look at another example. Look at the Flode chart on the left. Step through the chart and you will see it works as follows:

> If the number is less than or equal to 100, output 'Small’. If the number is larger than 100 then if it is also larger than 200, output ‘Huge’ otherwise output 'Big’.

## elif
Have a look at the second condition. It uses the following statement:

```python
elif input0 > 200:
```

Using `elif` means that this line will only execute if the first `if` condition was `false`.

Here is the general way Python evaluates its `if` statements.

```python
if condition1:
  do something
elif condition2:
  do something else
elif condition3:
  do something else
else:
  otherwise do this
```

- The first `if` condition is evaluated. If it is true, then its code block will execute and execution will then jump to the end of all the `if / else` statements.
- If it was false, then all `elif` conditions will be evaluated in turn until one of them has a `true` condition.
- If none of the `if` or `elif` conditions evaluate to `true`, then the `else` code block will automatically execute (if it is used).

