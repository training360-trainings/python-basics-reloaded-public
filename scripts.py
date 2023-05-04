import os


def get_lessons_from_module():
    with open(path + '/lessons-list', 'w') as file:
        for file_name in os.listdir(path):
            if file_name.endswith('.py'):
                name = file_name[3:] if file_name[0].isdigit() else file_name
                file.write(name.replace('.py', '\n'))


def get_ordered_lessons_list_from_file(path):
    with open(path + '/ordered-list', 'r') as file:
        return file.read().splitlines()


def rename_module_lessons():
    ordered_list = get_ordered_lessons_list_from_file(path)
    for file in os.listdir(path):
        if file.endswith('.py'):
            optimized_filename = f'{file[3:]}' if file[0].isdigit(
            ) else f'{file}'
            filename_number_prefix = f'{"%02d" % (ordered_list.index(optimized_filename[:-3])+1,)}'
            old_path = f'{path}/{file}'
            new_path = f'{path}/{filename_number_prefix}_{optimized_filename}'
            os.rename(old_path, new_path)


path = './04-Függvények/lessons/'
# get_lessons_from_module()
rename_module_lessons()
