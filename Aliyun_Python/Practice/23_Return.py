
# Task: Get familiar with return values.

print('1. fn()')


def fn():
    print('hello')


fn()            # Call fn()
print(fn())     # It returns hello and None in 2 lines, representing the command in fn() and return value respectively.
#   Therefore, print a function means to print the callable function first and then print its return value.


print('2. fn2()')


def fn2():
    def fn3():
        print('hello')


print(fn2())    # It only returns None as fn3() is not called. Also keep in mind that print(fn2()) actually calls fn2().


print('3. fn3()')


def fn3():      # It is a global fn3() which is different from local fn3() in fn2(), hence 2 objects even though not
    # recommended.
    def fn4():
        print('hello')
        return 'world'
    return fn4()


print(fn3())
