file = open('text.txt', 'r')
content = file.read()
print(content)
file.close()

with open('text.txt', 'r') as file:
    print(file.read())


# Writing to a file
with open('text.txt', 'w') as file:
    file.write("Hello, Pythonista!")

# Reading a specific number of characters
with open('example.txt', 'r') as file:
    print(file.read(5))


# Reading one line at a time using readline
with open('example.txt', 'r') as file:
    print(file.readline())


# Reading all lines at once using readlines
with open('example.txt', 'r') as file:
    print(file.readlines())


# Looping over a file object
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')