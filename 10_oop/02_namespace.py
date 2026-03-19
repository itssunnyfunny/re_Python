class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True

print(Chai.is_hot)

# creating objects from class Chai

masala = Chai()
print(f"Chai origin: {masala.origin}") # print(masala.origin)
print(f" Chai is hot: {masala.is_hot}") # print(masala.is_hot)

masala.is_hot = False
print(masala.is_hot)

masala.flavor = "spiced"
print(f"Chai flavor: {masala.flavor}")