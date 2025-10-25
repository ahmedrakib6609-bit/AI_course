# Iterative Deepening Search (IDS) Algorithm Implementation in Python

## Overview

This program implements the **Iterative Deepening Search (IDS)** algorithm, which is a powerful combination of **Depth-Limited Search (DLS)** and **Breadth-First Search (BFS)** characteristics.

IDS systematically explores the search space by executing a series of increasing-depth DLS searches. It starts with a depth limit of 0, then 1, then 2, and so on, until the goal is found or the overall maximum depth is reached.

---

## What is Iterative Deepening Search (IDS)?

IDS is an **uninformed search algorithm** designed to achieve the **optimality and completeness of BFS** while retaining the **memory efficiency of DFS**.

* **Core Idea:** It calls the **DLS** function repeatedly, increasing the depth limit ($L$) by 1 in each iteration.
* **Completeness:** It is guaranteed to find a solution if one exists (just like BFS).
* **Optimality:** It is guaranteed to find the **shallowest (shortest)** solution in an unweighted graph (just like BFS).

### Role of DLS

The `dls` function is the engine of the search. It performs a standard Depth-First Search but stops immediately when the current search level (`level`) equals the current depth limit (`depth_limit`).

---

## Code Structure

### Functions

1.  **`dls(node, goal, depth_limit, graph, level=0)`**:
    * Performs a recursive Depth-Limited Search.
    * Prints the currently visited node and its depth.
    * Returns `True` if the goal is found within the limit, and `False` otherwise (due to cutoff or failure).
2.  **`ids(start, goal, max_depth, graph)`**:
    * The main function that controls the iterative process.
    * Uses a `for` loop to increase the depth limit from 0 up to `max_depth`.
    * Calls `dls` in each iteration.

### Variables

1.  **`graph`**: A dictionary storing the graph's **Adjacency List**.
2.  **`start_node` / `goal_node`**: The nodes defining the search endpoints.
3.  **`max_depth`**: The user-defined overall maximum depth the IDS process will search up to.
4.  **`level`**: The current recursion depth within the `dls` function.

---

## How it Works

1.  **Depth Iteration**: The `ids` function starts a loop (`for depth in range(max_depth + 1)`).
2.  **DLS Call**: In each iteration, it calls `dls(start, goal, depth, ...)`:
    * **Iteration 0**: `dls` searches only the nodes at depth 0 (just the start node).
    * **Iteration 1**: `dls` searches nodes up to depth 1.
    * **...**
    * **Iteration $k$**: `dls` searches nodes up to depth $k$.
3.  **Goal Check**: If `dls` finds the goal in the current iteration, it returns `True`, and the `ids` search terminates immediately, having found the shortest path.
4.  **Cutoff vs. Success**: If `dls` returns `False`, the `ids` loop moves to the next depth limit.
5.  **Final Termination**: If the loop completes without finding the goal, the goal is unreachable within the specified `max_depth`.

---

## Complexity

* **Time Complexity**: $O(b^d)$, where $b$ is the branching factor and $d$ is the depth of the shallowest solution. Although IDS re-explores shallow nodes repeatedly, the asymptotic complexity remains the same as BFS and DFS because the vast majority of computation occurs at the final, deepest level.
* **Space Complexity**: $O(b \cdot d)$, which is proportional only to the current depth limit $d$. This is a huge advantage over BFS, which requires $O(b^d)$ space.

---

## Applications

1.  **Uninformed Search**: The preferred uninformed search algorithm when the search space is large and the depth of the solution is unknown.
2.  **Game AI**: Can be used in simpler games to find optimal moves without exhausting memory.
3.  **Pathfinding**: Finding the shortest path in unweighted graphs when memory is a critical constraint.

---

## Advantages

1.  **Optimal and Complete**: Guaranteed to find the shallowest path (optimal) and guaranteed to find the goal if one exists (complete).
2.  **Memory Efficient**: Due to its reliance on DFS, it uses memory proportional only to the depth ($O(d)$), unlike BFS ($O(b^d)$).
3.  **Fast**: Despite repeated exploration of shallow nodes, it is often faster than BFS in practice due to the overhead of managing a large queue in BFS.

---

## Disadvantages

1.  **Redundant Work**: It repeatedly generates states from shallower levels, which can be inefficient if the solution is very deep. (This cost is asymptotically minor, but noticeable).
2.  **Not Ideal for Weighted Graphs**: Designed for unweighted graphs; it cannot find the cheapest path in a graph with varying edge costs.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
