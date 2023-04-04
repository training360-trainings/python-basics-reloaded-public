net_prices = [1000, 220, 7450, 6600]

gross_prices = []
for i in net_prices:
    gross_prices.append(i * 1.27)

print(gross_prices)

# [expression for member in iterable]
gross_prices = [i * 1.27 for i in net_prices]

print(gross_prices)
