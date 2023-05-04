# 3.
def read_names_from_file(file_path):
    with open(file_path, 'r') as file:
        names = [name.strip() for name in file.readlines()]
        return sorted(names)
