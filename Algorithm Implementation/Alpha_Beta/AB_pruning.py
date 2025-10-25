# =========================
# Alpha-Beta Pruning Example
# =========================

import math

def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    # Terminal node / leaf node
    if depth == 0 or isinstance(node, int):
        return node

    if maximizingPlayer:
        maxEval = -math.inf
        for child in node:
            eval = alpha_beta(child, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return maxEval
    else:
        minEval = math.inf
        for child in node:
            eval = alpha_beta(child, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return minEval

# =========================
# User input for tree
# =========================

def get_tree_input():
    tree = []
    level1 = int(input("Enter number of children for root: "))
    for i in range(level1):
        child = input(f"Enter leaf values of child {i+1} (space separated): ").split()
        # Convert strings to integers
        leaf_values = [int(x) for x in child]
        tree.append(leaf_values)
    return tree

# Main
tree = get_tree_input()
result = alpha_beta(tree, 2, -math.inf, math.inf, True)
print("Optimal value (with Alpha-Beta pruning):", result)
