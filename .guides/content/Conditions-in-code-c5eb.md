Now let's see how that chart is written in Python, which you can see on the left. You can run and debug your code by clicking the "Run the code" button below.

{Run the code}(python3 content/02-if1/if1.py 120)

Let's analyze how our code works.

The coding challenges you will face will require your programs to take in various inputs. Inputs will be passed to your program on the command line. Command line arguments are accessed like this:

```python
9   argument1= sys.argv[1]   # argument will always be strings
```

Since all command line arguments will be strings, we have to convert them into the type that we want to use them as, in this case, an integer.

```python
10  number = int(argument1)  # to use as an integer
```


And here comes the important bit. We are using an `if` statement to check whether `argument1` is greater than 100. If it is, then we output the string 'Big'. Otherwise, we output the string 'Small'.

```python
if number > 100:
  print('Big')
else:
  print('Small')
```

## Reminder

![](.guides/img/simple-if.png
)