# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

yearly_salary = (120000, 72000, 57000, 98000, 120000)

# change
yearly_salary_list = list(yearly_salary)
yearly_salary_list.remove(98000)
yearly_salary = tuple(yearly_salary_list)
print(yearly_salary)
