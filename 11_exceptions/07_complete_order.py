class InvalidChaiError(Exception):
    def __init__(self, message):
        self.message = message

def bill(flavor, cups):
    menu = {"masala": 30, "ginger": 40, "lemon": 50}
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"Invalid chai flavor: {flavor}")
        if not isinstance(cups, int):
            raise TypeError(f"Number of cups must be an integer, not {type(cups)}")
        total =  menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai : {total}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Thanks for your order")

bill("ginger", 2)
bill("unknown", 2)
bill("ginger", "unknown")
bill("ginger", 9)