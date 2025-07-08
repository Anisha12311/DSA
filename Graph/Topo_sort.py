edges = [[2, 3], [3, 1], [4, 0], [4, 1], [5, 0], [5, 2]]


def topological_sort(edges):
    
    graph = {}
    all_nodes = set()
    
    for u, v in edges:
        
        if u not in graph:
            graph[u] = []
            
        graph[u].append(v)
        all_nodes.add(u)
        all_nodes.add(v)
    for node in all_nodes:
        if node not in graph:
            graph[node] = []    
            
    print(graph, all_nodes)
    visited = set()
    stack = [] 
    
    def dfs(node):
        
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                
        stack.append(node)
            
        
    for node in all_nodes:
          
        if node not in visited:
            dfs(node)
    
    return stack[::-1]

print(topological_sort(edges))
    