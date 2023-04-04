import os


def get_lessons_from_a_module(path):
    with open(path + '/order-list', 'w') as file:
        for x in os.listdir(path):
            if x.endswith('.py'):
                file.write(x.replace('.py', '\n'))


def order_module_lessons():
