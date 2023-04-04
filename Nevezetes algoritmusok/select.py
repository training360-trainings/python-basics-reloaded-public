# Kiválasztás - tudjuk, hogy benne van, az index kell

def get_index(values, element):
    for index in range(len(values)):
        if values[index] == element:
            return index


val = [10, 20, 30, 40, 50]
print(get_index(val, 20))
print(val.index(20))
