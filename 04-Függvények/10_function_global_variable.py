# bad practice

def calculate_gross_price():
    return price * (1 + vat_percent / 100)


price = 1000
vat_percent = 5
gross_price = calculate_gross_price()
print(gross_price)
