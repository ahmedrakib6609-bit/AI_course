def minimax(depth, node_index, is_maximizing, scores, max_depth):
    # Leaf node হলে value return করবে
    if depth == max_depth:
        return scores[node_index]

    if is_maximizing:
        return max(
            minimax(depth + 1, node_index * 2, False, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, scores, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, scores, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, scores, max_depth)
        )
scores = list(map(int, input("Enter leaf node values (space separated): ").split()))
import math
max_depth = int(math.log2(len(scores)))  # leaf থেকে depth হিসাব করা

print("\nRunning Minimax...")
best_value = minimax(0, 0, True, scores, max_depth)
print("The optimal value is:", best_value)

