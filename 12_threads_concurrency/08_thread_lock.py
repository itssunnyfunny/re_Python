import threading

counter = 0
lock = threading.Lock()

def increament():
    global counter 
    for _ in range(100_000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increament) for _ in range(10)]
[thread.start() for thread in threads]
[thread.join() for thread in threads]
print(counter)