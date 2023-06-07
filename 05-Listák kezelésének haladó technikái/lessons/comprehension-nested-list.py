# Nested List comprehension
matrix = [[j for j in range(5)] for i in range(5)]
print(matrix)

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)

rpg_games = [
    ['Earthdawn', 'Call of Cthulhu', 'Dungeons & Dragons'],
    ['Rifts', 'M.A.G.U.S', 'Blades in the Dark'],
    ['Star Wars', 'Shadowrun', 'Cyberpunk 2020'],
]

# Nested List comprehension with an if condition
flatten_rpg_games = [
    game for sublist in rpg_games for game in sublist if len(game) > 12
]

print(flatten_rpg_games)
