# Boolean

is_boiling = True
stri_count = 5 
total_actions = stri_count + is_boiling #upcasting 
print(f"Total actions: {total_actions}")

milk_present = 0 #no milk
print(f"Is ther milk? {bool(milk_present)}")


water_hot = True
tea_added = False

can_serve_tea = water_hot or tea_added
print(f"can serve tea? {can_serve_tea}")