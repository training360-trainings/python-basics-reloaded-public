def calcluate_high_salaries_sum(salaries, max_value=100000):
    return sum([salarie for salarie in salaries if salarie > max_value])


print(calcluate_high_salaries_sum([120000, 72000, 57000, 98000]))

print(calcluate_high_salaries_sum([100000, 172000, 157000, 91000], 120000))
