# https://docs.python.org/3/library/stdtypes.html#str.format
# https://www.w3schools.com/python/ref_string_format.asp

name = "Gergely"
age = 25

print('My name is', name, 'and I\'m', age, 'years old.')
print('My name is ' + name + ' and I\'m ' + str(age) + ' years old.')
print('My name is {} and I\'m {} years old.'.format(name, age))
print('My name is {0} and I\'m {1} years old. Call me {0}.'.format(name, age))
greeting = 'My name is {0} and I\'m {1} years old. Call me {0}.'.format(
    name, age)
print(greeting)

PI_VALUE = 3.14159265359
print("The value of pi is {:.2f}".format(PI_VALUE))

num = 2
index = '%02d' % num
print(index)
