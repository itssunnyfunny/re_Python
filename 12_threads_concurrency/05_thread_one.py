import threading 
import time

def boil_milk():
    print("boiling milk....")
    time.sleep(3)
    print("milk boiled....")

def toast_bun():
    print("toasting bun....")
    time.sleep(1)
    print("bun toasted....")

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Time taken: {end - start:.2f}")