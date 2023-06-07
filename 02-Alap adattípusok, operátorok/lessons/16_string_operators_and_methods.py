# string-methods
# https: // docs.python.org/3/library/stdtypes.html
# https://www.w3schools.com/python/python_ref_string.asp

print(f'+ operator: {"Gáll" + "Gergely"}')
print(f'* operator: {"Gergely" * 3}')
print(f'length: {len("Gergely")}')

name = 'Gergely'

print(f'capitalized name: {name.capitalize()}')
print(f'name: {name}')

print(f'convert to uppercase: {name.upper()}')
print(f'all character are lowercase: {name.islower()}')
print(f'the index of "g": {name.find("g")}')
print(f'count of "g": {name.count("g")}')
print(f'replace "e" to "E": {name.replace("e", "E")}')
print('remove leading spaces:',  '  Gergely '.strip())
