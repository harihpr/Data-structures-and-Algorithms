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
    

class UnorderedList(object):
    
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
        
    def add(self, item):
        node = Node(item)
        node.next_node = self.head
        self.head = node
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
        while not found and node is not None:
            if node.data == item:
                found = True
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
    
mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(len(mylist))
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(len(mylist))

mylist.remove(54)
print(len(mylist))
mylist.remove(93)
print(len(mylist))
mylist.remove(31)
print(len(mylist))
print(mylist.search(93))
mylist.traverse()
