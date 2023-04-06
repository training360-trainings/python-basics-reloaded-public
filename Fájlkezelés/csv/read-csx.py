import csv

# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

fields = []
rows = []
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        rows.append(row)
    print("Total no. of rows: %d" % (reader.line_num))

print('Field names are: ' + ', '.join(field for field in fields))

for row in rows:
    for col in row:
        print("%15s" % col, end=" "),
    print('\n')
