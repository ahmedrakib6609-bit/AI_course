def dls(node, goal, depth_limit, graph, level=0):
    print(f"Visited {node} | Depth: {level}")

    if node == goal:
        print(f"Goal found: {goal} at level {level}")
        return True

    if level >= depth_limit:
        return False

    for child in graph.get(node, []):
        if dls(child, goal, depth_limit, graph, level + 1):
            return True
    return False


def ids(start, goal, max_depth, graph):
    for depth in range(max_depth + 1):
        print(f"\n--- Trying depth limit: {depth} ---")
        if dls(start, goal, depth, graph):
            print(f" Goal '{goal}' found at depth limit {depth}")
            return True
    print(f" Goal node '{goal}' not found within max depth {max_depth}.")
    return False



graph = {}
n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input(f"Enter the name of node {i + 1}: ")
    neighbours = input(f"Enter the neighbors of {node} (space-separated): ").split()
    graph[node] = neighbours


start_node = input("Enter the start node name: ")
goal_node = input("Enter the goal node name: ")
max_depth = int(input("Enter the maximum depth to search: "))


ids(start_node, goal_node, max_depth, graph)