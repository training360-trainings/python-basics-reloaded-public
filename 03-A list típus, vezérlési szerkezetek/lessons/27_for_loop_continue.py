yearly_salary_list = [120000, 72000, 57000, 98000]
high_salary_filter = 100000

for salary in yearly_salary_list:
    if salary > high_salary_filter:
        continue
    print(salary)


for salary in yearly_salary_list:
    if salary < high_salary_filter:
        print(salary)
