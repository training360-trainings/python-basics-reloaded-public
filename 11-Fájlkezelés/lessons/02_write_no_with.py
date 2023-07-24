# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, Pythonista!")


# Writing multiple lines to a file
lines = ["Hello, Pythonista!\n", "Welcome to the world of Python.\n"]
with open('example.txt', 'w') as file:
    file.writelines(lines)


# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\nKeep on learning!")