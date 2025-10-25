graph = {}

nodes = input("Enter all nodes (space separated): ").split()
for node in nodes:
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

heuristic = {}
print("\nEnter heuristic values for each node:")
for node in nodes:
    h_val = int(input(f"h({node}): "))
    heuristic[node] = h_val

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

import heapq

def best_first_search(graph, start, goal, heuristic):
    visited_order = []
    visited = set()
    priority_queue = [(heuristic[start], start)]
    parent = {start: None}

    while priority_queue:
        h, node = heapq.heappop(priority_queue)
        print(f"Visiting: {node}")
        visited_order.append(node)

        if node == goal:
            print(f"\nGoal '{goal}' found ")


            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()

            print("Path:", " -> ".join(path))
            print("\nvisited_order: ","->".join(visited_order))
            return True

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in parent:
                parent[neighbor] = node
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

    print("Goal not found ")
    return False

best_first_search(graph, start, goal, heuristic)