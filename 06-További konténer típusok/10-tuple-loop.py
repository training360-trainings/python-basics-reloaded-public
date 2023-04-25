# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

yearly_salary = (120000, 72000, 57000, 98000, 120000)

for i in yearly_salary:
    print(i)

for i in range(len(yearly_salary)):
    print(i, yearly_salary[i])

for i, v in enumerate(yearly_salary):
    print(i, v)
