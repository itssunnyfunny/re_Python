# def make_chai():
#     return "Darjeeling yes low"

# return_value = make_chai()

# print(return_value)

def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cups():
    return 20

total = sold_cups()

print(total)


def chai_status(cups_left):
    if cups_left == 0:
        return "out of stock"
    return "available"

print(chai_status(0))
print(chai_status(10))

def chai_report():
    return 100, 20 #sold, remaining

sold, remaining = chai_report()

print(sold)
print(remaining)