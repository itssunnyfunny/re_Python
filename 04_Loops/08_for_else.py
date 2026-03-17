staff = [("Amit", 30), ("Sachin", 40), ("Rahul", 50), ("Rohit", 60)]

for name, age in staff:
    if age < 50:
       print(f"Name: {name}, Age: {age}")
       break
else:
    print("No more employees")