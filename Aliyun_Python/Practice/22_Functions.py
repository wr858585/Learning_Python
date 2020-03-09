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
    a = 20
    print('a =', a)


c = 10
fn(c)
print('c =', c)


def fn2(a):
    a[0] = 30
    print('a =', a)


c = [1, 2, 3]
fn2(c)
print('c =', c)
