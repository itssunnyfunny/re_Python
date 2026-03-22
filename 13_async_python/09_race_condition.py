import threading

chai_stock =0
def restock():
    global chai_stock
    for _ in range(100_000):
        chai_stock += 1


threads = [threading.Thread(target=restock) for _ in range(4)]

[thread.start() for thread in threads]
[thread.join() for thread in threads]
print(chai_stock)