file = open('birds.txt', 'r')
observation_count = int(file.readline())
birds = file.readline().split(' ')
print(birds)
