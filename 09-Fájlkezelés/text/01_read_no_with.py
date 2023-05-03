from os import path

file = open(f'{path.dirname(__file__)}/text.txt', 'r')
content = file.read()
print(content)
