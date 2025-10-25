# Breadth-First Search (BFS) Algorithm Implementation in Python

## Overview

This program implements the **Breadth-First Search (BFS)** algorithm, a fundamental **uninformed search algorithm** used for traversing or searching tree or graph data structures.

BFS explores the graph **level by level**, ensuring that all nodes at a given depth are visited before moving to the next depth. It is guaranteed to find the **shortest path** in an unweighted graph.

---

## What is BFS?

BFS is a simple strategy in which the current node is expanded, and all its immediate neighbors are generated. The core mechanism relies on a **First-In, First-Out (FIFO) Queue** to manage the order of node visitation.

* **Principle**: FIFO (First-In, First-Out).
* **Optimality**: Optimal for unweighted graphs (finds the shortest path in terms of the number of edges).
* **Completeness**: Complete (guaranteed to find a solution if one exists).

---

## Code Structure

### Variables

1.  **`graph`**: A dictionary used to store the **Adjacency List** representation of the graph.
2.  **`visited`**: A list used to keep track of nodes that have already been explored. This prevents cycles and redundant processing.
3.  **`queue`**: A list that functions as a **FIFO queue** to hold the nodes whose neighbors are yet to be fully explored.

### Function

1.  **`bfs(visited, graph, node)`**: The main function that performs the BFS traversal starting from the specified `node`.

### Execution Flow

1.  The program takes **user input** to define the graph structure (nodes and their neighbors).
2.  The user specifies a **starting node**.
3.  The starting node is added to both the `visited` list and the `queue`.
4.  The main `while queue:` loop iteratively:
    * **De-queues** the first element (`queue.pop(0)`).
    * **Prints** the dequeued node.
    * **En-queues** all unvisited neighbors of the dequeued node, simultaneously adding them to the `visited` list.

---

## Complexity

* **Time Complexity**: $O(V + E)$, where $V$ is the number of vertices (nodes) and $E$ is the number of edges. This is because every node and every edge is processed exactly once in the worst case.
* **Space Complexity**: $O(V)$, as in the worst case, all nodes may be stored in the `visited` list and the `queue`.

---

## Applications

1.  **Shortest Path**: Finding the shortest path between two nodes in an unweighted graph.
2.  **Web Crawlers**: Used to explore websites, going level by level from the starting page.
3.  **Connectivity Testing**: Checking if a graph is connected or finding all connected components.
4.  **Garbage Collection**: Used in certain memory management systems to identify reachable objects.

---

## Advantages

1.  **Guaranteed Shortest Path**: Finds the minimal path in terms of the number of edges.
2.  **Completeness**: Guaranteed to find a solution if one exists.

---

## Disadvantages

1.  **Memory Usage**: Can require significant memory to store the vast number of nodes in the queue, especially for graphs with large branching factors.
2.  **Efficiency on Deep Paths**: If the goal is very deep in a large graph, BFS might be slower than DFS, as it must explore all nodes at shallower levels first.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
