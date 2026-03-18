favourite_chai = [
    "Masala Chai", "Green Tea", "Masala Chai"
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]


unique_chai = {item for item in favourite_chai}
print(unique_chai)

recipes = {
    "Masala Chai": ["Masala", "Water", "Sugar"],
    "Green Tea": ["Green Tea", "Water"],
    "Elaichi Chai": ["Elaichi", "Water", "Sugar"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)