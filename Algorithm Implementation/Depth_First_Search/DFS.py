#DFS
# Take user input for graph
graph = {}
n = int(input("Enter number of nodes: "))
for i in range(n):
    node = input("Enter node name: ")
    neighbours = input(f"Enter neighbours of {node} separated by space: ").split()
    graph[node] = neighbours

visited = []  # List for visited nodes
stack = []    # Stack for DFS

def dfs(visited, graph, node):  
    stack.append(node)

    while stack:
        m = stack.pop()  
        if m not in visited:
            print(m, end=" ")
            visited.append(m)

            for neighbour in graph[m]:  
                if neighbour not in visited:
                    stack.append(neighbour)

print("Following is the Depth-First Search:")
start = input("Enter starting node: ")

dfs(visited, graph, start)