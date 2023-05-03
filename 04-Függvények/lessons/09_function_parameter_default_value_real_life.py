# NameError
# greetings()


def calculate_gross_price(price, vat_percent=27):
    return price * (1 + vat_percent / 100)


print(calculate_gross_price(1000))
