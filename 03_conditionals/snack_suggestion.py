snack =input("ENter your preferred snack: ").lower()

print(f"user said: {snack}")

if snack == "cokies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print(f"Sorry, we don't have {snack}")