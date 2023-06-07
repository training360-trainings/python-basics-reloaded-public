# 3.
import random


def roll_the_dice():
    num_dice = int(input('Kérem adja meg a dobókocka darabszámát: '))
    total = 0

    for i in range(num_dice):
        dice_value = random.randint(1, 6)
        while dice_value == 6:
            dice_value = random.randint(1, 6)
        total += dice_value

    return total


print(roll_the_dice())
