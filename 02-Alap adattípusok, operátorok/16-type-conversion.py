int_value = int('10')
float_value = float('10.10')
# ValueError
# float_value = float('10.10a')
str_value = str(10.10)
bool_value = bool(0)

print(int_value, type(int_value))
print(float_value, type(float_value))
print(str_value, type(str_value))
print(bool_value, type(bool_value))
