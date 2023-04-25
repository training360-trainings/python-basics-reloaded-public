yearly_salary_list = [120000, 72000, 57000, 98000]
max_salary_filter = 100000
sum_high_salaries = 0

for i in yearly_salary_list:
    if i > max_salary_filter:
        sum_high_salaries += i
print(sum_high_salaries)

sum_high_salaries = 0
for i in yearly_salary_list:
    if i > max_salary_filter:
        sum_high_salaries += i
print(sum_high_salaries)
