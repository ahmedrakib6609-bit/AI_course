
graph = {}
nodes = input("Enter nodes (space separated): ").split()
for node in nodes:
    neighbors = input(f"Neighbors of {node}: ").split()
    graph[node] = neighbors

start = input("Start node: ")
goal = input("Goal node: ")
max_depth = int(input("Max depth: "))

def dls(current, target, depth, path):
    new_path = path + [current]

    if current == target:
        return new_path

    if depth >= max_depth:
        return None
    for neighbor in graph.get(current, []):
        if neighbor in new_path:
            continue
        result = dls(neighbor, target, depth + 1, new_path)
        if result:
            return result
            
    return None

path = dls(start, goal, 0, [])
if path:
    print("Path found:", " -> ".join(path))
else:
    print(f"No path found within {max_depth} steps")