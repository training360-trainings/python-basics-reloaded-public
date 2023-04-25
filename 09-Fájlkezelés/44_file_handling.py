# # file handling

# # 1) without using with statement
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()

# # 2) without using with statement
# file = open('file_path', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()


# # using with statement
# with open('file_path', 'w') as file:
#     file.write('hello world !')

# with open('text.txt', 'w', 4096, 'utf-8') as file:
#     file.write('Banana')

file = open('text.txt', 'w', 4096, 'utf-8')
file.write('Banana')
file.close()

file = open('text.txt', 'r')
content = file.read()
print(content)

with open('text2.txt', 'r') as file2:
    # teljes tartalom beolvasása
    print(file2.read())
    # vissza a file elejére
    # vissza a file elejére
    file2.seek(0)
    # egy sor kiolvasása
    print(file2.readline())
    # vissza a file elejére
    file2.seek(0)
    # soronként bejárás
    for line in file2:
        print(line, end='')
    # vissza a file elejére
    file2.seek(0)
    # két akarakter kiolvasása
    print(file2.read(2))
