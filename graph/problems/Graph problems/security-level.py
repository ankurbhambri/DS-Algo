'''
You are given a directed graph where each edge has a security level.
For any path from startNode to endNode, the security level of the path is:

max(edge security levels in that path)
Find the path from startNode to endNode whose security level is minimized.
'''

from heapq import heappush, heappop

# Dijkstra
def minSecurityPath(n, edges, start, end):

    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((v, w))

    INF = float('inf')
    dist = [INF] * n

    dist[start] = 0

    pq = [(0, start)]  # (security_level, node)

    while pq:

        curr_sec, u = heappop(pq)

        if curr_sec > dist[u]:
            continue

        if u == end:
            return curr_sec

        for v, w in graph[u]:

            new_sec = max(curr_sec, w)

            if new_sec < dist[v]:
                dist[v] = new_sec
                heappush(pq, (new_sec, v))

    return -1