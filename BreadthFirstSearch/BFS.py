
def BFS(start_node):
    
    queue = []
    start_node.visited = True
    queue.append(start_node)
    
    while queue:
        #actual_node = queue.pop()
        actual_node = queue[0]
        queue = queue[1:]
        print "Visiting node - %s" % actual_node.name
        
        for n in actual_node.adjacency_list:
            if not n.visited:
                n.visisted = True
                queue.append(n)