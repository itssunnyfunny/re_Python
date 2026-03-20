import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"taking order for #{i}")
        time.sleep(1)


def brew_chai():
    for i in range(1, 4):
        print(f"brewing chai for #{i}")
        time.sleep(1)
#create threads
t1 = threading.Thread(target=take_orders)
t2 = threading.Thread(target=brew_chai)

t1.start()
t2.start()

#wait for threads to finish
t1.join()
t2.join()

print("all orders taken and chai is brewed")