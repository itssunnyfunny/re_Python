def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)
print(chai_flavor.__module__)

def generate_bill(chai=0, samosa=0):
    """
    Generate bill for chai and samosa
    :param chai: NUmber of chai cups (10 rupees each)
    :return: (total amount , thank you message)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for ordering chai and samosa"

generate_bill(2,1)

print(generate_bill.__doc__)
print(generate_bill.__name__)
print(generate_bill.__module__)