# Beam Search Algorithm Implementation in Python (Task 4)

## Overview

This program implements the **Beam Search** algorithm, a **heuristic search algorithm** used in Artificial Intelligence (AI) and pathfinding. Unlike Best-First Search, Beam Search limits the number of nodes expanded at each level by keeping only the top **$K$ (Beam Width)** most promising nodes, as determined by the heuristic function.

This implementation is designed as **Task 4** for an AI or Algorithms course, demonstrating the core mechanics of a limited-breadth, informed search.

---

## What is Beam Search?

Beam Search is an optimization of Breadth-First Search (BFS) that utilizes a heuristic function $h(n)$ to prioritize nodes.

* **Heuristic ($h(n)$):** An estimate of the cost from the current node $n$ to the goal. In this implementation, the search favors nodes with the **lowest** $h(n)$ (assuming $h(n)$ estimates the remaining cost).
* **Beam Width ($K$):** A parameter that dictates the maximum number of best-promising nodes kept at each level of the search.

By limiting the search breadth to $K$, Beam Search reduces memory usage and execution time, but it **sacrifices completeness and optimality**.

---

## Code Structure

### Variables

1.  **`graph`**: A dictionary storing the graph's **adjacency list** (unweighted connections).
2.  **`heuristic`**: A dictionary storing the **heuristic value ($h$-cost)** for each node.
3.  **`start` / `goal`**: The input nodes for the search.
4.  **`beam_width`**: The integer $K$ provided by the user, limiting the number of nodes expanded in parallel.

### Function

1.  **`beam_search(graph, start, goal, heuristic, beam_width)`**: The main function that executes the Beam Search logic.

### Internal Data Structures

1.  **`queue`**: A list storing the nodes currently being considered for expansion at the current level: `(h(n), node, path)`.
2.  **`new_queue`**: A temporary list used to collect all successors before pruning.

---

## How it Works

1.  **Initialization**: The search starts with the `queue` containing the **`start`** node.
2.  **Expansion**: All nodes in the current `queue` are expanded, and all their neighbors are added to the **`new_queue`**.
3.  **Goal Check**: The goal check happens **before** expansion at each level.
4.  **Sorting**: The `new_queue` (containing all successors) is sorted based on the **heuristic value ($h(n)$)**, prioritizing the lowest values.
5.  **Pruning (Limiting)**: The `queue` for the next iteration is reset to the **first `beam_width` ($K$)** elements of the sorted `new_queue`.
6.  **Termination**: If the goal is found, the path is printed. If the loop finishes without finding the goal, the search fails.

---

## Complexity

* **Time Complexity (Average)**: $O(K \cdot d \cdot b)$, where $K$ is the beam width, $d$ is the depth of the solution, and $b$ is the branching factor.
* **Space Complexity (Average)**: $O(K \cdot d)$. It is highly memory efficient.

---

## Advantages

1.  **Memory Efficiency**: Drastically **reduces memory usage** by limiting the number of stored nodes to $K$ per level.
2.  **Time Efficiency**: Typically **faster** than traditional Best-First Search by exploring fewer nodes overall.

---

## Disadvantages

1.  **Not Optimal**: It is **not guaranteed to find the shortest path** because it prunes potentially optimal branches.
2.  **Not Complete**: If the optimal or only path lies outside the beam width $K$, the algorithm will **fail to find the goal**, even if a path exists.

---

## Applications

1.  **Natural Language Processing (NLP)**: Used heavily in **machine translation** and **speech recognition** to find the most probable output sequence.
2.  **Robotics**: Quick, sub-optimal path planning in constrained environments.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
