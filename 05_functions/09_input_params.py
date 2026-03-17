# chai = "ginger chai"

# def prepare_cahi(order):
#     print(f"Chai order: ", order)

# prepare_cahi(chai)
# print(chai)

chai = [1,2,3]

def edit_chai(cup):
    cup[1] = 42
    return cup

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "yes", "low") #positional arguments
make_chai(tea="Green", sugar="medium", milk="no") #keyword arguments

def special_chai(*ingredients, **extras):
    print("Ingredients: ", ingredients)
    print("Extras: ", extras)


special_chai("cinnamon", "cardmom", sweetness="low", foam="yes")

# def chai_order(order=[]):
#     order.append("ginger")
#     print(order)

# chai_order()
# chai_order()
# print(chai_order())

def chai_order(order=None):
    if order is None:
        order = []
    order.append("ginger")
    return order

chai_order()
chai_order()
print(chai_order())