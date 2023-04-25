# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# unchangeable = immutable
# Faster than list

yearly_salary = (120000, 72000, 57000, 98000, 120000)
print(yearly_salary[0])
# yearly_salary [1] = 1990
# TypeError: 'tuple' object does not support item assignment

print(len(yearly_salary))
print(yearly_salary.count(120000))
print(yearly_salary.index(120000))
