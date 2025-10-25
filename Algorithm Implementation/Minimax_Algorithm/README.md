# Minimax Search Algorithm Implementation in Python (Recursive)

## Overview

This program implements the **Minimax Search Algorithm**, a foundational decision-making algorithm in **Artificial Intelligence (AI)**, particularly for two-player, zero-sum games (where one player's gain is exactly equal to the other player's loss).

This implementation models the game as a **perfect binary tree** where the goal is to find the **optimal value** (the highest score the Maximizing Player can guarantee) assuming the Minimizing Player also plays optimally.

---

## What is the Minimax Algorithm?

Minimax is a **recursive, depth-first search algorithm** that works by traversing a game tree and assigning a value to each node. This value represents the **best score** the current player can achieve from that point onward, assuming the opponent plays to minimize that score.

* **Maximizing Player (MAX):** Aims to choose the move that leads to the **maximum** possible score.
* **Minimizing Player (MIN):** Aims to choose the move that leads to the **minimum** possible score (thus minimizing the MAX player's score).
* **Zero-Sum Game:** The underlying assumption is that the total gain/loss for both players is zero.

### Tree Structure

The code assumes a **perfect binary tree** structure:
* The children of any node $N$ at index $I$ are at indices $2I$ and $2I + 1$.
* The depth of the tree is calculated based on the number of leaf nodes ($2^{\text{max\_depth}} = \text{len}(\text{scores})$).

---

## Code Structure

### Function

1.  **`minimax(depth, node_index, is_maximizing, scores, max_depth)`**: The core recursive function that performs the Minimax search.

### Variables

1.  **`scores`**: A list of integers representing the utility values or payoffs at the **leaf nodes** of the game tree.
2.  **`max_depth`**: The total depth of the game tree (from root to leaves), calculated from the number of leaf nodes as $\log_2(\text{len}(\text{scores}))$.
3.  **`depth`**: The current recursion level (starts at 0 for the root).
4.  **`node_index`**: The index of the current node being evaluated (starts at 0 for the root, following a complete binary tree indexing scheme).
5.  **`is_maximizing`**: A boolean flag (`True` or `False`) indicating the current player's role.

### Execution Flow

1.  **Input**: The program takes the **leaf node values** as a space-separated string.
2.  **Depth Calculation**: The total depth (`max_depth`) is determined using the base-2 logarithm of the number of leaf nodes.
3.  **Base Case**: If `depth == max_depth`, the function returns the value from the `scores` list at the calculated `node_index`.
4.  **MAX Node Logic**: If `is_maximizing` is `True`, the function recursively calls itself for both children and returns the **maximum** of the two returned values.
5.  **MIN Node Logic**: If `is_maximizing` is `False`, the function recursively calls itself for both children and returns the **minimum** of the two returned values.
6.  **Optimal Value**: The final result returned by the initial call (`minimax(0, 0, True, ...)` ) is the best guaranteed score for the Maximizing Player.

---

## Complexity

* **Time Complexity**: $O(b^m)$, where $b$ is the branching factor (which is 2 in this binary tree implementation) and $m$ is the maximum depth of the tree. The algorithm must explore **every node** in the game tree.
* **Space Complexity**: $O(m)$, as it is a depth-first search, and the space is dominated by the depth of the recursion stack.

---

## Applications

1.  **Game AI**: Core logic for classic deterministic games like **Tic-Tac-Toe, Chess, and Checkers** (though often optimized with Alpha-Beta Pruning for larger games).
2.  **Decision Making**: Any decision scenario where two opposing entities make sequential choices, and the outcome is zero-sum.
3.  **Modeling Optimal Behavior**: Used to model how two rational, competing agents would act in a simple scenario.

---

## Advantages

1.  **Optimality**: When applied to a full game tree, it guarantees finding the **optimal move** that maximizes the player's outcome against an optimal opponent.
2.  **Simplicity**: The concept is straightforward and easily implemented through recursion.

---

## Disadvantages

1.  **Time Cost**: The exponential time complexity ($O(b^m)$) makes it impractical for games with large branching factors and deep search trees (e.g., Chess, which often requires Minimax to be combined with heuristics and pruning).
2.  **Fixed Tree Structure**: This implementation is tailored for a specific perfect binary tree structure.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
