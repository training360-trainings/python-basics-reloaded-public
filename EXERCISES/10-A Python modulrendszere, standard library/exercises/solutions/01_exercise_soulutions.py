# 1.
import datetime


def calculate_age():
    birthyear = int(input('Add meg a születési éved: '))
    if birthyear > datetime.datetime.now().year:
        return 'Még nem járunk ebben az évben.'
    actual_year = datetime.date.today().year
    return actual_year - birthyear


print(calculate_age())
