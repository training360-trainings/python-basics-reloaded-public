import os


def count_txt_files(path='./'):
    files_dict = {}
    for file in os.listdir(path):
        if file.endswith(".txt"):
            file_path = os.path.join(path, file)
            files_dict[file] = os.path.getsize(file_path)
    return files_dict


print(count_txt_files())
