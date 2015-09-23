{Run code}(python3 run-user.py ./logical-ch/fast-cars2.py)

{Check It!|assessment}(test-393850037)

|||guidance
## Solution
```python
input0 = input0(70)
input1 = input1(80)

# Test for both fast cars
if input0 > 70 and input1 > 70:
  output('2 fast cars')
# Test for 1 or the other 
elif input0 > 70 or input1 > 70:
  output('1 fast car')
# So both must be 70 or less
else:
  output('no fast cars')
```
|||