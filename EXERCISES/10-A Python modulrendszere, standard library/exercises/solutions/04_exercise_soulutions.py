# 4.
import os


def get_directory_size(path='.'):
    total_size = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total_size += entry.stat().st_size
            elif entry.is_dir():
                total_size += get_directory_size(entry.path)
    return total_size


print(get_directory_size('./'), 'byte')
