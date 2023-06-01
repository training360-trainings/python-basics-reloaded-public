def calcluate_high_salaries_sum(salaries, max_value):
    sum_high_salaries = 0
    for i in salaries:
        if i > max_value:
            sum_high_salaries += i
    return sum_high_salaries


print(calcluate_high_salaries_sum([120000, 72000, 57000, 98000], 100000))

print(calcluate_high_salaries_sum([100000, 172000, 157000, 91000], 120000))
