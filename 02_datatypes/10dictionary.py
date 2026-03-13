# dictionary

chai_order = dict(type="black", sugar=5, milk=1)
print(f"Chai order: {chai_order}")
print(f"Chai type: {chai_order['type']}")

chai_recipe = {}

chai_recipe["type"] = "black"
chai_recipe["base"] = "milk"
chai_recipe["sugar"] = 1

print(f"Chai recipe: {chai_recipe}")
del chai_recipe["base"]
# print(f"Chai recipe: {chai_recipe}")
# print(f"Chai type: {chai_recipe.keys()}")
# print(f"Chai values: {chai_recipe.values()}")
# print(f"Chai items: {chai_recipe.items()}")


print(f"Is milk in chai recipe? {'milk' in chai_recipe}")

extra_spices = {"cardamom": 2, "cinnamon": 1}
chai_recipe.update(extra_spices)
print(f"Chai recipe: {chai_recipe}")

customer_note =  extra_spices.get("ginger")
print(f"Chai recipe: {customer_note}")