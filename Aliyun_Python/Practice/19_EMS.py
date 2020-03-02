
# Task: Create a Employee Management System with functions of search, add, and delete employees.

print('=' * 10, '欢迎使用员工管理系统', '=' * 10)
narrative = str('''请选择要做的操作：
\t1.查询员工
\t2.添加员工
\t3.删除员工
\t4.退出系统''')

numbers = [1]
names = ['孙悟空']
ages = ['18']
genders = ['男']
addresses = ['花果山']
j = 1

while True:
    print(narrative)
    choice = input('请选择（1-4）：')
    if choice == '1':
        i = 1
        print('\t序号\t姓名\t年龄\t性别\t住址')
        for a in numbers:
            print(f'\t{i}\t\t{names[i-1]}\t{ages[i-1]}\t\t{genders[i-1]}\t\t{addresses[i-1]}')
            i += 1
            # It is i-1 in the brackets as a is in list 'numbers' and the first element is 1.
            # Loop i needs to be in if_statement == '1' or otherwise there would be issues deleting employees since\
            # the number would be attached to the person.
    elif choice == '2':
        j += 1
        numbers.append(j)
        emp_name = input('请输入员工的名字：')
        names.append(emp_name)
        emp_age = input('请输入员工的年龄：')
        ages.append(emp_age)
        emp_gender = input('请输入员工的性别：')
        genders.append(emp_gender)
        emp_address = input('请输入员工的住址：')
        addresses.append(emp_address)
    elif choice == '3':
        delete_emp = input('请输入想删除员工的名字：')
        if delete_emp in names:
            index = names.index(delete_emp)
            numbers.pop(index)
            names.pop(index)
            ages.pop(index)
            genders.pop(index)
            addresses.pop(index)
        else:
            print('该员工不存在')
    elif choice == '4':
        input('谢谢使用，按回车键退出。')
        break
    else:
        print('请输入一个合法的值')
