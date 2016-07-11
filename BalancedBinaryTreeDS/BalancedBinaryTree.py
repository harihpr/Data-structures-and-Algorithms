
from Node import Node

class BalancedBinaryTree(object):
    
    def __init__(self):
        self.root_node = None
    
    def insert(self, data):
        parent_node = self.root_node
        if self.root_node == None:
            parent_node = Node(data, None)
            self.root_node = parent_node
        else:
            parent_node = self.root_node.insert(data, self.root_node)
        
        self.rebalanceTree(parent_node)
    
    def setBalance(self, node):
        node.balance = self.height(node.right_child) - self.height(node.left_child)
    
    def rebalanceTree(self, parent_node):
        self.setBalance(parent_node)
        
        if parent_node.balance < -1:
            if self.height(parent_node.left_child.left_child) >= self.height(parent_node.left_child.right_child):
                parent_node = self.rotateRight(parent_node)
            else:
                parent_node = self.rotateLeftRight(parent_node)
        elif parent_node.balance > 1:
            if self.height(parent_node.right_child.right_child) >= self.height(parent_node.right_child.left_child):
                parent_node = self.rotateLeft(parent_node)
            else:
                parent_node = self.rotateRightLeft(parent_node)
        
        if parent_node.parent_node is not None:
            self.rebalanceTree(parent_node.parent_node)
        else:
            self.root_node = parent_node
            
    def rotateLeftRight(self, node):
        print ("Rotating Left and then Right...")
        node.left_child = self.rotateLeft(node.left_child)
        return self.rotateRight(node)
    
    def rotateRightLeft(self, node):
        print ("Rotating Right and then Left...")
        node.right_child = self.rotateRight(node.right_child)
        return self.rotateLeft(node)
    
    def rotateLeft(self, node):
        print("Left rotation...\n");

        b = node.right_child;
        b.parent_node = node.parent_node;
        
        node.right_child = b.left_child;
        
        if( node.right_child is not None ):
            node.right_child.parent_node = node;
            
        b.left_child = node;
        node.parent_node = b;
        
        if( b.parent_node is not None ):
            if( b.parent_node.right_child == node ):
                b.parent_node.right_child = b;
            else:
                b.parent_node.left_child = b;
                
        self.setBalance(node);
        self.setBalance(b);
        
        return b;
        
    def rotateRight(self, node):
        print("Right rotation...\n");

        b = node.left_child;
        b.parent_node = node.parent_node;
        
        node.left_child = b.right_child;
        
        if( node.left_child is not None ):
            node.left_child.parent_node = node;
            
        b.right_child = node;
        node.parent_node = b;
        
        if( b.parent_node is not None ):
            if( b.parent_node.right_child == node ):
                b.parent_node.right_child = b;
            else:
                b.parent_node.left_child = b;
                
        self.setBalance(node);
        self.setBalance(b);
        
        return b;
    
    def height(self, node):
        if(node == None):
            return -1;
        
        return 1 + max(self.height(node.left_child) , self.height(node.right_child));