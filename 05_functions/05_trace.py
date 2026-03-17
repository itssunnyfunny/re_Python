def add_vat(price, vat_rat):
    return price * (100 + vat_rat)/100

orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 20)
    print(f"Price: {price}, Final amount: {final_amount}")