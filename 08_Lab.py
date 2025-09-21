import heapq

# Graph representation (Bucharest Map example simplified)
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

# Heuristic values (straight-line distance to Bucharest)
h = {
    'Arad': 366, 'Zerind': 374, 'Sibiu': 253, 'Timisoara': 329,
    'Oradea': 380, 'Lugoj': 244, 'Mehadia': 241, 'Drobeta': 242,
    'Craiova': 160, 'Rimnicu': 193, 'Fagaras': 176, 'Pitesti': 100,
    'Bucharest': 0, 'Giurgiu': 77
}

def a_star(start, goal):
    # Priority queue (min-heap)
    open_list = [(h[start], 0, start, [start])]  # (f, g, node, path)
    closed_set = set()

    while open_list:
        f, g, node, path = heapq.heappop(open_list)  # best node nikalo
        if node == goal:
            return path, g  # path and cost
        if node in closed_set:
            continue
        closed_set.add(node)

        for neighbor, cost in graph.get(node, {}).items():
            if neighbor not in closed_set:
                g_new = g + cost
                f_new = g_new + h[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')


# Run the algorithm
path, cost = a_star("Arad", "Bucharest")
print("Path found:", " -> ".join(path))
print("Total cost:", cost)
