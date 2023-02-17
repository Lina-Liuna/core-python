import threading
import queue

# The queue module implements multi-producer, multi-consumer queues.
# It is especially useful in threaded programming when information must be exchanged safety between multiple threads.

# Constructor for a FIFO queue.
q = queue.Queue()

def worker():
    while True:

        # q.get: remove and return an item from the queue.
        item = q.get()
        print(f'Working on {item}')
        print(f'Finished {item}')

        # indicate that a formerly enqueued task is complete.
        q.task_done()

# Turn-on the worker thread.
threading.Thread(target=worker, daemon=True).start()

# Send thirty task requests to the worker.
for item in range(5):
    # put item in the queue.
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')