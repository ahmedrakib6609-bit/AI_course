# Alpha-Beta Pruning Implementation in Python (Minimax Optimization)

## Overview

This program implements the **Alpha-Beta Pruning** algorithm, which is an optimization technique for the **Minimax search algorithm**. Alpha-Beta Pruning reduces the number of nodes evaluated in the search tree without affecting the final result, making the game-playing AI more efficient.

The implementation handles a fixed-depth game tree where the goal is to find the optimal move for the **Maximizing Player** (usually the AI) against an optimal opponent (the **Minimizing Player**).

---

## What is Alpha-Beta Pruning?

Alpha-Beta Pruning is a depth-first search algorithm used to find the optimal move in a zero-sum game by pruning (eliminating) branches that cannot possibly influence the final decision.

It uses two key parameters:

* **Alpha ($\alpha$)**: The best value (highest) found so far for the **Maximizing Player** along the path from the root. It is initialized to $-\infty$.
* **Beta ($\beta$)**: The best value (lowest) found so far for the **Minimizing Player** along the path from the root. It is initialized to $+\infty$.

### The Cutoffs

1.  **Beta Cutoff (Maximizing Player)**: If $\beta \le \alpha$, the Maximizing Player can stop considering further children of the current node. This happens when the current Maximizing node finds a value that is already guaranteed to be worse for the Minimizing Player (its parent) than a previously found option.
2.  **Alpha Cutoff (Minimizing Player)**: If $\beta \le \alpha$, the Minimizing Player can stop considering further children. This happens when the current Minimizing node finds a value that is already guaranteed to be worse for the Maximizing Player (its parent) than a previously found option.

---

## Code Structure

### Function

1.  **`alpha_beta(node, depth, alpha, beta, maximizingPlayer)`**: The core recursive function that performs the Alpha-Beta search.

### Variables

1.  **`node`**: Represents the current node being evaluated. This can be a list (an internal node with children) or an integer (a terminal leaf node).
2.  **`depth`**: The remaining depth to search. The search stops when `depth == 0`.
3.  **`alpha`**: The best score found so far for the Maximizer on the current path.
4.  **`beta`**: The best score found so far for the Minimizer on the current path.
5.  **`maximizingPlayer`**: A boolean flag (`True` or `False`) indicating whose turn it is.

### User Input and Main

1.  **`get_tree_input()`**: A utility function that takes user input to construct the game tree (specifically, the leaf values grouped by their parent node).
2.  **Tree Structure**: The game tree is represented by a nested list of integers (the leaf node values).
3.  **Initial Call**: The search is initiated from the root with `depth=2`, `alpha=-inf`, `beta=+inf`, and `maximizingPlayer=True`.

---

## How it Works

1.  **Terminal Check**: The recursion base case checks if the node is a leaf (depth 0 or `isinstance(node, int)`).
2.  **Maximizing Player ($\text{MAX}$)**:
    * Initializes `maxEval` to $-\infty$.
    * Iterates through children and recursively calls `alpha_beta`.
    * Updates `maxEval` with the maximum value returned.
    * Updates $\alpha$: $\alpha = \max(\alpha, \text{eval})$.
    * **Pruning**: If $\beta \le \alpha$, the loop breaks immediately (Beta Cutoff).
3.  **Minimizing Player ($\text{MIN}$)**:
    * Initializes `minEval` to $+\infty$.
    * Iterates through children and recursively calls `alpha_beta`.
    * Updates `minEval` with the minimum value returned.
    * Updates $\beta$: $\beta = \min(\beta, \text{eval})$.
    * **Pruning**: If $\beta \le \alpha$, the loop breaks immediately (Alpha Cutoff).
4.  **Result**: The final output is the highest value the Maximizing Player can achieve, assuming the Minimizing Player plays optimally.

---

## Complexity

* **Time Complexity (Best Case)**: $O(b^{m/2})$, where $b$ is the branching factor (number of children per node) and $m$ is the depth of the tree. This occurs when the best moves are always explored first, maximizing pruning efficiency.
* **Time Complexity (Worst Case)**: $O(b^m)$, which is the same as the Minimax algorithm without pruning. This happens when the ordering of nodes prevents effective pruning.
* **Space Complexity**: $O(m)$ (linear with depth), as it is a depth-first search.

---

## Applications

1.  **Game AI**: Core algorithm for classical board games like **Chess, Checkers, and Go**.
2.  **Decision Making**: Used in any scenario that can be modeled as a two-player, zero-sum game tree.
3.  **Optimizing Search**: General technique to efficiently search large, complex state spaces.

---

## Advantages

1.  **Efficiency**: Dramatically reduces the number of nodes searched compared to Minimax, making complex games solvable within time limits.
2.  **Optimality**: Retains the **same optimal result** as the full Minimax search.

---

## Disadvantages

1.  **Move Ordering**: Performance heavily depends on the order in which children are explored. Good move ordering maximizes the pruning effect.
2.  **Fixed Depth**: Typically requires a fixed search depth, and choosing the right depth is crucial for performance and quality of play.

---

## License

This project is open-source — feel free to use, modify, or distribute it.
