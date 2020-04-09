
# Task: Get familiar with various file operations.

file_name = 'demo_1.txt'

try:
    with open(f'../demo/{file_name}', encoding='utf-8') as file_obj:
        content = file_obj.read(6)
        content = file_obj.read(6)
        content = file_obj.read(6)
        print(content)
        print(len(content))
        # 也可以用readline(), readlines()等方法来读取
        # 也可以用for循环来读取，会全部打印出来，且会有空行在每个打印语句中，不想要的话加end=''
        # for t in file_obj:
        #     print(t)
except FileNotFoundError:
    print(f'{file_name}文件不存在')
finally:
    print('操作完毕')
