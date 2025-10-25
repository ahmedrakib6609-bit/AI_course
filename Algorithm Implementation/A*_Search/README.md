# A* Search Algorithm Implementation in Python

## Overview

This program implements the **A* Search** algorithm in Python, a popular pathfinding method that finds the shortest path from a start node to a goal node in a weighted graph. It combines **Dijkstra's algorithm** with **heuristics** to efficiently guide the search toward the goal.

This specific implementation takes the graph structure, heuristic values for each node, and the start and goal nodes as user input via the console.

---

## What is A\* Search?

A\* is an **informed search algorithm** that prioritizes nodes based on an estimated total cost, $f(n)$, which is the sum of two components:

* **$g(n)$**: The actual cost from the **start node** to the **current node $n$**.
* **$h(n)$**: A heuristic estimate of the cost from $n$ to the **goal**. This estimate must be **admissible** (i.e., it must never overestimate the actual cost).
* **$f(n) = g(n) + h(n)$**: The total estimated cost, used to prioritize which node to explore next.

The algorithm explores nodes with the lowest $f(n)$ first and stops when the goal is reached or no path exists.

---

## Code Structure

### Variables

1.  **`graph`**: A dictionary storing the adjacency list for the graph, including the **edge costs**.
2.  **`heuristic`**: A dictionary storing the **heuristic value ($h$-cost)** for each node.
3.  **`start` / `goal`**: The input nodes defining the beginning and end of the search.

### Key Data Structures

1.  **`open_list`**: A **min-heap** (implemented using Python's `heapq` library) that acts as a priority queue. It stores the nodes to be explored, prioritized by their $f$-cost. Each entry is a tuple: `(f_cost, g_cost, node, path, total_cost)`.
2.  **`closed_set`**: A set that stores the nodes that have already been fully visited and evaluated, preventing cycles and redundant processing.

### Main Execution Flow

1.  The program **collects graph topology, edge weights, and heuristic values** from the user input.
2.  The **`a_star_search`** function is called with the compiled data.
3.  Inside the function, the `open_list` is initialized with the start node.
4.  The search runs in a loop, continuously **popping the node with the lowest $f$-cost** from the `open_list`.
5.  If the popped node is the goal, the path and cost are printed. Otherwise, its neighbors are explored.

---

## How it Works

1.  **Initialization**: The search begins by adding the start node to the `open_list` with $g=0$ and $f=h(\text{start})$.
2.  **Node Selection**: The algorithm repeatedly selects the node with the **lowest $f$-cost** from the `open_list`.
3.  **Goal Check**: If the selected node is the goal, the search terminates successfully, and the optimal path is returned.
4.  **Neighbor Exploration**: For each neighbor of the selected node:
    * The new $g$-cost (distance from start) is calculated as $g(\text{current}) + \text{cost}(\text{current}, \text{neighbor})$.
    * The new $f$-cost is calculated as $g_\text{new} + h(\text{neighbor})$.
5.  **Update/Add**: If the neighbor has not been fully processed (not in `closed_set`), it is added to the `open_list` with its new costs and updated path.
6.  **Termination**: If the `open_list` becomes empty, it means the goal is unreachable.

---

## Complexity

* **Time Complexity**: $O(b^d)$, where $b$ is the branching factor and $d$ is the depth of the optimal path. With a consistent heuristic and efficient priority queue, it is often more efficient in practice, closer to $O(E \log V)$ in some graph structures (similar to Dijkstra's).
    * $V$: Number of vertices (nodes)
    * $E$: Number of edges
* **Space Complexity**: $O(b^d)$ or $O(V+E)$ in the worst case, as the `open_list` and `closed_set` may store all nodes and edges.

---

## Applications

1.  **Pathfinding**: Core algorithm in video games, robotics, and logistics for calculating the most efficient route.
2.  **Network Routing**: Used to find optimal data paths in computer networks.
3.  **Artificial Intelligence**: General state-space search problems.

---

## Advantages

1.  **Optimality**: Guarantees finding the **shortest path** if the heuristic used is **admissible**.
2.  **Efficiency**: Significantly more efficient than uninformed searches (like BFS or DFS) because the heuristic intelligently directs the search toward the goal.

---

## Disadvantages

1.  **Heuristic Quality**: Performance heavily relies on the quality of the heuristic function. A poor heuristic can make the search almost as slow as Dijkstra's algorithm.
2.  **Computational Cost**: For extremely large state spaces, storing the `open_list` and `closed_set` can lead to high memory consumption.

---

## Example Use Cases

1.  **Video Games**: Directing NPCs (Non-Player Characters) through complex maps while avoiding obstacles.
2.  **Autonomous Vehicles**: Real-time route planning and obstacle avoidance.
3.  **Logistics and Supply Chain**: Optimizing delivery routes to minimize distance and time.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
