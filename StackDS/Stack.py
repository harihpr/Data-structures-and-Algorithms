
class Stack(object):
    
    def __init__(self):
        self.stack = []
        self.num_of_items = 0
        
    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)
        self.num_of_items += 1
    
    def pop(self):
        if len(self.stack) > 0:
            self.num_of_items -= 1
            return self.stack.pop()

    
    def size(self):
        return len(self.stack)