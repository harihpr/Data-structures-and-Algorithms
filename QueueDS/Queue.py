
class Queue(object):
    
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return self.queue == []
    
    def enqueue(self, data):
        self.queue.append(data)
        
    def dequeue(self):
        if len(self.queue) > 0:
            elem = self.queue[0]
            self.queue = self.queue[1:]
            return elem
    
    def size(self):
        return len(self.queue)