graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'J': [],
    'F': [],
    'D': ['G'],
    'G': [],
    'E': ['C', 'H', 'I'],
    'C': [],
    'H': [],
    'I': ['L'],
    'L': [],
    'N': [],
    'M': []
}

def dls(node, goal, limit, path):
    path.append(node)
    print('limit========>',limit)
    print('path========>',path)
    if node == goal:
        return True
    if limit <= 0:
        path.pop()
        return False
    for neighbor in graph.get(node, []):
        if dls(neighbor, goal, limit - 1, path):
            return True
    path.pop()
    return False

def iddfs(start, goal, max_depth):
    for depth in range(max_depth):
        path = []
        print(f"Trying depth limit: {depth}")
        if dls(start, goal, depth, path):
            return path
    return None


start_node = 'A'
goal_node = 'G'
max_depth = 4  

result_path = iddfs(start_node, goal_node, max_depth)

if result_path:
    print(f"\nGoal '{goal_node}' found! Path: {' -> '.join(result_path)}")
else:
    print(f"\nGoal '{goal_node}' not found within depth limit.")