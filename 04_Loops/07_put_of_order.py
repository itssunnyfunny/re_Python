flavours = ["Ginger", "out of stock", "Lemon", "Discoutinued", "Tulsi"]

for flavour in flavours:
    if flavour =="out of stock":
        continue
    if flavour == "Discoutinued":
        print("Sorry, this flavour is discoutinued")
        break
    print(flavour)
print("Thanks for your order")