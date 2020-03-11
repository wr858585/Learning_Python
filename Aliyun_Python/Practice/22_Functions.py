# Task 1: Create a function that calculates the product of three numbers.


def tri_product(a, b, c):
    print('%d * %d * %d = %d' % (a, b, c, a * b * c))


tri_product(1, 2, 4)
print()

# Task 2: Create a function that displays different welcome information as per username.


def welcome(a):
    print(f'Welcome {a}')


welcome('大野')

# Task 3: The difference between changing variables and changing objects.


def fn(a):
    a = 20  # Simply assign variable a without affecting c.
    print('a =', a, id(a))


c = 10
fn(c)
print('c =', c, id(c))


def fn2(a):
    a[0] = 30   # Object [1, 2, 3] has been changed.
    print('a =', a, id(a))


c = [1, 2, 3]
fn2(c)
print('c =', c, id(c))


def fn3(b):
    b = 20
    print('b =', b, id(b))


# fn3(b) will get not defined error as b in fn3(b) is a local variable only in fn3.
b = 10
fn3(b)  # b = 20
print('b =', b, id(b))  # b = 10

# The two 'b's are different objects which both have the same value of 'b' but are stored in separate space in RAM.
# They are independent local variable (b in fn3) and global variable.
