# NameError
# greetings()


def calculate_sum_prices(basket):
    sum_price = 0
    for i in basket:
        sum_price += i
    return sum_price


print(calculate_sum_prices([1000, 2000, 3000]))
