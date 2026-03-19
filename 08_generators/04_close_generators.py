def local_chai():
    yield "masala chai"
    yield "ginger chai"
    yield "black chai"
    yield "kulfi chai"


def imported_chai():
    yield "ginger chai"
    yield "black chai"
    yield "kulfi chai"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try: 
        while True:
            order = yield "waiting for chai order"
    except:
        print("stall closed, No more chai")

stall = chai_stall()
print(next(stall))
stall.close()