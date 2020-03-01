
# Task: Use various tools and methods to change the original list

# 1. Use index to replace or delete elements in list

print()
chars = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
print('Use index to replace or delete elements')
print()

chars[1] = '大野'
print(chars)

del chars[0]
print(chars)

del chars[0:5:2]
print(chars)

print('-' * 100)
print()

# 2. Use slicing to change or delete elements in list

chars = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
print('Use slicing to change or delete elements')
print()

chars[0:2] = ['大野', '杉山']
print(chars)

chars[0:2] = ['大野', '杉山', '小丸子']    # The number of elements may not be the same.
print(chars)

chars[::2] = ['大野', '杉山', '小丸子', '小玉']    # If step exists, the number of elements must be the same.
print(chars)

del chars[::2]
print(chars)

chars[1:3] = []
print(chars)

print('-' * 100)
print()

# 3. Use methods to add elements in list

chars = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
print('Method 1. s.append(x)')
print()

chars.append('大野')
print(chars)

print()

print('Method 2. s.insert(i, x)')
print()

chars.insert(6, '小丸子')      # Insert an element that is just before element indexed i
print(chars)
print()

print('Method 3. s.extend')
print()

chars.extend(['杉山', '小玉'])
print(chars)
print()

new_chars = ['贝吉塔', '孙悟饭', '特兰克斯']      # Equivalent to append multiple elements at the end
chars.extend(new_chars)
print(chars)
print()
print('-' * 100)

# 4. Use methods to delete elements in list

print('Method 1. s.clear()')
print()
chars = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

chars.clear()
print(chars)

print()
chars = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

print('Method 2. s.pop(i)')
result = chars.pop(1)
# A wrong way to do this:
# chars.pop(1)
# result = chars.pop(1)
# print('被删除的值是：', result)
# Consequence: By doing this it deletes elements indexed 0 and 1 since line 93 executes s.pop(1) again in the new list
# that was crafted by line 92. Besides, line 94 will return a wrong element.
print(chars)
print('被删除的值是：', result)

print()

result = chars.pop()    # It removes the last element by default.
print(chars)
print('被删除的值是：', result)

print('Method 3. s.remove(x)')      # It is an x in the parentheses which represents the value instead of index (i)
print()

chars = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']

chars.remove('蜘蛛精')  # s.remove(x) takes excatly one argument
print(chars)

print()
print('-' * 100)

# 5. Use methods to change orders of elements in list

print()
print('Method 1. s.reverse()')

chars = ['孙悟空', '猪八戒', '沙和尚', '唐僧', '蜘蛛精', '白骨精']
chars.reverse()
print(chars)

print()
print('Method 2. s.sort()')

some_letters = list('jklanreiouojvlksanvk')     # Ascending order by default
some_letters.sort()
print(some_letters)

print()
some_letters.sort(reverse=True)     # Descending order
print(some_letters)
