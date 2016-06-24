This is very important, so please read it carefully.

## Indenting your code
Indentation means leaving an empty space between the left margin and the beginning of a line of code. In Python, indentation is required - if you do not indent your code properly, it will not run.

In other languages, such as JavaScript, your code will run fine without indentation but it will look messy and can be hard for others to read and understand.

Have a look at the Python code below which is written without indentations. The code will not run because there is no indentation. Python does not recognise anything as being contained within the `if` and `else` code blocks.

```python
if number > 100:
print('Big')
else:
print('Small')
```

## What code should you indent?
You should indent all code within a code block. Code blocks start with the `:` character.

```python
if number > 100:
  code here
  and here
  and here
  all indented
```

You will see other statements soon that also have code blocks, such as loops. These should be indented too.

```python
while counter <= 9:
  print counter
  counter = counter + 1
```

## How do you indent code?
Press the tab key at the beginning of a new line to indent your code. (The tab key is the key with two arrows pointing in opposite directions).
Sometimes beginners press the space bar several times to indent their code. **Don’t do this**.
Always use the tab key instead. This ensures that indentations are consistent.
