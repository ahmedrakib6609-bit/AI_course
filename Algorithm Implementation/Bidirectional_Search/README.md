# Bidirectional Search Algorithm Implementation in Python

## Overview

This program implements the **Bidirectional Search** algorithm, an **uninformed search technique** used to find the shortest path between a start node and a goal node in an **unweighted graph**.

Instead of searching in a single direction (like standard Breadth-First Search, BFS), this algorithm searches simultaneously from the start node and backward from the goal node. The search terminates when the two frontiers intersect, resulting in a significantly faster path discovery in large search spaces.

---

## What is Bidirectional Search?

Bidirectional Search is a graph traversal technique that aims to find the shortest path more efficiently than single-directional searches.

* **Dual Search:** It runs two concurrent searches: a **forward search** from the start node and a **backward search** from the goal node.
* **Termination:** The search stops when a node is expanded by one search (e.g., forward search) and is already present in the visited set of the other search (e.g., backward search). This intersecting node is the **meeting point**.
* **Suitability:** It is primarily used on unweighted graphs where the step cost is uniform (like a standard BFS) to ensure the path found upon meeting is indeed the shortest path.

---

## Code Structure

### Variables

1.  **`graph`**: A dictionary storing the graph's **adjacency list** (unweighted connections).
2.  **`start` / `goal`**: The input nodes for the search.
3.  **`start_parent`**: A dictionary tracking parent pointers for the forward search (from start). Used for path reconstruction.
4.  **`goal_parent`**: A dictionary tracking parent pointers for the backward search (from goal). Used for path reconstruction.
5.  **`start_queue` / `goal_queue`**: Deques (using `collections.deque`) used for BFS-style expansion from the start and goal sides, respectively.
6.  **`meeting_node`**: The node where the two concurrent searches intersect.

### External Libraries

* **`collections.deque`**: Used to implement the efficient queues required for the BFS nature of the search.

---

## How it Works

1.  **Initialization**: Two independent BFS processes are initialized: one starting at `start` and one at `goal`. Each process has its own queue (`start_queue`, `goal_queue`) and parent dictionary (`start_parent`, `goal_parent`).
2.  **Alternating Expansion**: The `while` loop alternates between expanding one level from the forward search and one level from the backward search.
3.  **Forward Search**: A node is popped from `start_queue`. Its unvisited neighbors are added to `start_parent` and pushed to `start_queue`.
4.  **Intersection Check (Forward)**: Immediately after a neighbor is visited by the forward search, it checks if that neighbor has already been visited by the backward search (i.e., if it exists in `goal_parent`). If it exists, the intersection is found, and the search breaks.
5.  **Backward Search**: The same process is repeated by expanding a node from `goal_queue` and checking for intersection with `start_parent`.
6.  **Path Reconstruction**: Once the `meeting_node` is found, the final path is constructed in two parts:
    * Tracing back from the `meeting_node` to the `start` node using the **`start_parent`** map (which is then reversed).
    * Tracing forward from the `meeting_node` to the `goal` node using the **`goal_parent`** map.
7.  **Termination**: The two path segments are joined at the `meeting_node` to form the final shortest path.

---

## Complexity

* **Time Complexity**: $O(b^{d/2})$, where $b$ is the branching factor and $d$ is the depth of the solution. This is a significant improvement over single-directional BFS, which is $O(b^d)$. Searching half the depth leads to an exponential decrease in complexity.
* **Space Complexity**: $O(b^{d/2})$, as the algorithm needs to store the visited nodes and parent pointers for both searches up to the meeting point.

---

## Applications

1.  **Pathfinding**: Finding the shortest path in social networks, road maps, or game environments where edges are unweighted or have uniform cost.
2.  **Network Routing**: Identifying the optimal route in wide-area network routing protocols.
3.  **Reachability Analysis**: Quickly determining if two points in a large graph are connected.

---

## Advantages

1.  **Efficiency**: Dramatically reduces the time complexity from exponential $O(b^d)$ to $O(b^{d/2})$, making it much faster for large graphs with deep solutions.
2.  **Reduced Search Space**: The search space is much smaller, as the two search frontiers only have to explore up to half the full depth.

---

## Disadvantages

1.  **Implementation Complexity**: More complex to implement than standard BFS due to the management of two concurrent searches and the path reconstruction logic.
2.  **Heuristic Limitation**: It is an uninformed search; it cannot easily be adapted to weighted graphs (like A*) without complex modifications to handle different edge costs correctly.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
