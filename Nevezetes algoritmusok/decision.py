
# Eldöntés - True, False

def contains_or_not(values, search):
    for value in values:
        if value == search:
            return True
    return False


val = [10, 20, 30, 40, 50]
print(contains_or_not(val, 10))
print(10 in val)
