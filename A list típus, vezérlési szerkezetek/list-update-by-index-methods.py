yearly_salary_list = [120000, 72000, 57000, 98000]


# adott indexen lévő érték módosítása
yearly_salary_list[0] = 121000
print(yearly_salary_list)

# elem hozzáfűzése a végéhez
yearly_salary_list.append(48000)
print(yearly_salary_list)

# lista kiegészítése elemekkel
yearly_salary_list.extend([66000, 53000])
print(yearly_salary_list)

# elem hozzáadása a adott indexű helyre
yearly_salary_list.insert(1, 111111)
print(yearly_salary_list)

# érték törlése, egy elemet töröl, ha nincs akkor hibát dob
yearly_salary_list.remove(53000)
print(yearly_salary_list)
