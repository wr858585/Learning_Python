
# Task: Determine whether the number that user types is an odds or even.

number = int(input('Please type a number: '))

if number % 2 == 0:
    print('It is an even.')

else:
    print('It is an odds.')

# Another approach: use print function arguments to display input and other text combined.
# print(number, 'is an even.')
# print(number, 'is an odds.')
