import os


def get_lessons_from_module():
    with open(path + '/lessons-list', 'w') as file:
        for file_name in os.listdir(path):
            if file_name.endswith('.py'):
                name = file_name[3:] if file_name[0].isdigit() else file_name
                file.write(name.replace('.py', '\n'))


def get_ordered_list(path):
    with open(path + '/ordered-list', 'r') as file:
        return file.read().splitlines()


def rename_module_lessons():
    ordered_list = get_ordered_list(path)
    for file in os.listdir(path):
        if file.endswith('.py'):
            pass
            old_path = f'{path}/{file}'
            search = f'{file[3:]}' if file[0].isdigit() else f'{file}'
            filename_number_prefix = f'{"%02d" % (ordered_list.index(search[:-3]),)}'
            new_path = f'{path}/{filename_number_prefix}-{file}'
            os.rename(old_path, new_path)


path = './02-Alap adattípusok, operátorok'
# get_lessons_from_module()
rename_module_lessons()
