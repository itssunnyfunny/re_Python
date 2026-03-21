from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers....")
    total = 0 
    for i in range(10**7):
        total += i
    print(f"✅Total is {total}")

if __name__ == "__main__":
        
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(10)]
    [thread.start() for thread in processes]
    [thread.join() for thread in processes]
    end = time.time()
    print(f"Time taken: {end - start:.2f}")