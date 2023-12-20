# https://www.geeksforgeeks.org/shortest-cycle-in-an-undirected-unweighted-graph/

''' Given an undirected or bi-directional unweighted graph. The task is to find the length of the 
    shortest cycle in the given graph. If no cycle exists print -1. '''


from collections import deque


def shortest_cycle_undirected(graph, n):
    adj = {i: [] for i in range(n)}

    for u, v in graph:
        adj[u].append(v)
        adj[v].append(u)

    res = float("inf")

    for i in range(n):

        visit = set()
        distance = {i: 0 for i in range(n)}
        q = [(i)]

        while q:
            node = q.pop(0)

            for ch in adj[node]:

                if ch not in visit:
                    # same as sssp.py bfs logic
                    distance[ch] = 1 + distance[node]
                    visit.add(ch)
                    q.append(ch)

                else:
                    res = min(res, distance[node] + distance[ch] + 1)

    return res if res != float("inf") else -1


n = 7
graph = [[0, 6], [0, 5], [5, 1], [1, 6], [2, 6], [2, 3], [3, 4], [4, 1]]
print(shortest_cycle_undirected(graph, n))

# above logic falling in this test case but below one is working need to return -1 but returning 4.
print("ank", shortest_cycle_undirected(
    [[0, 1], [0, 2]], 4))

# https://leetcode.com/problems/shortest-cycle-in-a-graph/


def findShortestCycle(n, edges):

    # Creating Graph
    adj = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    res = float('inf')

    for i in range(n):
        time = [-1] * n
        time[i] = 0
        q = deque()
        q.append(i)

        while q:
            node = q.popleft()
            for child in adj[node]:
                # If we are visiting the node for the first time
                if time[child] == -1:
                    time[child] = time[node] + 1
                    q.append(child)
                # If the node v is already visited then the len of the cycle will be
                # time_in[v] + time_in[u] + 1
                elif time[child] >= time[node]:
                    res = min(res, time[child] + time[node] + 1)

    return -1 if res == float('inf') else res


print(findShortestCycle(
    7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]]))
print(findShortestCycle(4,
                        [[0, 1], [0, 2]]))
