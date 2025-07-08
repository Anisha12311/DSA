graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    stack = [start]
    order = []
    while stack:
        node = stack.pop()

        if node not in visited:
            print(node)
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return order
         
   
   
def BFS(graph, start):
    visited = set()
    queue = [start]
    
    order = []
    
    while queue:
        node = queue.pop(0)
        
        if node not in visited:
            visited.add(node)
            order.append(node)
            
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                
    return order
                
            
print(BFS(graph, 'A'))