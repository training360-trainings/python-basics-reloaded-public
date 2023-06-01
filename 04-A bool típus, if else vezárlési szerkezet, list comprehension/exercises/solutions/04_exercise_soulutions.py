# 4.
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = [num for num in input_list if num % 2 != 0]
evens = [num for num in input_list if num % 2 == 0]

print(f'odds: {odds}, evens: {evens}')
