my_dict = {'one': 1, 'two': 2, 'three': 3}
a, b, c = my_dict  # Unpack keys
print(a, b, c)

a, b, c = my_dict.values()  # Unpack values
print(a, b, c)

a, b, c = my_dict.items()  # Unpacking key-value pairs
print(a, b, c)
