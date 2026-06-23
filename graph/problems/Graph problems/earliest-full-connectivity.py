'''
Earliest Full Connectivity Timestamp

We have a log of Uber rides when passengers shared their rides together through Uber Share. The log string is sorted chronologically.

Example Log:
    1670000001 Alice shared-ride-with Bob
    1670000042 Charlie shared-ride-with Dan
    1670000450 Bob shared-ride-with Charlie
    1670000501 Alice shared-ride-with Eve
    1670000621 Bob shared-ride-with Dan

Output: 1670000501

Given this log text and a list of all possible riders, write a function that returns the earliest timestamp when all riders become connected through the car shared network. 
A rider is connected to another if they have shared a ride, or if they are connected through a chain of other riders.

'''

class UnionFind:
    def __init__(self, people):

        self.parent = {p: p for p in people}
        self.rank = {p: 0 for p in people}
        self.components = len(people)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a, b):

        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        # union by rank
        if self.rank[rootA] > self.rank[rootB]:
            self.parent[rootB] = rootA

        elif self.rank[rootA] < self.rank[rootB]:
            self.parent[rootA] = rootB

        else:
            self.parent[rootB] = rootA
            self.rank[rootA] += 1

        self.components -= 1
        return True


def earliestFullConnectivity(logs, people):

    # in this case logs are not sorted then, we need to sort them
    logs.sort(key=lambda x: x[0])

    uf = UnionFind(people)

    for timestamp, a, b in logs:

        uf.union(a, b)

        if uf.components == 1:
            return timestamp

    return -1


print(earliestFullConnectivity([
    (1670000001, "Alice", "Bob"),
    (1670000042, "Charlie", "Dan"),
    (1670000450, "Bob", "Charlie"),
    (1670000501, "Alice", "Eve"),
    (1670000621, "Bob", "Dan")
], ["Alice", "Bob", "Charlie", "Dan", "Eve"]))  # Output: 1670000501

# Follwup - 1

'''
Rider Blocking

Riders can now block each other. The log can include blocking events which break connections.

Now you would update your solution to handle these events and still determine the earliest timestamp when the network is fully connected.

Example Log with Blocking:
    1670000001 Alice shared_ride with Bob
    1670000450 Bob shared_ride with Charlie
    1670000488 Alice blocked Bob
    1670000501 Alice shared_ride with Eve
'''

from collections import defaultdict, deque

def is_connected(graph, people):

    if len(people) <= 1:
        return True

    visited = set()

    # Start BFS from any node, since we just want to check if all nodes are connected.
    # Here, set is unordered, so we can just take the first element as the starting point.
    start = next(iter(people))

    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

    return len(visited) == len(people)


def earliest_connectivity_with_block(logs, people):

    graph = defaultdict(set)

    for timestamp, a, action, b in logs:

        if action == "shared_ride":
            graph[a].add(b)
            graph[b].add(a)

        elif action == "blocked":
            graph[a].discard(b)
            graph[b].discard(a)

        if is_connected(graph, people):
            return timestamp

    return -1

print(earliest_connectivity_with_block([
    (1670000001, "Alice", "shared_ride", "Bob"),
    (1670000450, "Bob", "shared_ride", "Charlie"),
    (1670000488, "Alice", "blocked", "Bob"),
    (1670000501, "Alice", "shared_ride", "Eve")
], ["Alice", "Bob", "Charlie", "Eve"]))  # Output: -1