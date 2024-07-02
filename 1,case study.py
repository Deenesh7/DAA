graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 2},
    'F': {'D': 6, 'E': 2}
}
start_node = 'A'
distances = {}
predecessors = {}
for node in graph:
    distances[node] = float('inf')
    predecessors[node] = None
distances[start_node] = 0
priority_queue = [(0, start_node)]
visited = set()
while priority_queue:
    priority_queue.sort()
    current_distance, current_node = priority_queue.pop(0)
    if current_node in visited:
        continue
    visited.add(current_node)
    for neighbor, weight in graph[current_node].items():
        distance = current_distance + weight
        
        if distance < distances[neighbor]:
            distances[neighbor] = distance
            predecessors[neighbor] = current_node
            priority_queue.append((distance, neighbor))
print("Shortest distances from the start node:")
for node in distances:
    print(f"Distance to {node}: {distances[node]}")

print("\nShortest paths from the start node:")
for node in graph:
    if node == start_node:
        continue
    path = []
    current = node
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    print(f"Path to {node}: {' -> '.join(path)}")