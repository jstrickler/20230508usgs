
from threading import Thread, Lock
import random
import time

STDOUT_LOCK = Lock()
LIST_LOCK = Lock()

data = []

def my_task(num):  # function to launch in each thread
    time.sleep(random.randint(1, 3))
    with STDOUT_LOCK:
        print("Hello from thread {}".format(num))
    with LIST_LOCK:
        data.append(num)

thread_list = []
for i in range(16):
    t = Thread(target=my_task, args=(i,))  # create thread
    t.start()  # launch thread
    thread_list.append(t)

print("All threads launched.")  # "Done" is printed immediately -- the threads are "in the background"

for thread in thread_list:
    thread.join()  # wait for thread to end

print("All threads done")
print(f"data: {data}")
