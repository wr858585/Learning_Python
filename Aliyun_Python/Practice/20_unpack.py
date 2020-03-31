# 1. The Basics
print('-' * 50)
print('1. The Basics')
print('-' * 50)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])

# print(my_tuple(1)) is wrong as [] means slicing here not exclusively creating a list.
# () [] {} means tuple, list, dictionary, respectively only when creating or calling them.

nums = [1, 2, 3, 4, 5]
print('原版本：', nums, id(nums))
nums[0] = 5
print('第一次修改：', nums, id(nums))  # Slicing does not change physical id of object in RAM.
nums = [6, 7, 8, 9, 10]
print('第二次修改：', nums, id(nums))  # It assigns another object to variable a thus changing the id.

print('-' * 50)

# 2. Unpack
print('2. Unpack')
print('-' * 50)

a, b, c, d, e = nums
print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)
print('e =', e)

a, b = b, a
print('a =', a)
print('b =', b)

# It is more complicated than it seems. The left side is 2 variables whilst the right side is actually a tuple which is
# equivalent to (b, a) as parentheses can be omitted as long as the comma is there telling python that it meas tuple.

a, b, *c = nums
print('a =', a)
print('b =', b)
print('c =', c)     # It returns a list as unpack is a common operation of sequence.

a, *b, c = nums
print('a =', a)
print('b =', b)
print('c =', c)

# List, string，tuple and other sequence types can also be unpacked.

my_list = [1, 2, 3, 4]
*a, b, c = my_list
print('a =', a)
print('b =', b)
print('c =', c)

a, *b, c = 'hello world'
print('a =', a)
print('b =', b)
print('c =', c)

a, b, *c = (1, 2, 3, 4)
print('a =', a)
print('b =', b)
print('c =', c)

# 3. Dictionary
print('3. Dictionary')
print('-' * 50)

profiles = {'name': '孙悟空', 'age': 18, 'gender': '男'}

for i in profiles.items():
    print(i)

for k, v in profiles.items():   # Using unpack to fetch multiple elements in items (keys & values, 双值子序列)
    print(k, v)
