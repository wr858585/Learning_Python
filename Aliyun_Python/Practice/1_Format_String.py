
# Question: Create a variable to store your name and print the following message
# 欢迎xxx同学，SHUFE欢迎你！

name = '大野'
body_part_1 = '欢迎'
body_part_2 = '同学，SHUFE欢迎你！'

# Solution 1. Using string addiction
print(body_part_1 + name + body_part_2)

# Solution 2. Using arguments
print(body_part_1, name, body_part_2)

# Solution 3. Using placeholders
print('欢迎%s同学，SHUFE欢迎你！' % name)

# Solution 4. Using format string
print(f'{body_part_1}{name}{body_part_2}')

# As we can notice, solution 2 appears to be different from the remaining three as there are extra spaces between
# the three parts when run. Reason being arguments of print function generate spaces automatically.

# Solution 4 seems kind of unfamiliar using braces connecting variables but it does the job to convert values into
# string and make printing feasible.