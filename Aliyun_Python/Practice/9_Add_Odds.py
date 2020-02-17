# Question: Add all positive odds numbers under 100.

# Solution 1: while + if statements

num = 0
result = 0

while num < 100:
    num += 1
    if num % 2 != 0:
        result += num

print('result = ', result)

# Solution 2: change the default/initial variable value

num = 1
result = 0

while num < 100:
    result += num
    num += 2

print('result = ', result)
