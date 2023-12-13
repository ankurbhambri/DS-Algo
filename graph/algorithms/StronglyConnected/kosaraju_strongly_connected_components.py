"""
Ways to find Strongly connected components in a graph

1. Brute force

    a. Find all pairs shortest path using Floyd warshall algo.
    b. Check if between any two pairs the distance is infinity
       (i.e, unreachable) except self loops.

2. Kosaraju Algorithm
    a. Perform DFS traversal of graph. Push node to stack before returning. - DFS
    b. Find the transpose graph by reversing the edges. - Reverse
    c. Pop nodes one by one from stack and again do DFS on modifies graph.(Keep popping nodes) - DFS
"""
# T.C  = 3 * (V + E) = O(V + E)


from collections import defaultdict

V = 8
adj = defaultdict(list)
rev = defaultdict(list)


def DFS1(i, visited, st):
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            DFS1(j, visited, st)

    st.append(i)


def reverse():
    for i in range(V):
        for j in adj[i]:
            rev[j].append(i)


def DFS2(i, visited):
    print(i, end=" ")
    visited[i] = True
    for j in rev[i]:
        if not visited[j]:
            DFS2(j, visited)


def findSCCs():
    stack = []

    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            DFS1(i, visited, stack)

    reverse()

    visited = [False] * V

    print("Strongly Connected Components are:")
    while stack:
        curr = stack.pop()
        if not visited[curr]:
            DFS2(curr, visited)
            print()
            visited[curr] = True


if __name__ == "__main__":
    adj[0].append(1)
    adj[1].append(2)
    adj[2].append(0)
    adj[2].append(3)
    adj[3].append(4)
    adj[4].append(5)
    adj[4].append(7)
    adj[5].append(6)
    adj[6].append(4)
    adj[6].append(7)

    findSCCs()
