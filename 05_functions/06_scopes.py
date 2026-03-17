def serve_chai():
    chai_type = "Ginger chai" #local variable
    print(f"Chai type: {chai_type}")
    return chai_type

chai_type = "Lemon"

# print(f"Chai type: {chai_type}")
# serve_chai()
# print(f"Chai type: {chai_type}")

def chai_counter():
    chai_order = "lemon" #Enclosing scope
    def print_order():
        chai_order = "ginger" #local variable
        print(f"Chai order: {chai_order}")
    print_order()
    print(f"Chai order: {chai_order}")

cahi_order = "tulsi"# Global scope
chai_counter()
print(f"Chai order: {cahi_order}")