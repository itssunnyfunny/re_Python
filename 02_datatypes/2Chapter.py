# mutables

spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}")
spice_mix.add("something")
spice_mix.add("anotherthing")
print(f"After adding spices mix id : {id(spice_mix)}")