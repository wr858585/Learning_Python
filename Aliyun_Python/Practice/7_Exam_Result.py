
# Task: Give Tom rewards as per his final exam result.

result = int(input("Tom's final exam result: "))

if result > 100 or result < 0:
    print('Please enter a valid number.')

elif result == 100:
    print('You get yourself a BMW!')

elif result >= 80:
    print('You get an IPhone!')

elif result >= 60:
    print('You get a reference book.')

else:
    print('You get nothing.')
