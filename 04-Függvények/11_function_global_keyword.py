# bad practice

price = 1000
vat_percent = 5
gross_price = 0


def calculate_gross_price():
    # global gross_price
    gross_price = price * (1 + vat_percent / 100)


calculate_gross_price()
print(gross_price)
