# Question: Find the max value of the three variables a, b, and c using if logic, values of which are 10, 20, and 30
# respectively

a = 10
b = 20
c = 30

# Solution 1: if-elif-else logic

if a == max(a, b, c):
    print(a)

elif b == max(a, b, c):
    print(b)

else:
    print(c)

# Solution 2:

Max = a if a > b else b
Max = Max if b > c else c
print(Max)

# Solution 3:

Max = a if a > b and a > c else b if b > c else c
print(Max)


