# Best-First Search Algorithm Implementation in Python

## Overview

This program implements the **Best-First Search (BFS)** algorithm, which is an **informed search technique** used to find a path from a start node to a goal node in a graph. Unlike standard Breadth-First Search, BFS uses a **heuristic function** to prioritize which node to explore next, always expanding the node that appears closest to the goal.

This implementation is designed to work on **unweighted graphs** (where all edge costs are considered equal) and demonstrates the concept of greedy exploration guided solely by the heuristic.

---

## What is Best-First Search (Greedy Search)?

Best-First Search (often called **Greedy Best-First Search**) is a heuristic search algorithm that operates similarly to Breadth-First Search but uses a priority queue instead of a standard FIFO queue.

* **Heuristic ($h(n)$):** The only factor guiding the search is the **heuristic value ($h$-cost)**, which is an estimate of the cost from the current node $n$ to the goal.
* **Prioritization:** At every step, the algorithm selects the node from the frontier (priority queue) with the **lowest $h(n)$** (the "best" node) and expands it first.
* **Search Type:** It is a **greedy** approach because it only looks at the immediate heuristic value, ignoring the path cost from the start node ($g$-cost).

---

## Code Structure

### Function

1.  **`best_first_search(graph, start, goal, heuristic)`**: The main function that executes the Best-First Search logic.

### Variables

1.  **`graph`**: A dictionary storing the graph's **adjacency list** (unweighted connections).
2.  **`heuristic`**: A dictionary storing the **heuristic value ($h$-cost)** for each node.
3.  **`start` / `goal`**: The input nodes for the search.
4.  **`visited_order`**: A list to track the sequence of nodes visited.
5.  **`visited`**: A set to store nodes that have already been fully expanded.
6.  **`priority_queue`**: A **min-heap** (using `heapq`) that stores nodes to be explored, prioritized by $h(n)$. The elements are tuples: `(h(n), node)`.
7.  **`parent`**: A dictionary tracking parent pointers for path reconstruction.

### External Libraries

* **`heapq`**: Python's implementation of the heap queue algorithm, used to efficiently manage the priority queue.

---

## How it Works

1.  **Initialization**: The search begins by adding the **`start`** node and its heuristic value to the `priority_queue`.
2.  **Search Loop**: The loop continues as long as the `priority_queue` is not empty.
3.  **Node Selection**: `heapq.heappop` extracts the node with the **lowest heuristic value ($h$-cost)** from the queue. This is the "best" node to expand.
4.  **Goal Check**: If the selected node is the `goal`, the path is reconstructed by tracing back through the `parent` pointers, and the search terminates successfully.
5.  **Expansion**: The current node is added to the `visited` set.
6.  **Neighbor Evaluation**: For each unvisited and unqueued neighbor:
    * Its parent is set to the current node.
    * It is added to the `priority_queue` along with its heuristic value.
7.  **Termination**: If the `priority_queue` becomes empty without finding the goal, no path exists.

---

## Complexity

* **Time Complexity**: $O(b^m)$ in the worst case, where $b$ is the branching factor and $m$ is the depth of the solution. However, with a good heuristic, it is generally much faster as it explores far fewer nodes than an uninformed search.
* **Space Complexity**: $O(b^m)$, as it may need to store all nodes in the worst case (in the `visited` set and `priority_queue`).

---

## Applications

1.  **Pathfinding**: Used in AI to quickly find a path in a graph when the primary concern is the estimated distance to the goal, not necessarily the shortest path.
2.  **Heuristic Search**: A foundation for more complex searches like A\*, demonstrating the power of greedy exploration.
3.  **Game AI**: Can be used for fast but sub-optimal pathfinding for non-critical agents.

---

## Advantages

1.  **Efficiency**: When the heuristic is accurate, it is significantly **faster** than uninformed searches like BFS because it focuses its efforts towards the goal.
2.  **Simplicity**: Simpler to implement than A\* because it only considers $h(n)$ and ignores $g(n)$ (path cost).

---

## Disadvantages

1.  **Not Optimal**: It is **not guaranteed to find the shortest path** (the one with the fewest steps). It may get stuck following a path with a low heuristic value that is actually very long.
2.  **Incompleteness**: Like Beam Search, it can sometimes be **incomplete** if a poor heuristic leads it down an infinite path without backtracking to find a short path.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
