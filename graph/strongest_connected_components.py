'''
Ways to find Strongly connected components in a graph

1. Brute force

    a. Find all pairs shortest path using Floyd warshall algo.
    b. Check if between any two pairs the distance is infinity
       (i.e, unreachable) except self loops.

2. Kosaraju Algorithm
    a. Perform DFS traversal of graph. Push node to stack before returning.
    b. Find the transpose graph by reversing the edges.
    c. Pop nodes one by one from stack and again do DFS on modifies graph.(Keep popping nodes)
'''
# T.C  = 3 * (V + E) = O(V + E)


def dfs2(node, visited):
    print(node)
    visited[node] = True
    for nei in graph[node]:
        if not visited[nei]:
            dfs2(nei, visited)


def reverse_graph(graph, n):
    for i in range(n):
        for j in graph[i]:
            graph[j].append(i)
    return graph


def dfs(node, visited, st):
    visited[node] = True
    for nei in graph[node]:
        if not visited[nei]:
            dfs(nei, visited, st)
    st.append(node)


def findSCCs(graph, n):

    visit = {i: False for i in range(n)}
    st = []

    for i in range(n):
        if not visit[i]:
            dfs(i, visit, st)

    graph = reverse_graph(graph, n)

    visit = {i: False for i in range(n)}  # reset visit false

    print("Strongly connected components are: \n")
    while st:
        node = st.pop(0)
        if not visit[i]:
            dfs2(node, visit)
            print("\n")


graph = {i: [] for i in range(8)}
graph[0].append(1)
graph[1].append(2)
graph[2].append(0)
graph[3].append(4)
graph[4].append(5)
graph[4].append(7)
graph[5].append(6)
graph[6].append(4)
graph[6].append(7)

findSCCs(graph, 8)
