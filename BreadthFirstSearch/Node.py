
class Node(object):
    
    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False