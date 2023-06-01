# 7.
def filter_dict(original_dict, keys_to_keep):
    filtered_dict = {}
    for key, value in original_dict.items():
        if key in keys_to_keep:
            filtered_dict[key] = value
    return filtered_dict


original = {'a': 1, 'b': 2, 'c': 3}
filtered = filter_dict(original, ['a', 'b'])

print('Original dict:', original)
print('Filtered dict:', filtered)
