class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.next_node = None
        
    def setNext(self, next_node):
        self.next_node = next_node
        
    def getNext(self):
        return self.next_node
    
    def setData(self, new_data):
        self.data = new_data
    
    def getData(self):
        return self.data
    

class OrderedList(object):
    
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
        
    def add(self, item):
        prev = None
        cur = self.head
        found_index = False
        while cur is not None and not found_index:
            if cur.data > item:
                found_index = True
            else:
                prev = cur
                cur = cur.next_node
                
        node = Node(item)
        if prev == None:
            node.next_node = self.head
            self.head = node
        else:
            node.next_node = cur
            prev.next_node = node
        self.length += 1
    
    def remove(self, item):
        node = self.head
        prev = None
        found = False
        while not found:
            if node.data == item:
                found = True
            else:
                prev = node
                node = node.next_node
                
        if prev == None:
            self.head = self.head.next_node
        else:
            prev.next_node = node.next_node
        self.length -= 1
            
    def search(self, item):
        node = self.head
        found = False
        stop = False
        while node is not None and not found and not stop:
            if node.data == item:
                found = True
            else:
                if node.data > item:
                    stop = True
                else:
                    node = node.next_node
        return found
    
    def traverse(self):
        node = self.head
        items = ""
        while node is not None:
            items += str(node.data)
            items += " "
            node = node.next_node
        print items if items else "This is an empty list"
            
    
mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(len(mylist))
print(mylist.search(93))
print(mylist.search(100))
mylist.traverse()
print mylist()
