# Átlag

def summa(values):
    sum_value = 0
    for value in values:
        sum_value += value
    return sum_value


val = [10, 20, 30, 40, 50]


def average(values):
    return summa(values / len(values))


print(average(val))
