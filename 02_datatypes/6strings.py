# strings

chai_type = "Ginger chai"

customer_name = "Priya"
print(f"Hello {customer_name} your chai type is {chai_type}")

chai_description= "Aromatic and Bold"

print(f"first word: {chai_description[0:8:1]}")
print(f"last word: {chai_description[12:]}")
print(f"reversing : {chai_description[::-1]}")

label_text = "Chai SPecial"
encoded_label = label_text.encode("utf-8")
print(f"non encoded label {label_text}")
print(f"encoded label {encoded_label }")




decoded_lable = encoded_label.decode("utf-8")
print(f"decoded label: {decoded_lable} ")