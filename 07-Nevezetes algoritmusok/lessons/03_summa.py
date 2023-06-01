# Összegzés

def summa(values):
    sum_value = 0
    for value in values:
        sum_value += value
    return sum_value


val = [10, 20, 30, 40, 50]

print(summa(val))
print(sum(val))
