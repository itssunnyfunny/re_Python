class Chai:
    temperature= "hot"
    strength = "strong"

cutting = Chai()
print(cutting.temperature)
print(cutting.strength)

cutting.temperature = "Mild"
cutting.cup = "small"

print(f"Cutting chai temperature: {cutting.temperature}")
print(f"Cutting chai cup: {cutting.cup }")
print(f"Direct look into the class: {Chai.temperature}")

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(f"cup size is :{cutting.cup} ")