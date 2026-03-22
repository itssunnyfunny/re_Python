import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def task1():
    with lock_a:
        print("Task 1 holds lock A ")
        with lock_b:
            print("Task 1 holds lock A and B ")


def task2():
    with lock_b:
        print("Task 2 holds lock B ")
        with lock_a:
            print("Task 2 holds lock B and A ")


thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()