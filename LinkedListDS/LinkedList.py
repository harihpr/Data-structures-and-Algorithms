
from Node import Node

class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.counter = 0
        
    def traverseList(self):
        curr_node = self.head
        while curr_node is not None:
            print curr_node.data
            curr_node = curr_node.next_node
            
    def length(self):
        return self.counter
    
    def insertAtStart(self, data):
        self.counter += 1
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    
    def insertAtEnd(self, data):
        if self.head is None:
            self.insertAtStart(data)
            return
        
        self.counter += 1
        new_node = Node(data)
        curr_node = self.head
        while curr_node.next_node is not None:
            curr_node = curr_node.next_node
        curr_node.next_node = new_node
        
    def remove(self, data):
        prev_node = self.head
        if prev_node:
            if prev_node.data == data:
                self.head = prev_node.next_node
            else:
                curr_node = prev_node.next_node
                while curr_node is not None:
                    if curr_node.data == data:
                        prev_node.next_node = curr_node.next_node
                        temp_node = curr_node.next_node
                        del curr_node
                        curr_node = temp_node
                    else:
                        prev_node = curr_node
                        curr_node = curr_node.next_node
        #if self.head:
            #if data == self.head.data:
                #self.head = self.head.next_node
            #else:
                #self.head.remove(data, self.head)
            #self.counter -= 1