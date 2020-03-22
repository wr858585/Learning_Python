
# Task: Get familiar with advanced functions

# 1. return a function or its return value
print('1. return a function or its return value')


def fn1():
    def fna():
        print('hello')
    return fna  # return the function of fna itself


fn1()           # return:
print(fn1)      # return: <function fn1 at 0x02F51A90>
print(fn1())    # return: <function fn1.<locals>.fna at 0x01701A48>


print('-' * 100)


def fn2():
    def fna():
        print('hello')
    return fna()    # return the result of calling function fna


fn2()           # return: hello
print(fn2)      # return: <function fn2 at 0x02F51A48>
print(fn2())
"""
return:
hello
None 
(Why there is a None? Because it is equivalent to print(fna()) as the return value of fn2 is fna(). See also part 2.)
(We can also analyze it this way: print(fn2()) is different from print(fn2), the former being running the function of 
fn2 and then printing the return value of fn2 (which is to equivalent to print(fna())), the latter being simply 
printing fn2 physical address without running it.)
"""


# 2. A more complicated case
print('2. A more complicated case')


def fn3():
    print('hello')


fn3()           # return: hello
print(fn3)      # return: <function fn3 at 0x00D81A90>
print(fn3())    # return: None (This is why line 34 shows None)

# Advanced functions like these are often used in decorators.
# fn() means calling function fn
# print(fn) means printing the object of function fn
# print(fn()) means printing the result of calling function fn, which is equivalent to calling the function fn and
# printing its return value as well.
