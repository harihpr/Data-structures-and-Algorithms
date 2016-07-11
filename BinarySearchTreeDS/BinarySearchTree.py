
from Node import Node

class BinarySearchTree(object):
    
    def __init__(self):
        self.root_node = None
        
    def insert(self, data):
        if self.root_node is None:
            self.root_node = Node(data)
        else:
            self.root_node.insert(data)
            
    def remove(self, data):
        if self.root_node:
            if self.root_node.data == data:
                temp_node = Node(None)
                temp_node.left_child = self.root_node
                self.root_node.remove(data, temp_node)
                self.root_node = temp_node.left_child
            else:
                self.root_node.remove(data, None)
    
    def getMax(self):
        if self.root_node:
            return self.root_node.getMax()
    
    def getMin(self):
        if self.root_node:
            return self.root_node.getMin()
            
    def inOrderTraversal(self):
        if self.root_node:
            return self.root_node.inOrderTraversal()
    
    def inOrderTraversalWithStack(self):
        stack = []
        if self.root_node:
            current = self.root_node
            done = False
            while not done:
                if current is not None:
                    stack.append(current)
                    current = current.left_child
                else:
                    if len(stack) != 0:
                        temp = stack.pop()
                        print temp.data
                        current = temp.right_child
                    else:
                        done = True
                    