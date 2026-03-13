# Lists -> mutable(changeable) = array

ingredients = ["ginger", "tea", "milk"]
ingredients.append("sugar")
print(f"ingredients: {ingredients}")
ingredients.remove("ginger")
print(f"ingredients: {ingredients}")

spice_options = ["cardamom", "cinnamon", "cloves"]
chai_ingredients = ["water", "milk"]
chai_ingredients.extend(spice_options)
print(f"Chai ingredients: {chai_ingredients}")
chai_ingredients.insert(2, "ginger")
print(f"Chai ingredients: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Last added: {last_added}")
print(f"Chai ingredients: {chai_ingredients}")

chai_ingredients.reverse()
print(f"Chai ingredients: {chai_ingredients}")

chai_ingredients.sort()
print(f"Chai ingredients: {chai_ingredients}")

print(f"Index of milk: {chai_ingredients.index('milk')}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Average sugar level: {sum(sugar_levels) / len(sugar_levels)}")

print(f"Min sugar level: {min(sugar_levels)}")
print(f"Max sugar level: {max(sugar_levels)}")

#operators overloading
base_liquid = ["water", "milk"]
extra_flavor = ["ginger", "cardamom"]

full_liquid = base_liquid + extra_flavor
print(f"Full liquid: {full_liquid}")

strong__brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong__brew}")

#bytearray

raw_spice_data = bytearray(b"CINNAMON")

print(f"Raw spice data: {raw_spice_data}")