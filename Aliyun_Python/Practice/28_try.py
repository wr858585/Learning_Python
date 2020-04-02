# Task: Try to use try statement

print('hello')

try:
    print(10 / 0)
except:
    print('哈哈哈，出错啦')
else:
    print('程序正常，可以运行')

print('bye')        # bye会照常执行，程序不会退出。这就是try语句的意义

print('-' * 100)

print('异常出现前')

try:
    print(c)
    print(10/0)
except NameError:
    print('出现NameError异常')

print('异常出现后')
