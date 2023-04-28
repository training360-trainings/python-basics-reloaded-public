Írj egy Python függvényt, amely visszaadja az adott stringben található szavak számát!

```py
def count_words(string):
    return len(string.split())
```

Készíts egy függvényt, amely paraméterként kap egy string-et és visszaadja azt, hogy a string tartalmaz-e legalább egy nagybetűt! A visszatérési érték bool típusú!

```py
def has_uppercase(string):
    for char in string:
        if char.isupper():
            return True
    return False

# példa használat:
my_string = 'hello World'
print(has_uppercase(my_string))  # True
```

Írj egy függvényt, amely egy lista számokat kap bemenetként, majd visszatér egy új listával, amelyben a számok a kétszeresükkel vannak helyettesítve.

```py
def double_numbers(numbers):
    new_numbers = []
    for num in numbers:
        new_numbers.append(num * 2)
    return new_numbers

```

Írj egy Python függvényt, amely eldönti, hogy egy adott string palindrom-e vagy sem!
Használj slicingot!

```py
def is_palindrome(string):
    return string == string[::-1]
```

Készíts egy függvényt, amely paraméterként kap egy listát és visszaadja azt a listát,amely csak a páros számokat tartalmazza! A megoldás során comprehensiont használj!

```py
def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# példa használat:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_even_numbers(my_list))  # [2, 4, 6, 8, 10]
```

Készíts egy függvényt, amely paraméterként kap két listát és visszaadja azt a listát, amely csak azokat az elemeket tartalmazza, amelyek mindkét listában szerepelnek! Comprehensiont használj!

```py
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

# példa használat:
print(intersection([1,2,3,4],[3,4,5,6]))
```

Készíts egy függvényt `calculate_average`, amelynek paraméterként egy számokat tartalmazó listát kap, és visszaadja számok átlagát!
Készíts egy másik függvényt is `calculate_class_average` névvel, amely paraméterként egy olyan listát kap, ami tuple-öket tartalmaz. A tuple-öknek két eleme van az egyik egy tanuló neve, a másik pedig egy érdemjegy.
pl.: 'students = [("John", 85), ("Jane", 92), ("Mark", 77), ("Sarah", 90)]'
Ez a függvény adja vissza, hogy a teljes osztálynak (list összes eleme) mennyi az átlaga. Ezen a függvényen belül kell meghívnod a `calculate_average` függvényt.

```py
def calculate_average(grades):
    total = sum(grades)
    return total / len(grades)

def calculate_class_average(students):
    grades = []
    for student in students:
        grades.append(student[1])
    return calculate_average(grades)

students = [("John", 85), ("Jane", 92), ("Mark", 77), ("Sarah", 90)]
class_avg = calculate_class_average(students)
print(f"The class average is {class_avg}.")
```

Készíts egy függvényt, amely egy adott szám faktoriálisát számolja ki. A függvénynek egy bemeneti paramétere legyen, amely az egész szám, aminek a faktoriálisát ki kell számolni!  
Tipp: A függvényen belül meg tudod hívni önmagát eltérő paraméterekkel!

```py
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

Írj egy Python függvényt, amely visszaadja az n-edik Fibonacci-számot. A Fibonacci-sorozat első két eleme 0 és 1, majd a következő számok az előző két szám összegeként számolódnak ki. Tehát a sorozat így néz ki: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

A függvénynek egy paramétert kell fogadnia: 'n'. Ha az n kisebb, mint 0, a függvénynek `None` értéket kell visszaadnia, egyébként pedig a megfelelő számot.
Tipp: A függvényen belül meg tudod hívni önmagát eltérő paraméterekkel!

```py
def fibonacci_of(n):
  if n < 0:
    return None
  if n in {0, 1}:  # Base case
    return n
  return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
```

Készíts egy függvényt, amely meghatározza, hogy egy szám prím-e vagy sem!
A függvény paraméterként egy számot kap a visszatérési érték pedig bool típusú érték.

```py
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# példa használat:
print(is_prime(7))  # True
print(is_prime(10)) # False
```
