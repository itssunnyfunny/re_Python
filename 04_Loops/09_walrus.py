# value = 13
# remainder = value % 3 

# if remainder:
#     print(f"{value} is not divisible by 3")
# else:
#     print(f"{value} is divisible by 3")

value = 13

if(remainder := value % 3):
    print(f"{value} is not divisible by 3")
else:
    print(f"{value} is divisible by 3")

available_sizes = ["small", "medium", "large"]
size = "small"

if (request_size := input("Enter you cahi cup size: ")) in available_sizes:
    print(f"Your cup size is {request_size}")
else:
    print(f"Sorry, we don't have {request_size}")

flavours = ["masala", "ginger", "lemon", "spiced", "mint"]

print("Available flavours: ", flavours)
while(flavour := input("Enter your favourite flavour: ")):
    if flavour in flavours:
        print(f"Thanks for your order {flavour}")
    else:
        print(f"Sorry, we don't have {flavour}")
        break