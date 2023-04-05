

# Lineáris keresés - adjuk vissza az indexet, ha benne van

def linear_search(values, element):
    for index in range(len(values)):
        if values[index] == element:
            return index
    return -1


val = [10, 20, 30, 40, 50]

print(linear_search(val, 20))

print(val.index(20))
