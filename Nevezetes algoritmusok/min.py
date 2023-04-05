
# Minimum kiválasztás


def get_minimum(values):
    min_value = values[0]
    for index in range(1, len(values)):
        if values[index] < min_value:
            min_value = values[index]
    return min_value


val = [10, 20, 30, 40, 50]

print(get_minimum(val))
print(min(val))
