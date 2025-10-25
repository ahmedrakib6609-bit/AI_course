graph = {}

nodes = input("Enter all nodes (space separated): ").split()
for node in nodes:
    neighbors_input = input(f"Enter neighbors of {node} with cost (e.g., B 2 C 3): ").split()
    graph[node] = []
    for i in range(0, len(neighbors_input), 2):
        neighbor = neighbors_input[i]
        cost = int(neighbors_input[i + 1])
        graph[node].append((neighbor, cost))

heuristic = {}
print("\nEnter heuristic values for each node:")
for node in nodes:
    h_val = int(input(f"h({node}): "))
    heuristic[node] = h_val

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")
c = []
import heapq

# A* Search Algorithm
def a_star_search(graph, start, goal, heuristic,c):
    open_list = [(heuristic[start], 0, start, [start],f+g[start])]  # (f, g, node, path)
    closed_set = set()
    

    while open_list:
        f, g, node, path, c = heapq.heappop(open_list)
        print(f"Visiting: {node}, f={f}, g={g}, h={heuristic[node]}")

        if node == goal:
            print(f"Goal '{goal}' found ")
            print("Path:", " -> ".join(path))
            print("Total cost:", g)
            print("node cost: ", c)
            return True

        closed_set.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in closed_set:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor], f+g[neighbor]))

    print("Goal not found ")
    return False

a_star_search(graph, start, goal, heuristic,c)
