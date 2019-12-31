import threading
from queue import Queue
import time

# If variables are shared between two threads lock them

printLock = threading.Lock() # Var to lock print function.

def exampleJob(worker):
    time.sleep(0.5)

    with printLock:
        print(threading.current_thread().name, worker)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done()

q = Queue()

for x in range(10):

    t = threading.Thread(target = threader) # Defining a thread and var threader.
    t.daemon = True # By classifying it as a daemon, the thread dies, when the main thread dies.
    t.start()

start = time.time() # start var, i.e. time.time(), is to calculate how much time a particular part of program is right now.

for worker in range(20): # Var workers.

    q.put(worker) # Putting variable worker in queue.

q.join() # join() waits for the thread to terminate.

print('Time taken ', time.time() - start)