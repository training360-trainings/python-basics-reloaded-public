# 5.
def find_key_value_pairs(dct, value):
    return [(key, val) for key, val in dct.items() if val == value]


dct = {'year': 2024, 'month': 3, 'day': 3}
value = 3

print(find_key_value_pairs(dct, value))
