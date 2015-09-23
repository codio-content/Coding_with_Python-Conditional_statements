Now let's see how that chart is written in Python, which you can see on the left. You can run and debug your code by clicking the "Run the code" button below.

{Run the code}(python3 run-user.py 02-if1/if1.py)

Let's analyse how our code works.

The coding challenges you will face will require your programs to take in various inputs. You can do this by calling the provided input functions `input0`, `input1`, `input2` etc. They are numbered, starting at 0 and go up to the amount required for the challenge. The input functions expect a default value, something that makes sense for debugging your code, but when your code is checked by the assessment system these functions will return random values to make sure your code handles many scenarious.

First of all, we are setting the test data `20` for our input variable `input0`, just like we did in Flode.

```python
input0 = input0(20)
```

And here comes the important bit. We are using an `if` statement to check whether `input0` is greater than 100. If it is, then we output the string 'Big'. Otherwise, we output the string 'Small'.

```python
if input0 > 100:
  output('Big')
else:
  output('Small')
```

## Reminder

![](.guides/img/simple-if.png
)