# Task: Get familiar with binary file operations

file_name = 'demo_binary.jpg'

with open(f'../demo/{file_name}', 'rb') as file_obj:
    new_name = 'demo_2.jpg'
    with open(new_name, 'wb') as new_obj:
        chunk = 1024 * 100          # 1024 bytes * 100 == 100 kb
        while True:
            content = file_obj.read(chunk)
            new_obj.write(content)
            if not content:         # content is None after all is read.
                break
