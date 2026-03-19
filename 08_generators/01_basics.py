def serve_chai():
    yield "Cup 1: masala chai"
    yield "Cup 2: ginger chai"
    yield "Cup 3: black chai"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return ["cup 1", "cup 2", "cup 3"]


# generator function 
def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))