# NameError
# greetings()


def calculate_gross_price(price, vat_percent):
    if vat_percent is None:
        return 'Gross price can not be calculated'
    return price * (1 + vat_percent / 100)


print(calculate_gross_price(1000, 27))
print(calculate_gross_price(1000, None))
