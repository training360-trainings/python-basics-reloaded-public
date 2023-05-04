# 2.

def sum_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        numbers = file.readline().strip().split(',')
        return sum(map(int, numbers))
