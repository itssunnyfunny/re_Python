cup = input("Chose your cup size (small, medium, large): ").lower()

if cup == "small":
    print("Your total is $2.00")
elif cup == "medium":
    print("Your total is $2.50")
elif cup == "large":
    print("Your total is $3.00")
else:
    print("Invalid cup size")
