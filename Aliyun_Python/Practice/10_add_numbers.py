
# Task: Get the sum of all positive numbers under 100 that can be divided by 7. Count how many numbers satisfying
# the requirement.

# Solution 1: while and if statements

num = 0
result = 0
count = 0

while num < 100:
    num += 1
    if num % 7 == 0:
        result += num
        count += 1

print('sum =', result)
print('amount =', count)

# Solution 2: change the default/initial variable values

num = 7
result = 0
count = 0

while num < 100:
    result += num
    num += 7
    count += 1

print('sum =', result)
print('amount =', count)

