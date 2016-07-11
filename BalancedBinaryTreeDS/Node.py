
class Node(object):
    
    def __init__(self, data, parent_node):
        self.data = data
        self.parent_node = parent_node
        self.right_child = None
        self.left_child = None
        self.balance = 0
    
    def insert(self, data, parent_node):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data, parent_node)
            else:
                self.left_child.insert(data, parent_node)
        else:
            if not self.right_child:
                self.right_child = Node(data, parent_node)
            else:
                self.right_child.insert(data, parent_node)
        return parent_node
    
    def getMin(self):
        if self.left_child is None:
            return self.data
        else:
            self.left_child.getMin()
            
    def getMax(self):
        if self.right_child is None:
            return self.data
        else:
            self.right_child.getMax()
            
    def inOrderTraversal(self):
        if self.left_child is not None:
            self.left_child.inOrderTraversal()
            
        print self.data
        
        if self.right_child is not None:
            self.right_child.inOrderTraversal()
    
    