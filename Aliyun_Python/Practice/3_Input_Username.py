# Question: Fetch the username that user types in command line and do the following
# Write 'Welcome, admin' if the username is admin/Admin/ADMIN or otherwise do nothing.

username = input('Please enter your username: ')

if username == 'admin' or 'Admin' or 'ADMIN':
    print(f'Welcome {username}')
