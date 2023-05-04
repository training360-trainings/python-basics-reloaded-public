import random

# Egész számok generálása 1 és 100 között
szam = random.randint(1, 100)

print(szam)

# Keverés
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)

print(lista)

# Véletlenszerű választás
my_list = ['apple', 'banana', 'cherry', 'date']
random_item = random.choice(my_list)
print(random_item)
