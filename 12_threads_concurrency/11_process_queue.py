from multiprocessing import Process, Queue
import time

def prepare_chai(queue):
    queue.put("chai is prepared")


if __name__ == '__main__':
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))
    p.start()

    print(queue.get())
    p.join()