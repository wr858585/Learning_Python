
# Task: Get familiar with advanced functions

# 1. return a function or its return value
print('1. return a function or its return value')


def fn1():
    def fna():
        print('hello')
    return fna


fn1()           # return:
print(fn1)      # return: <function fn1 at 0x02F51A90>
print(fn1())    # return: <function fn1.<locals>.fna at 0x01701A48>


print('-' * 100)


def fn2():
    def fna():
        print('hello')
    return fna()


fn2()           # return: hello
print(fn2)      # return: <function fn2 at 0x02F51A48>
print(fn2())
"""
return:
hello
None
"""
