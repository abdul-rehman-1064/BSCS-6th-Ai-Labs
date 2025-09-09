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