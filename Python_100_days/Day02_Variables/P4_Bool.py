# Bool is short for Boolean which is a value as either True or False

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1 != 2)
print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print('flag5 =', flag5)
print(flag1 is True)
print(flag2 is not False)
print('\u0040')

# Please note != means not equal to sth
# In line 17, \u0040 (any \uxxxx) is a variation of escaping characters (\u) but it means to match the corresponding
# characters or symbols of 0040 as per universal character code like UTF-8. However, the result is a string and should
# not be printed without quotes or otherwise object not defined.
