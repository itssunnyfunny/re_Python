# set

essential_spices = {"cardamom", "cinnamon", "cloves"}
print(f"essential spices: {essential_spices}")

optional_spices = {"ginger", "nutmeg", "cinnamon"}
print(f"optional spices: {optional_spices}")

all_spices = essential_spices | optional_spices
print(f"all spices: {all_spices}")

comman_spices = essential_spices & optional_spices
print(f"common spices: {comman_spices}")

only_in_essential = essential_spices - optional_spices
print(f"only in essential: {only_in_essential}")

only_in_optional = optional_spices - essential_spices
print(f"only in optional: {only_in_optional}")

print(f"Is cardamom in all spices? {'cardamom' in all_spices}")