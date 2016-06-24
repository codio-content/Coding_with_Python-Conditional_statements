Now we are going to look in more detail at how the `if` statement works. Here is the full code again:

```python
if number > 100:
  print('Big')
else:
  print('Small')
```

First, have a look at the first line:

## The if statement
```python
if number > 100:
```

1. You start your line with `if`.
1. You then specify the condition . 
1. Finally, at the end of the line you add a `:`, to end the statement. 

## If the condition is true
**If** the condition is true, then you carry out all the instructions that come after it and are indented. In this example there is only one instruction.

```python
  print('Big')
```

Everything after the statement is called a *code block*. The block ends when the indentation level decreases at the `else` keyword.  

## Otherwise
If the condition is **not true**, the `else` code block executes instead.

```python
  print('Small')
```
