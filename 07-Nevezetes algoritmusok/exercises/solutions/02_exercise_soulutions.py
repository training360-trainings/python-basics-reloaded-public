# 2.
def has_uppercase(string):
    for char in string:
        if char.isupper():
            return True
    return False


print(has_uppercase('Banana'))
