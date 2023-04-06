'''Doc'''

import csv

with open('users.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print([row for row in reader])


with open('users.csv', encoding='utf-8') as csvfile:
    my_list = ['banana', 'apple', 'orange']
    wr = csv.writer(csvfile, delimiter=',')
    wr.writerow(my_list)
