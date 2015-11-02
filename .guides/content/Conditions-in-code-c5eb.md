Now let's see how that chart is written in Python, which you can see on the left. You can run and debug your code by clicking the "Run the code" button below.

{Run the code}(python3 run-user.py content/02-if1/if1.py 120)

Let's analyse how our code works.

The coding challenges you will face will require your programs to take in various inputs. Inputs will be passed to your program on the command line. Command line arguments are accessed like this:

```python
argument1 = sys.argv[2] # first argument
argument2 = sys.argv[3] # second argument
argument3 = sys.argv[4] # third argument

# sys.argv[0] -> the interpreter's name
# sys.argv[1] -> the name of the python file
```

And here comes the important bit. We are using an `if` statement to check whether `argument1` is greater than 100. If it is, then we output the string 'Big'. Otherwise, we output the string 'Small'.

```python
if argument1 > 100:
  print('Big')
else:
  print('Small')
```

## Reminder

![](.guides/img/simple-if.png
)