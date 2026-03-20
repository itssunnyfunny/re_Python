chai_menu = {"masala": 30, "ginger": 40, "lemon": 50}


try:
    chai_menu["elaichi"]
except KeyError:
    print("Sorry, we don't have elaichi chai")

print("Thanks for your order")