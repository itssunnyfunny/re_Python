name = ["shani","Meera", "carolos", "priya"]
bills = [40, 50, 60, 70]

for name, amount in zip(name, bills):
    print(f"{name} owes ${amount}")