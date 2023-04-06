# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

yearly_salary = (120000, 72000, 57000, 98000, 120000)


# add/insert
yearly_salary_list = list(yearly_salary)
yearly_salary_list.insert(2, 99000)
yearly_salary = tuple(yearly_salary_list)
print(yearly_salary)
