# Depth-Limited Search (DLS) Algorithm Implementation in Python (Recursive)

## Overview

This program implements the **Depth-Limited Search (DLS)** algorithm, a variation of Depth-First Search (DFS) that is constrained by a maximum depth. DLS is an **uninformed search algorithm** that explores the graph as deep as possible, but only up to a predefined limit.

DLS is primarily used to prevent the search from getting trapped in **infinite loops** within cyclic graphs or spending excessive time exploring deep, non-productive branches.

---

## What is Depth-Limited Search (DLS)?

DLS is essentially a depth-first search where the search depth is bounded by an integer value, $L$ (represented here by `max_depth`).

* **Depth Limit ($L$):** The maximum depth allowed for the search. Any node beyond this depth is treated as a terminal node (a dead end).
* **Search Strategy:** It uses the same recursive, LIFO (Last-In, First-Out) strategy as DFS.
* **Goal:** To find a path to the goal node, $G$, only if the length of that path is **less than or equal to $L$**.

### Key DLS Outcomes

1.  **Goal Found:** The target is reached within the limit.
2.  **Cutoff:** The search reached the depth limit without finding the goal.
3.  **Failure:** The search explored all reachable nodes within the limit, and the goal was not found.

---

## Code Structure

### Function

1.  **`dls(current, target, depth, path)`**: The core recursive function that performs the Depth-Limited Search.

### Variables

1.  **`graph`**: A dictionary storing the graph's **Adjacency List** representation (unweighted connections).
2.  **`start` / `goal`**: The input nodes for the search.
3.  **`max_depth`**: The integer input $L$ that limits the maximum search depth.
4.  **`current`**: The node currently being visited in the recursion.
5.  **`depth`**: The current depth of the search (starts at 0).
6.  **`path`**: The list of nodes from the start to the `current` node, used for **cycle prevention** and path reconstruction.

### Execution Flow

1.  **Initialization**: The recursive search starts with `dls(start, goal, 0, [])`.
2.  **Path Extension**: The `current` node is added to the `new_path` for the current call.
3.  **Goal Check**: If `current == target`, the path is returned.
4.  **Cutoff Check**: If `depth >= max_depth`, the search stops on this branch and returns `None` (representing a cutoff).
5.  **Cycle Prevention**: The code checks `if neighbor in new_path` to avoid visiting a node already on the current path, preventing simple cycles.
6.  **Recursion**: For each unvisited neighbor, `dls` is called recursively with an incremented `depth`.
7.  **Path Result**: If any recursive call returns a valid `result` (the path list), that result is immediately passed back up the call stack.

---

## Complexity

* **Time Complexity**: $O(b^L)$, where $b$ is the branching factor and $L$ is the depth limit. The complexity is bounded by the limit $L$.
* **Space Complexity**: $O(b \cdot L)$, which is dominated by the recursion stack depth $L$.

---

## Applications

1.  **Iterative Deepening Search (IDS/IDDFS)**: DLS is the core component of the more powerful IDDFS algorithm, where the depth limit is gradually increased.
2.  **Search Space Pruning**: Used to enforce resource constraints (time/memory) on a search process.
3.  **Structured Search**: Applicable when solutions are known to exist within a certain, narrow depth (e.g., Chess where only moves up to depth 3 are considered).

---

## Advantages

1.  **Cycle Prevention**: Naturally avoids infinite loops in graphs with cycles by enforcing the maximum depth limit $L$.
2.  **Memory Efficiency**: Due to its DFS nature, it is highly memory efficient, requiring space proportional only to the current path depth ($O(L)$).

---

## Disadvantages

1.  **Incompleteness**: If the shallowest solution exists at a depth greater than $L$, DLS will **fail to find the goal**.
2.  **Non-Optimality**: Like DFS, if multiple paths exist within the limit, the first one found (not necessarily the shortest) is returned.
3.  **Blind Choice of $L$**: The effectiveness of DLS heavily depends on choosing the correct `max_depth` ($L$).

---

## License

This project is open-source — feel free to use, modify, or distribute it.
