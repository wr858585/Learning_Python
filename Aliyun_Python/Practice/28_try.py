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
except NameError as exc:    # 这样就只会捕获指定的NameError
    print('出现NameError异常', exc, type(exc))

print('异常出现后')

print('-' * 100)

print('文件操作的标准方式')

file_name = 'hello'

try:
    with open(file_name) as file_obj:
        print(file_obj.read())
except FileNotFoundError:
    print(f'{file_name}文件不存在')

