# 1.

file_name = 'user_data.txt'
user_name = input('Add meg a neved: ')
with open(file_name, 'w') as file:
    file.write(user_name)
