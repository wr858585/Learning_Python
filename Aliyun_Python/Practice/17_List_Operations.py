
# Question: Use a range of operations to work with mutable sequences like lists.

chars = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

# 1. Use slicing to obtain certain elements.

print()
print('Slicing')
print()

print(chars[0])     # get a single element indexed 0
print(chars[5])
print(chars[-1])    # get the first element counterclockwise
print(chars[-6])    # get the sixth element counterclockwise

print(chars[0:1])   # a slice of elements including index i and excluding index j
print(chars[0:2])
print(chars[1:4])

print(chars[1:])    # a slice of elements including all starting from index i
print(chars[:5])
print(chars[::])    # same as a copy of list chars

print()

print('-' * 100)

# 2. Use common sequence operations

print('Common sequence operations')
print()

print(chars + chars)
print(chars * 3)

print('沙和尚' in chars)
print('白骨精' not in chars)

print(len(chars))

print(max(chars))
print(min(chars))

print('-' * 100)
print()

# 3. Use methods

print('Methods')
print()

print(chars.index('孙悟空'))
print(chars.index('猪八戒', 0))
print(chars.index('猪八戒', 0, 2))

print(chars.count('孙悟空'))

# It is very important to understand that these operations does not change the original list of chars. Rather, it makes
# a new list containing elements that satisfy the selecting criteria.
