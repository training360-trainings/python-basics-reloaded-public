

def maximum(values):
    max_value = values[0]
    for index in range(1, len(values)):
        if values[index] > max_value:
            max_value = values[index]
    return max_value


val = [10, 20, 30, 40, 50]
print(maximum(val))
print(max(val))
