from os import path

file = open(
    file=f'{path.dirname(__file__)}/banana.txt',
    mode='w',
    encoding='utf-8'
)
file.write('Banana')
file.close()
