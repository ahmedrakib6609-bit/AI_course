from collections import deque

# User input for graph
graph = {}
nodes = input("Enter all nodes (space separated): ").split()
for node in nodes:
    neighbors = input(f"Neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Start node: ")
goal = input("Goal node: ")

# Special case: start and goal are same
if start == goal:
    print(f"Path: {start}")
    exit()

# Track parents and visited nodes
start_parent = {start: None}
goal_parent = {goal: None}
start_queue = deque([start])
goal_queue = deque([goal])

# Track meeting point
meeting_node = None

while start_queue and goal_queue:
    # Expand from start side
    current = start_queue.popleft()
    for neighbor in graph.get(current, []):
        if neighbor not in start_parent:
            start_parent[neighbor] = current
            start_queue.append(neighbor)
            if neighbor in goal_parent:
                meeting_node = neighbor
                break
    if meeting_node:
        break

    # Expand from goal side
    current = goal_queue.popleft()
    for neighbor in graph.get(current, []):
        if neighbor not in goal_parent:
            goal_parent[neighbor] = current
            goal_queue.append(neighbor)
            if neighbor in start_parent:
                meeting_node = neighbor
                break
    if meeting_node:
        break

# Reconstruct path if meeting point found
if meeting_node:
    # Build path from start to meeting point
    path = []
    node = meeting_node
    while node:
        path.append(node)
        node = start_parent.get(node)
    path.reverse()
    
    # Build path from meeting point to goal
    node = goal_parent.get(meeting_node)
    while node:
        path.append(node)
        node = goal_parent.get(node)
    
    print("Path:", " -> ".join(path))
else:
    print(f"No path between {start} and {goal}")
