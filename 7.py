# Graph nodes: A, B, C, D, E (index 0 to 4)

# Adjacency matrix representation for DFS
graph_matrix = [
    [0, 1, 1, 0, 0],  # A connected to B and C
    [1, 0, 0, 1, 0],  # B connected to A and D
    [1, 0, 0, 1, 1],  # C connected to A, D, E
    [0, 1, 1, 0, 1],  # D connected to B, C, E
    [0, 0, 1, 1, 0]   # E connected to C, D
]

def dfs(node, visited):
    visited[node] = True
    print(chr(node + 65), end=' ')  # Convert 0->A, 1->B, etc.
    for neighbor in range(len(graph_matrix)):
        if graph_matrix[node][neighbor] == 1 and not visited[neighbor]:
            dfs(neighbor, visited)

print("DFS traversal starting from A:")
visited = [False] * 5
dfs(0, visited)  # Start at node A (0)

# Adjacency list representation for BFS
graph_list = {
    0: [1, 2],   # A connected to B, C
    1: [0, 3],   # B connected to A, D
    2: [0, 3, 4],# C connected to A, D, E
    3: [1, 2, 4],# D connected to B, C, E
    4: [2, 3]    # E connected to C, D
}

from collections import deque

def bfs(start):
    visited = [False] * 5
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(chr(node + 65), end=' ')
        for neighbor in graph_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

print("\nBFS traversal starting from A:")
bfs(0)
