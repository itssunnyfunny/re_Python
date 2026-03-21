import threading
import time 

def prepare_chai(type_, wait_time):
    print(f"Preparing {type_} chai....")
    time.sleep(wait_time)
    print(f"{type_} chai is prepared...")


t1 = threading.Thread(target=prepare_chai, args=("black", 4))
t2 = threading.Thread(target=prepare_chai, args=("ginger", 2))

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()
print(f"Time taken: {end - start:.2f}")