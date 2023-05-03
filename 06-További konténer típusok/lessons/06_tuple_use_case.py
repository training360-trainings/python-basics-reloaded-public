# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. immutable

location = (37.7749, -122.4194)
color = (255, 0, 0)


def calculate_gross_prices(prices):
    gross_prices = ()
    for i in prices:
        gross_prices += (i * 1.27,)
    return gross_prices


print(calculate_gross_prices([990, 3990, 999990]))
