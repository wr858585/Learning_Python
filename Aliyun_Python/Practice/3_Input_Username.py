# Question: Fetch the username that user types in command line and do the following
# Write 'Welcome, admin' if the username is admin/Admin/ADMIN or otherwise do nothing.

# Solution 1: (Incorrect)
#
# username = input('Please enter your username: ')
#
# if username == 'admin' or 'Admin' or 'ADMIN':
#     print(f'Welcome {username}')

# Analysis:
# line 8 appears to be correct and logically coherent as spoken English, but Python interprets it in a different way.
# Python finds that there are three parallel objects being "username == 'admin'", "'Admin'", "'ADMIN'" instead of
# three separate statements being "'username == 'admin'", "username == 'Admin'", and "username == 'ADMIN'".
# As a result, it is equivalent to: if_statement (False or True or True) given input is anything other than admin/Admin
# /ADMIN.

# Solution 2: (Correct)

username = input('Please enter your username: ')

if username == 'admin' or username == 'Admin' or username == 'ADMIN':
    print(f'Welcome {username}')

# Solution 3: (Correct)
