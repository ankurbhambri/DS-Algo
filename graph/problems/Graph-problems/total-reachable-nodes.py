from collections import defaultdict, deque

# DFS

def dfs(node, visited, adj):
    visited[node] = True
    count = 1  # Count current node
    for neighbor in adj[node]:
        if not visited[neighbor]:
            count += dfs(neighbor, visited, adj)
    return count


adj = defaultdict(list)
edges = [
    (0, 1), (1, 2),
    (3, 4)
]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

n = 5  # total number of nodes
result = [0] * n

for i in range(n):
    visited = [False] * n
    result[i] = dfs(i, visited, adj)

print("Reachable nodes from each node:")
for i in range(n):
    print(f"Node {i}: {result[i]}")


# BFS
def bfs(start, adj, n):

    visited = [False] * n
    queue = deque([start])
    visited[start] = True

    count = 1  # count of reachable nodes

    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                count += 1
                queue.append(neighbor)
    
    return count

n = 5
result = []
adj = defaultdict(list)
edges = [
    (0, 1), (1, 2),
    (3, 4)
]

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

for i in range(n):
    result.append(bfs(i, adj, n))
