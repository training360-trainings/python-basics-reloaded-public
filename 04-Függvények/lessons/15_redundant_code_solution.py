def calcluate_high_salaries_sum(salaries, max_value):
    sum_high_salaries = 0
    for i in salaries:
        if i > max_value:
            sum_high_salaries += i
    return sum_high_salaries


yearly_salary_list_1 = [120000, 72000, 57000, 98000]
max_salary_criterion_1 = 100000

print(calcluate_high_salaries_sum(
    yearly_salary_list_1,
    max_salary_criterion_1)
)

yearly_salary_list_2 = [100000, 172000, 157000, 91000]
max_salary_max_salary_criterion_2 = 120000

print(calcluate_high_salaries_sum(
    yearly_salary_list_2, max_salary_max_salary_criterion_2))
