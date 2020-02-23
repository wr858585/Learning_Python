
# Question: Print the multiplication table.

# Solution 1: Use placeholders

i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        print("%d * %d =" % (j, i), i * j, end='    ')
    print()

# Blank between solutions
print()

# Solution 2: Use format string

i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        print(f'{j} * {i} = {i * j}', end='    ')
    print()
