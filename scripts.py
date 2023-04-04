import os


def get_lessons_from_a_module(path):
    with open(path + '/order-list', 'w') as file:
        for i in os.listdir(path):
            if i.endswith('.py'):
                file.write(i.replace('.py', '\n'))


def get_ordered_list(path):
    with open(path + '/order-list', 'r') as file:
        return file.read()


def rename_module_lessons(path):
    for i, v in enumerate(os.listdir(path)):
        if v.endswith('.py'):
            old_name = f'{path}/{v}'
            new_name = f'{path}/{"%02d" % (i,)}-{v}'
            print(old_name, new_name)


path = './A list típus, vezérlési szerkezetek'
ordered_list = get_ordered_list(path)
rename_module_lessons(path)
