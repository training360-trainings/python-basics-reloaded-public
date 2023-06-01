# 4.
def get_value(dct, key):
    if key in dct:
        return dct[key]
    else:
        return 'Nincs ilyen kulcs'


dct = {'alma': 3, 'körte': 4, 'barack': 2}
key = 'alma'
print(get_value(dct, key))  # 3
