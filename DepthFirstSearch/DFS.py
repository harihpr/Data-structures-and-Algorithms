
def DFS(node):
    
    node.visited = True
    print "Visiting node - %s" % node.name
    
    for n in node.adjacency_list:
        if not n.visited:
            DFS(n)