yearly_salary_list = [120000, 72000, 57000, 98000]
max_salary_filter = 100000

for i in yearly_salary_list:
    if i < max_salary_filter:
        print(i)

sum_low_salaries = 0

for i in yearly_salary_list:
    if i < max_salary_filter:
        sum_low_salaries += i

print(sum_low_salaries)
