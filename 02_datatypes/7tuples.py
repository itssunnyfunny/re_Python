# tuples 

masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spices3) = masala_spices

print(f"main masala spices: {spice1}, {spice2}, {spices3}")

ginger_ratio ,cadramon_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio} and C: {cadramon_ratio} ")

ginger_ratio , cadramon_ratio = cadramon_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio} and C: {cadramon_ratio} ")

# membership

print(f"is cinnamon in masala spieces? {'cinnamon' in masala_spices}")