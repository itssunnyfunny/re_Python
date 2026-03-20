class OutOfIngredientsError(Exception):
    def __init__(self, message):
        self.message = message

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Out of ingredients")
    print("Making chai with milk and sugar")

make_chai(1, 1)
make_chai(0, 1)
make_chai(1, 0)
make_chai(0, 0)