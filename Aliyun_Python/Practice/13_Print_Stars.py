
# Question: Print a picture of stars with height = 32 and width = 7

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
