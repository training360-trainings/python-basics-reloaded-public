
# Eldöntés - True, False

def is_contains(values, search):
    for value in values:
        if value == search:
            return True
    return False


val = [10, 20, 30, 40, 50]
print(is_contains(val, 10))

print(10 in val)
