with open('text.txt', 'r+') as file:
    content = file.read()
    content = content.replace('a', 'A')
    file.seek(0)
    file.write(content)
