# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

def makeConnected(n, connections):

    if len(connections) < n - 1:
        return -1

    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    redundant = 0
    for a, b in connections:
        parent[find(a)] = find(b)            

    components = len(set(find(i) for i in range(n)))

    return components - 1

print(makeConnected(4, [[0, 1], [0, 2], [1, 2]]))  # Output: 1
print(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]))  # Output: -1
print(makeConnected(5, [[0, 1], [0, 2], [0, 3], [1, 2]]))  # Output: 1
print(makeConnected(4, [[0, 1], [0, 2], [1, 2]]))  # Output: 1
