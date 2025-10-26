import heapq

# Input graph with costs
graph = {}

nodes = input("Enter all nodes (space separated): ").split()
for node in nodes:
    neighbors_input = input(f"Enter neighbors of {node} with cost (e.g., B 2 C 3): ").split()
    graph[node] = []
    for i in range(0, len(neighbors_input), 2):
        neighbor = neighbors_input[i]
        cost = int(neighbors_input[i + 1])
        graph[node].append((neighbor, cost))

# Input heuristic values
heuristic = {}
print("\nEnter heuristic values for each node:")
for node in nodes:
    h_val = int(input(f"h({node}): "))
    heuristic[node] = h_val

# Start and goal node
start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

# A* Search Algorithm
def a_star_search(graph, start, goal, heuristic):
    # (f, g, node, path)
    open_list = [(heuristic[start], 0, start, [start])]
    closed_set = set()

    while open_list:
        # Pop the node with the lowest f(n)
        f, g, node, path = heapq.heappop(open_list)
        print(f"Visiting: {node}, f={f}, g={g}, h={heuristic[node]}")

        # Goal check
        if node == goal:
            print(f"\n✅ Goal '{goal}' found!")
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return True

        closed_set.add(node)

        # Explore neighbors
        for neighbor, cost in graph[node]:
            if neighbor not in closed_set:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    print("\n❌ Goal not found.")
    return False


# Run the search
a_star_search(graph, start, goal, heuristic)
