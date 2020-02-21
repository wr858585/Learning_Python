
# Question 1: Print a picture of stars with height = 32 and width = 7

# Solution 1: (Correct)

i = 0

while i < 5:
    j = 0
    while j < 5:
        print('*', end='')
        j += 1
    print()
    i += 1

# Blank between solutions

print()

# Solution 2: (Incorrect)

i = 0
j = 0

while i < 5:
    while j < 5:
        print('*', end='')
        j += 1
    print()
    i += 1

# Analysis: This is wrong because the initial expression for loop_j is not in the loop, making it impossible to reset j
# after loop_j ends and python traces back to line 25. Then it becomes while j < 5: which is equivalent to while False:
# since j is still 5 and not reset.

# Note: We can also interpret it by following how python runs the project.
# Solution 1: line 6 >>> line 8-9 >>> line 10-12 for 5 times till j = 5 >>> line 13-14 >>> line 8-9 and j resets to 0
# >>> line 10-12 for 5 times till j =5 >>> line 13-14 >>> ... and this loops for 5 times
# Solution 2: line 22-23 >>> line 25 >>> line 26-28 for 5 times till j = 5 >>> line 29-30 >>> line 25 (True as i = 1)
# >>> line 26 (False as j = 5 and not reset) so skipping line 27-28 >>> line 29-30 >>> line 25 >>> ... So loop_i keeps
# running but there is no more stars printed since loop_j is always skipped.

# Question 2: Print a picture of stars as below
# *
# **
# ***
# ****
# *****

i = 0

while i < 5:
    j = 0
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1

