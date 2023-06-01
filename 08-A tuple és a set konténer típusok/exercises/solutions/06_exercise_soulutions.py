# 6.
def extend_dict(dict1, dict2):
    for key, value in dict2.items():
        if key in dict1:
            dict1[key] += value
        else:
            dict1[key] = value
    return dict1


dct_1 = {'year': 2023, 'month': 5, 'day': 3}
dct_2 = {'age': 33,  'day': 3}

print(extend_dict(dct_1, dct_2))
