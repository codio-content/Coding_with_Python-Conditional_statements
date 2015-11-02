This is very important, so please read it carefully.

## Indenting your code
In languages like Python, indentation is *required*. If you don't indent you code properly, it will not run.

In some languages like Javascript, your code will run fine without indentation but it will look messy if you don't.

The Python code below will not run as, due to the lack of indentation, Python does not recognise anything as being contained in the `if` and `else` code blocks.

```python
if number > 100:
print('Big')
else:
print('Small')
```

## What code should you indent?
You should indent all code within a code block. Code blocks start with the ':'.

```python
if number > 100:
  code here
  and here
  and here
  all indented
```

You will see other statements soon that also have code blocks, such as loops. The same applies here.

```python
while counter <= 9:
  print counter
  counter = counter + 1
```

## Tab key NOT spaces
One thing that beginners do when indenting their code is to press the space bar several times. **Don't do this**.

Use the tab key instead. This ensures that indentations are consistent.
