with open('text.txt', 'w') as file:
    content = file.read()
    content = content.replace('a', 'A')
    file.write(content)
