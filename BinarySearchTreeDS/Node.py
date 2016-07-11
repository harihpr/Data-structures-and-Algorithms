
class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    def insert(self, data):
        if data < self.data:
            if not self.left_child:
                self.left_child = Node(data)
            else:
                self.left_child.insert(data)
        else:
            if not self.right_child:
                self.right_child = Node(data)
            else:
                self.right_child.insert(data)
                
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
            
    def remove(self, data, parent_node):
        if data < self.data:
            if self.left_child is not None:
                self.left_child.remove(data, self)
        elif data > self.data:
            if self.right_child is not None:
                self.right_child.remove(data, self)
        else:
            if self.left_child is not None and self.right_child is not None:
                self.data = self.right_child.getMin()
                self.right_child.remove(self.data, self)
            elif self.parent_node.left_child == self:
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child
                self.parent_node.left_child = temp_node
            elif self.parent_node.right_child == self:
                if self.left_child is not None:
                    temp_node = self.left_child
                else:
                    temp_node = self.right_child
                self.parent_node.right_child = temp_node