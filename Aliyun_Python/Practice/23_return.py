
# Task: Get familiar with return values.

print('1. fn()')


def fn():
    print('hello')


fn()            # Call fn()
print(fn())     # It returns hello and None in 2 lines, representing the command in fn() and return value respectively.
#   Therefore, print a function means to print the callable function first and then print its return value.


print('2. fn2()')


def fn2():
    def fn3():   # Even though fn3 here is defined in fn2 without conflicts of global fn2, still better rename it.
        print('hello')

fn2()
print(fn2())    # It only returns None as fn3() is not called. Also keep in mind that print(fn2()) actually calls fn2().


print('3. fn3()')


def fn3():      # It is a global fn3() which is different from local fn3() in fn2(), hence 2 objects even though not
    # recommended.
    def fn4():
        print('hello')
        return 'world'
    return fn4()


fn3()
print(fn3())


print('4. fn4')


def fn4():
    def fn5():
        print('hello')
    return fn5      # It only returns the function without calling it. Therefore, the code in the function will not run.


fn4()
print(fn4())
print(fn4)


print('5. return result rather than print result')

print(print(1))     # It shows that print function does not have a return value


def sum_print_result(*nums):
    result = 0
    for i in nums:
        result += i
    print(result)


def sum_return_result(*nums):
    result = 0
    for i in nums:
        result += i
    return result


a = sum_print_result(1, 2, 3)       # Will display the result which is 6.
b = sum_return_result(2, 3, 4)      # No result displayed.

# print(a + 1) will cause trouble even hindering the line 79 being executed and shown. Consequently, The function
# sum_print_result has very limited use.

print(b + 1)    # The result in sum_return_result is easy to use and call when necessary.
