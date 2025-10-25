# Depth-First Search (DFS) Algorithm Implementation in Python (Iterative)

## Overview

This program implements the **Depth-First Search (DFS)** algorithm, a fundamental **uninformed search algorithm** used for traversing or searching tree or graph data structures.

DFS explores as **far as possible** along each branch before **backtracking**. The iterative approach uses an explicit **stack** to manage the search order, prioritizing the exploration of the deepest unvisited nodes first.

---

## What is DFS?

DFS is a search strategy that prioritizes the depth of the graph. It uses the **Last-In, First-Out (LIFO)** principle to determine the next node to visit.

* **Principle**: LIFO (Last-In, First-Out).
* **Data Structure**: An explicit **Stack** (implemented here using a Python list and the `pop()` method).
* **Optimality**: **Not guaranteed** to find the shortest path in terms of the number of edges.
* **Completeness**: Complete for finite graphs, provided visited nodes are tracked correctly to prevent infinite loops in cyclic graphs.

---

## Code Structure

### Variables

1.  **`graph`**: A dictionary used to store the **Adjacency List** representation of the graph (nodes and their unweighted connections).
2.  **`visited`**: A list used to keep track of nodes that have already been explored. This is essential for **cycle detection** and preventing redundant processing.
3.  **`stack`**: A list that functions as the **LIFO stack**. Nodes are pushed onto and popped from this list to control the search path.

### Function

1.  **`dfs(visited, graph, node)`**: The main iterative function that performs the DFS traversal starting from the specified `node`.

### Execution Flow

1.  **Input**: The program takes user input to define the number of nodes, their names, and their neighbors, building the `graph` dictionary.
2.  **Initialization**: The `start` node is immediately pushed onto the `stack`.
3.  **Search Loop**: The `while stack:` loop continues as long as there are nodes to explore.
    * **Node Selection**: The last node added is removed using `stack.pop()`. This implements the LIFO stack behavior.
    * **Visit Check**: If the popped node (`m`) has **not** been `visited`:
        * It is printed and added to the `visited` list.
        * All its **unvisited** neighbors are then pushed onto the `stack`. By pushing all neighbors, the **last one pushed** will be the **first one popped** in the next iteration, forcing the search deeper down that branch.

---

## Complexity

* **Time Complexity**: $O(V + E)$, where $V$ is the number of vertices (nodes) and $E$ is the number of edges. Every node and every edge is processed exactly once.
* **Space Complexity**: $O(V)$, as the `visited` list and the `stack` store nodes, which, in the worst case, can hold all nodes in the graph.

---

## Applications

1.  **Topological Sorting**: Ordering tasks or items based on dependencies.
2.  **Cycle Detection**: Checking for loops in a graph.
3.  **Connectivity Analysis**: Finding connected components in a graph.
4.  **Solving Puzzles**: Used to find a solution path in problems like solving mazes.

---

## Advantages

1.  **Memory Efficiency**: Generally requires less memory than BFS for graphs with large branching factors because the stack only stores nodes along the current path.
2.  **Fast for Deep Goals**: Can find a deep goal node much faster than BFS by prioritizing depth.

---

## Disadvantages

1.  **Not Optimal**: Does not guarantee the shortest path.
2.  **Path Choice**: Can get lost exploring a very long, unproductive path while a much shorter path is available nearby.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
