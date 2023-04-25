# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. immutable

location = (37.7749, -122.4194)
color = (255, 0, 0)


def calculate_salary_aggregates(salaries):
    summa = 0
    for i in salaries:
        summa += i
    return (summa, summa / len(salaries))
