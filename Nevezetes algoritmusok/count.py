
# Megszámlálás - adott elem hányszor van benne

def count_values(values, search):
    counter = 0
    for value in values:
        if (value == search):
            counter += 1
    return counter


val = [10, 20, 30, 40, 50]

print(count_values(val, 10))
print(val.count(10))
