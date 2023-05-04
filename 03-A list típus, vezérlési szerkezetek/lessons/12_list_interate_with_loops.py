yearly_salary_list = [120000, 72000, 57000, 98000]

for i in yearly_salary_list:
    print(i)

for i in range(len(yearly_salary_list)):
    print(f'index: {i}, value: {yearly_salary_list[i]}')

for i, v in enumerate(yearly_salary_list):
    print(f'index: {i}, value: {v}')
