# 1.
def count_words(string):
    return len(string.split())


print(count_words('Banana'))

# 2.


def has_uppercase(string):
    for char in string:
        if char.isupper():
            return True
    return False


print(has_uppercase('Banana'))

# 3.


def double_numbers(numbers):
    new_numbers = []
    for num in numbers:
        new_numbers.append(num * 2)
    return new_numbers


print(double_numbers('Banana'))

# 4.


def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome('apa'))

# 5.


def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]


print(filter_even_numbers(1, 2, 3, 4, 5, 6))

# 6.


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


print(intersection([1, 2, 3, 4], [3, 4, 5, 6]))

# 7.


def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)


def calculate_class_average(students):
    grades = []
    for student in students:
        grades.append(student[1])
    return calculate_average(grades)


students = [("John", 85), ("Jane", 92), ("Mark", 77), ("Sarah", 90)]
print(calculate_class_average(students))

# 8.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(8))

# 9.


def fibonacci_of(n):
    if n < 0:
        return None
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


print(fibonacci_of(10))

# 10.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(7))
print(is_prime(10))
