
# Task 1: Create the factorial function using loop and recursion.
print('Task 1: Create the factorial function using loop and recursion.')
print()


def factorial_loop(n):
    for i in range(1, n):
        n *= i
    return n


factorial_loop(10)
print(factorial_loop(10))


def factorial_rec(n):
    if n == 1:
        return 1
    return n * factorial_rec(n-1)


factorial_rec(10)
print(factorial_rec(10))

print()

# 2. Task 2: Create the power function using loop and recursion.
print('Task 2: Create the power function using loop and recursion.')
print()


def power_loop(a, b):
    result = a
    for b in range(1, b):
        result *= a
    return result


power_loop(2, 3)
print(power_loop(2, 3))


def power_rec(a, b):
    if b == 1:
        return a
    return a * power_rec(a, b-1)


power_rec(2, 3)
print(power_rec(2, 3))

print()

# 3. Task 3: Create a function which tests whether a string is palindrome using loop and recursion.
print('Task 3: Create a function which tests whether a string is palindrome using loop and recursion.')
print()


def palindrome(a: str):
    """
        palindrome(a:str) is a function that detects whether a string is palindrome, returning True or False.

        Arguments:
            a: string
    """
