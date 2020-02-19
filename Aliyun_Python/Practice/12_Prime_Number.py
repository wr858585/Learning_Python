
# Question: Determine whether the number user inputs is a prime number.

num = int(input('Please an integer which is larger than 1: '))
factor = 2
flag = True

if num > 1:
    while factor < num:
        if num % factor == 0:
            flag = False
        factor += 1

    if flag == True:
        print(num, 'is a prime number.')
    else:
        print(num, 'is not a prime number.')
else:
    print('Please enter a valid number.')
