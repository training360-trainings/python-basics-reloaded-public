import os


def get_lessons_from_module():
    with open(path + '/lessons-list', 'w') as file:
        for file in os.listdir(path):
            if file.endswith('.py'):
                name = file[3:] if file[0].isdigit() else file
                file.write(name.replace('.py', '\n'))


def get_ordered_list(path):
    with open(path + '/ordered-list', 'r') as file:
        return file.read().splitlines()


def rename_module_lessons():
    ordered_list = get_ordered_list(path)
    for file in os.listdir(path):
        if file.endswith('.py'):
            old_name = f'{path}/{file[3:]}' if file[0].isdigit() else f'{path}/{file}'
            filename_number_prefix = f'{"%02d" % (ordered_list.index(file[:-3]),)}'
            new_name = f'{path}/{filename_number_prefix}-{file}'
            os.rename(old_name, new_name)


path = './A list típus, vezérlési szerkezetek'
rename_module_lessons()
