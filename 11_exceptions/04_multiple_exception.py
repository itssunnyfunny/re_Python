def process_order (item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price*quantity
        print(f"Total cost: {cost}")
    except KeyError:
        print(f"Sorry, we don't have {item}")
    except TypeError:
        print(f"Quantity must be a number")

process_order("ginger", 2)
process_order("masala", "two")