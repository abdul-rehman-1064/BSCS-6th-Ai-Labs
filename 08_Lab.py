
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90}
}

h = {
    'Arad': 366, 'Zerind': 374, 'Sibiu': 253, 'Timisoara': 329,
    'Oradea': 380, 'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242,
    'Craiova': 160, 'Rimnicu': 193, 'Fagaras': 176, 'Pitesti': 100,
    'Bucharest': 0, 'Giurgiu': 77
}


def a_star_recursive(node, goal, visited, g):
    if node == goal:
        return [node], g

    visited.add(node)
    best_path, best_cost = None, float("inf")

    for neighbor, cost in graph.get(node, {}).items():
        if neighbor not in visited:
            g_new = g + cost
            f_new = g_new + h[neighbor]

            # Recursive call
            path, total_g = a_star_recursive(neighbor, goal, visited.copy(), g_new)

            if path is not None:
                f_val = total_g + h[path[-1]]  # total f value
                if f_val < best_cost:
                    best_path = [node] + path
                    best_cost = total_g

    return best_path, best_cost


# Run the recursive A*
path, cost = a_star_recursive("Arad", "Bucharest", set(), 0)
print("Path found:", " -> ".join(path))
print("Total cost:", cost)
