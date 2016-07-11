
from Node import Node
import BFS

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacency_list.append(node2)
node1.adjacency_list.append(node5)
node2.adjacency_list.append(node4)
node4.adjacency_list.append(node3)

BFS.BFS(node1)