
graph = {
    'A': ['B', 'F','D','E'],
    'B': ['K', 'J'],
    'F': [],
    'D': ['G'],
    'E': ['C','H','I'],
    'K': ['N','M'],
    'J': [],
    'G': [],
    'C': [],
    'H': [],
    'I': ['L'],
}

# Breadth-First Search function
def bfs(graph, start, goal):
    # Create a queue for BFS
    queue = []
    # Keep track of visited nodes
    visited = []
    
    if start == goal:
        print("Goal node ", goal, "found!")
        return
    
    # Add the starting node to the queue and mark as visited
    queue.append(start)
    visited.append(start)

    while queue:
        # Remove the first element from the queue
        node = queue.pop(0)
        print("Visiting:", node)
        
        # If we find the goal, stop the search
        if node == goal:
            print("Goal node", goal, "found!")
            return
        
        # Add neighbors to the queue if not visited
        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

# Call the function
bfs(graph, 'A', 'G')
