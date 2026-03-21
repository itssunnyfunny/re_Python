import threading 
import time

def berw_chai():
    print(f"{threading.current_thread().name} is brewing chai")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} has brewed chai")
    return count

tread1 = threading.Thread(target=berw_chai, name="chai maker 1")
tread2 = threading.Thread(target=berw_chai, name = "chai maker 2")

start = time.time()
tread1.start()
tread2.start()

tread1.join()
tread2.join()

end = time.time()
print(f"Time taken: {end - start:.2f}")

print("all chai is brewed")