def is_even_number(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


def is_even_number(num):
    if num % 2 == 0:
        return 'Even'
    return 'Odd'


def is_even_number(num):
    return 'Even' if num % 2 == 0 else 'Odd'


print(is_even_number(10))

a = 11
b = 'Even' if a % 2 == 0 else 'Odd'

print(b)
