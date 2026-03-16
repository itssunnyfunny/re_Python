order_amount = input("Enter the order amount: ")
order_amount = float(order_amount)
delivery_fee = 0 if order_amount > 100 else 10

print(f"Delivery fee: {delivery_fee}")