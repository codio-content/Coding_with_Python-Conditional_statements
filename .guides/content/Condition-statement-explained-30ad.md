Now let's analyse how the `if` statement works. Here's the full code again.

```python
if number > 100:
  print('Big')
else:
  print('Small')
```

Let's start with the first line.

## The if statement
```python
if number > 100:
```

1. You start your line with `if`.
1. You then specify the condition . 
1. Finally, at the end of the line you add a `:`, to end the statement. 

## If the condition is true
**If** this condition is true, then you execute all the instructions that come after it and are indented. There is only one instruction in this example.

```python
  print('Big')
```

Everything after the statement is called a *code block*. The block ends when the indentation level decreases at the `else` keyword.  

## Otherwise
If the condition is **not true**, then execute the `else` code block.

```python
  print('Small')
```
