import os


def get_lessons_from_module(path):
    with open(path + '/lessons-list', 'w') as file:
        for file_name in os.listdir(path):
            if file_name.endswith('.py'):
                name = file_name[3:] if file_name[0].isdigit() else file_name
                file.write(name.replace('.py', '\n'))


def get_ordered_lessons_list_from_file(path):
    with open(path + '/ordered-list', 'r') as file:
        return file.read().splitlines()


def rename_module_lessons(path):
    ordered_list = get_ordered_lessons_list_from_file(path)
    for file in os.listdir(path):
        if file.endswith('.py'):
            optimized_filename = f'{file[3:]}' if file[0].isdigit(
            ) else f'{file}'
            filename_number_prefix = f'{"%02d" % (ordered_list.index(optimized_filename[:-3]) + 1,)}'
            old_path = f'{path}/{file}'
            new_path = f'{path}/{filename_number_prefix}_{optimized_filename}'
            os.rename(old_path, new_path)


modules = [
    '01-A Python nyelv, fejlesztő környezet, számok és operátorok',
    '02-Alap adattípusok, operátorok',
    '03-A list konténer típus, ciklusok',
    '04-if else vezérlési szerkezet, vezérlési szerkezetek egymásba ágyazása',
    '05-Listák kezelésének haladó technikái',
    '06-Függvények',
    '07-Nevezetes algoritmusok',
    '08-A tuple és a set konténer típusok',
    '09-A dict konténer típus, CRUD műveletek',
    '10-A Python modulrendszere, standard library',
    '11-Fájlkezelés',
    '12-Összetett feladat',
]


def get_lessons_from_all_module():
    for i in modules:
        get_lessons_from_module(i)


def rename_all_module_lessons():
    for i in modules:
        rename_module_lessons(i)


# get_lessons_from_module()
# rename_module_lessons()
rename_all_module_lessons()
