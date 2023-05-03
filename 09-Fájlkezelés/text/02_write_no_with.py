from os import path

file = open(f'{path.dirname(__file__)}/banana.txt', 'w', 4096, 'utf-8')
file.write('Banana')
file.close()
