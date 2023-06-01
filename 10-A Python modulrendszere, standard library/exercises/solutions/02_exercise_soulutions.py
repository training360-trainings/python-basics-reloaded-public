# 2.
import random


def game():
    number = random.randint(1, 100)
    guess = None
    count = 0
    while guess != number:
        guess = int(
            input('Gondoltam egy számra 1 és 100 között. Melyikre gondoltam? '))
        count += 1
        if guess == number:
            print(f'Gratulálok, eltaláltad a számot {count}. próbálkozásra!')
        elif guess < number:
            print('A gondolt szám nagyobb a megadott számnál.')
        else:
            print('A gondolt szám kisebb a megadott számnál.')


game()
