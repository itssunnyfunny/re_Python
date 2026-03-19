def chai_customer():
        print("Welcome to chai shop ! what chai would you like? ")
        order = yield
        while True:
                print(f"Chai order: {order}")
                order = yield 

customer = chai_customer()
next(customer)
customer.send("ginger chai")
customer.send("black chai")