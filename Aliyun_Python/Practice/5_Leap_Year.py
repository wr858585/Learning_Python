
# Question: Check if the year that user types is leap year.

year = int(input('Please enter the year: '))

if year % 4 == 0:
    print('It is a leap year.')

else:
    print('It is a common year.')
