
# Task: Find all Narcissistic numbers under 1000.

# Background information: Narcissistic numbers are those whose value is equal to the sum of its own digits each raised
# to the power of the number of digits.
# For instance, 153 = 1 ** 3 + 5 ** 3 + 3 ** 3.

# Solution 1: (Incorrect)

# ones_digit = 0
# tens_digit = 0
# hundreds_digit = 0
# num = 100 * hundreds_digit + 10 * tens_digit + ones_digit
# count = 0
#
# while hundreds_digit < 10:
#     while tens_digit < 10:
#         while ones_digit < 10:
#             if num == ones_digit ** 3 + tens_digit ** 3 + hundreds_digit ** 3:
#                 print(f'{count} narcissistic number is {num}')
#                 count += 1
#             ones_digit += 1
#         tens_digit += 1
#     hundreds_digit += 1
#
# Solution 2: (Correct)

num = 100
hundreds_digit = 0
tens_digit = 0
ones_digit = 0
count = 0

while num < 999:
    # print(i) could be used to see all i
    num += 1
    hundreds_digit = num // 100
    tens_digit = (num - 100 * hundreds_digit) // 10
    ones_digit = (num - 100 * hundreds_digit) % 10
    # print(num, hundreds_digit, tens_digit, ones_digit) could be used to see all i with digit retails
    if num == hundreds_digit ** 3 + tens_digit ** 3 + ones_digit ** 3:
        count += 1
        print(f'{num} is the {count} Narcissistic Number.')
