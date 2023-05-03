from os import path

with open(file=f'{path.dirname(__file__)}/banana.txt', mode='w') as f:
    f.write('Banana')
