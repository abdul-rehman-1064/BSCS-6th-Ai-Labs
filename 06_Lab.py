# Graph represented as an adjacency list
graph = {
    '1': ['2', '7', '8'],
    '2': ['3', '6'],
    '7': [],
    '8': ['9', '12'],
    '3': ['4', '5'],
    '6': [],
    '9': ['10', '11'],
    '12': [],
    '4': [],
    '5': [],
    '10': [],
    '11': []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    
    dfs_traversal = [start]  
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_traversal.extend(dfs(graph, neighbor, visited))  
            
    return dfs_traversal


dfs_result = dfs(graph, '8')
print("DFS Traversal:", dfs_result)