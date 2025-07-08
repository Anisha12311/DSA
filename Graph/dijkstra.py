# graph = {
#     'A': [('B', 1), ('C', 4)],
#     'B': [('A', 1), ('C', 2), ('D', 5)],
#     'C': [('A', 4), ('B', 2), ('D', 1)],
#     'D': [('B', 5), ('C', 1)]
# }

start_node = 0

    # edge list format: {u, v, weight}
edges =[[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]];


def build_graph(edges):
    graph = {}
    
    for u, v, w in edges:
        if u not in graph:
            graph[u] = []
            
        if v not in graph:
            graph[v] = []
            
            
        graph[u].append((v,w))
        graph[v].append((u, w))
        
    return graph

def dijkstra(graph, start):
    
    distance = {node : float('inf') for node in graph}
    print(distance)
    
    visited = set()
    
        
    distance[start] = 0
    
    while len(visited) < len(graph):
        min_node = None
        
        for node in graph: 
            if node not in visited:
                if min_node is None or distance[node] < distance[min_node]:
                    min_node = node
                    
                    
        if min_node is None:
            break
        
        visited.add(min_node)
        
        for neighbor, weight in graph[min_node]:
            
            if neighbor not in visited:
                
                if distance[min_node] + weight < distance[neighbor]:
                    distance[neighbor] = distance[min_node] + weight
                    
    return distance      
    
    
graph = build_graph(edges)
print("graph", graph)
result = dijkstra(graph, start_node)


for node in result:
    print(f"{start_node} -> {node} : {result[node]}")