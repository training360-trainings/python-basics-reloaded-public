import csv
from os import path


def read_csv_file(file):
    with open(f'{path.dirname(__file__)}/{file}', 'r') as file:
        reader = csv.reader(file)
        print([row for row in reader])


read_csv_file('data.csv')
