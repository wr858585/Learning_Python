
# Question: Print the multiplication table.

i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        print("%d * %d =" % (j, i), i * j, end='    ')
    print()
