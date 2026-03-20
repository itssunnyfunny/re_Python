# file = open("order.txt", "w")

# try:
#     file.write("masala chai")
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("masala chai - 10 cups")
