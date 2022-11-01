''' 
In graph theory, a cycle graph or circular graph is a graph that consists of a single cycle, 
or in other words, some number of vertices connected in a closed chain
'''

def check_cycle_dfs(edges, st, n):

    adj = {i: [] for i in range(n + 1)}

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visit = set()

    def dfs(node, pt):
        visit.add(node)
        for ch in adj[node]:
            if ch not in visit:
                return dfs(ch, node) # assigning it's parent
            else:
                if ch != pt:
                    return 'Cycle'
        return 'No cycle'

    return dfs(st, -1) # starting node, parent node initially for root node there is no parent

def check_cycle_bfs(edges, st, n):
    
    adj = {i: [] for i in range(n + 1)}

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    q = [st] # queue
    visit = set()
    pt = -1 # parent node initially for root node there is no parent

    while q:
        node = q.pop(0)
        for ch in adj[node]:
            if ch not in visit:
                q.append(ch)
                visit.add(ch)
                pt = node # assigning it's parent
            else:
                if ch != pt:
                    return 'Cycle'
    return 'No cycle'


e = [[1, 2], [1, 3], [2, 3], [2, 4], [4, 5], [5, 1]]
e1 = [[0, 1],[0, 2],[1, 2],[2, 0],[2, 3],[3, 3]]
e2 = [[0, 1], [1, 2]]
e3 = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 4)]

# using dfs
print(check_cycle_dfs(e, 1, 5))
print(check_cycle_dfs(e1, 0, 3))
print(check_cycle_dfs(e2, 0, 2))
print(check_cycle_dfs(e3, 0, 5))

# using bfs
print(check_cycle_bfs(e, 1, 5))
print(check_cycle_bfs(e1, 0, 3))
print(check_cycle_bfs(e2, 0, 2))
print(check_cycle_bfs(e3, 0, 5))

