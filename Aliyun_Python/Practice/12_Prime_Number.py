
# Task 1: Determine whether the number user inputs is a prime number.

from time import *

begin = time()

num = int(input('Please an integer which is larger than 1: '))
factor = 2
flag = True

if num > 1:
    while factor < num:
        if num % factor == 0:
            flag = False
        factor += 1

    if flag:
        print(num, 'is a prime number.')
    else:
        print(num, 'is not a prime number.')
else:
    print('Please enter a valid number.')

end = time()

print('Time used:', end - begin)

# Blank between questions

print()

# Task 2: Get all prime numbers under 10000.

# Solution 1: Original Answer

begin = time()

num = 2

while num < 10000:
    factor = 2
    flag = True
    while factor < num:
        if num % factor == 0:
            flag = False
        factor += 1
    if flag:
        print(num, 'is a prime number.')
    num += 1

end = time()

print('Time used:', end - begin)

# Blank between solutions

print()

# Solution 2: (Optimized 1st time)

begin = time()

num = 2

while num < 10000:
    factor = 2
    flag = True
    while factor < num:
        if num % factor == 0:
            flag = False
        if not flag:
            break
        factor += 1
    if flag:
        print(num, 'is a prime number.')
    num += 1

end = time()

print('Time used:', end - begin)

# Blank between solutions

print()

# Solution 3: (Optimized 2nd time)

begin = time()

num = 2

while num < 10000:
    factor = 2
    flag = True
    while factor < num:
        if num % factor == 0:
            flag = False
            break
        factor += 1
    if flag:
        print(num, 'is a prime number.')
    num += 1

end = time()

print('Time used:', end - begin)

# Blank between solutions

print()

# Solution 4: (Optimized 3nd time)

begin = time()

num = 2

while num < 10000:
    factor = 2
    flag = True
    while factor <= num ** 0.5:
        if num % factor == 0:
            flag = False
            break
        factor += 1
    if flag:
        print(num, 'is a prime number.')
    num += 1

end = time()

print('Time used:', end - begin)
