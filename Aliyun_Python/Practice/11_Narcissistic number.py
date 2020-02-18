
# Question: Find all Narcissistic numbers under 1000.

# Background information: Narcissistic numbers are those whose value is equal to the sum of its own digits each raised
# to the power of the number of digits.
# For instance, 153 = 1 ** 3 + 5 ** 3 + 3 ** 3.

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

i = 100

while i < 1000:
    print(i)
    i += 1
