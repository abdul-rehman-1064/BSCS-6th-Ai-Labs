# Define tree structure globally
children = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"]
}

values = {
    "D": 3, "E": 5,
    "F": 2, "G": 9
}

def minimax(node, depth, maximizingPlayer):
    # Step 2: base case
    if depth == 0 or node not in children:
        return values[node]

    if maximizingPlayer:
        maxEva = float('-inf')
        for child in children[node]:
            eva = minimax(child, depth - 1, False)
            maxEva = max(maxEva, eva)
        return maxEva
    else:
        minEva = float('inf')
        for child in children[node]:
            eva = minimax(child, depth - 1, True)
            minEva = min(minEva, eva)
        return minEva


# Initial call (same as in pseudo-code)
result = minimax("A", 3, True)
print("Optimal value:", result)




# Alpha-Beta Pruning Implementation

# Tree structure
children = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"]
}

values = {
    "D": 3, "E": 5,
    "F": 2, "G": 9
}

def minimax(node, depth, alpha, beta, maximizingPlayer):
    # Base case: leaf node or depth limit
    if depth == 0 or node not in children:
        return values[node]

    if maximizingPlayer:  # Maximizer's turn
        maxEva = float('-inf')
        for child in children[node]:
            eva = minimax(child, depth - 1, alpha, beta, False)
            maxEva = max(maxEva, eva)
            alpha = max(alpha, eva)  # update alpha
            if beta <= alpha:  # pruning condition
                print(f"Pruned at node {node} while checking {child}")
                break
        return maxEva
    else:  # Minimizer's turn
        minEva = float('inf')
        for child in children[node]:
            eva = minimax(child, depth - 1, alpha, beta, True)
            minEva = min(minEva, eva)
            beta = min(beta, eva)  # update beta
            if beta <= alpha:  # pruning condition
                print(f"Pruned at node {node} while checking {child}")
                break
        return minEva


# Initial call
result = minimax("A", 3, float('-inf'), float('inf'), True)
print("\nOptimal value with Alpha-Beta Pruning:", result)
