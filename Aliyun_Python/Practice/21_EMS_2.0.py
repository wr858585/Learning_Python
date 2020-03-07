# Task: Create a Employee Management System with functions of search, add, and delete employees.

print('=' * 10, '欢迎进入员工管理系统', '=' * 10)


def narrative():
    print('''
请选择要执行的操作：
    1.查询员工
    2.添加员工
    3.删除员工
    4.退出系统
    ''')


title = '\t序号\t姓名\t年龄\t性别\t住址'
employees = ['\t\t孙悟空\t18\t\t男\t\t花果山']

while True:
    narrative()
    choice = input('请输入（1-4）：')
    if choice == '1':
        print(title)
        i = 1
        for emp in employees:
            print(f'\t{i}{emp}')
            i += 1
    elif choice == '2':
        name = input('请输入员工的姓名：')
        age = input('请输入员工的年龄：')
        gender = input('请输入员工的性别：')
        address = input('请输入员工的地址：')
        employees.append(f'\t\t{name}\t{age}\t\t{gender}\t\t{address}')
    elif choice == '3':
        delete_num = int(input('请输入要删除员工的序号：'))
        employees.pop(delete_num - 1)
    elif choice == '4':
        print('谢谢使用，程序已退出')
        break
    else:
        print('输入有误，请输入一个1-4的数字')
