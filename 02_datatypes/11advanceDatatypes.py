# import arrow 

# current_time = arrow.now()
# EuroTime = current_time.to('Europe/Paris').format('Europe/Paris')
# print(f"Current time: {current_time}")


from collections import namedtuple
Customer = namedtuple('Customer',["name", "address"])
customer = Customer('John Smith', '123 Main Street')
print(f"Customer name: {customer.name}")