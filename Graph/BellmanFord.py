def bellman_ford(edges, num_nodes, start):
    distance = [float('inf')] * num_nodes
    distance[start] = 0
    for _ in range(num_nodes - 1):
        
        for u, v, w in edges:
            if distance != 'inf' and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                
    for u, v, w in edges:
        if distance[u] != 'inf' and distance[u] + w < distance[v]:
            print("negative cycle")
            return None
    return distance                

edges = [
    [0, 1, 4],
    [0, 2, 5],
    [1, 2, -3],
    [2, 3, 4],
    [3, 1, 2]
]

result = bellman_ford(edges, 4, 0)


if result: 
    for i , d in enumerate(result):
        print(f"0 -> {i} : {d}")