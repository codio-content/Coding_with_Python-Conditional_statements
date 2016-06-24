On the left is the Python code equivalent of the Flode chart from the previous page.

If you run the code you will see that it deals with the conditional statement in exactly the same way as the Flode chart did.

{Run the code}(python3 content/02-if1/if1.py 120)

Have a look how this code works:

An input will be passed to your program on the command line. Command line arguments are accessed like this:

```python
9   argument1= sys.argv[1]   # argument will always be strings
```

Since all command line arguments will be strings, they have to be converted into the type that we want to use them as, in this case, an integer.

```python
10  number = int(argument1)  # to use as an integer
```


And here is the important bit. We are using an `if` statement to check whether `argument1` is greater than 100. If it is, then we output the string 'Big'. Otherwise, we output the string 'Small'.

```python
if number > 100:
  print('Big')
else:
  print('Small')
```

## Reminder

![](.guides/img/simple-if.png
)