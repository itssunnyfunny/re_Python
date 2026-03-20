from multiprocessing import Process
import time

def brew_chai(name):
   print(f"brewing chai for {name}")
   time.sleep(1)
   print(f"chai brewed for {name}")


if __name__ == "__main__":
   chai_makers = [
      Process(target=brew_chai, args=(f"chai maker {i}",))
        for i in range(1, 4)
   ]

  
# start all processes
   for chai_maker in chai_makers:
      chai_maker.start()

   # wait for all processes to finish
   for chai_maker in chai_makers:
      chai_maker.join()

   print("all chai is brewed")
