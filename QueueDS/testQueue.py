
from Queue import Queue

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print queue.dequeue()
print queue.dequeue()
print queue.size()
print queue.dequeue()
print queue.size()
print queue.dequeue()