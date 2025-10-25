graph = {}

nodes = input("Enter all nodes (space separated): ").split()
for node in nodes:
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

heuristic = {}
print("\nEnter heuristic values for each node:")
for node in nodes:
    heuristic[node] = int(input(f"h({node}): "))

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")
beam_width = int(input("Enter Beam Width (K): "))

def beam_search(graph, start, goal, heuristic, beam_width):
    queue = [(heuristic[start], start, [start])]  # (h(n), node, path)

    while queue:
        
        new_queue = []
        for h, node, path in queue:
            print(f"Visiting: {node}")

            if node == goal:
                print("\nGoal found ")
                print("Path:", " -> ".join(path))
                return True

            for neighbor in graph[node]:
                new_queue.append((heuristic[neighbor], neighbor, path + [neighbor]))

        
        new_queue.sort(key=lambda x: x[0])

        
        queue = new_queue[:beam_width]

    print("Goal not found ")
    return False

beam_search(graph, start, goal, heuristic, beam_width)
