# Here's an example implementation of the shortest path in a unweighted graph using BFS in Python:

import heapq
from collections import defaultdict, deque


def shortest_path(graph, start, end):
    q = deque([start])
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    while q:
        node = q.popleft()
        if node == end:
            return distances[end]
        for neighbor in graph[node]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[node] + 1
                q.append(neighbor)
    return -1


graph = defaultdict(list)
graph[0].append(1)
graph[0].append(2)
graph[1].append(2)
graph[2].append(0)
graph[2].append(3)
graph[3].append(3)

print(shortest_path(graph, 0, 3))


# Here's an example implementation of finding connected components in a graph using BFS in Python:
from collections import defaultdict


def connected_components(graph):
    visited = set()
    components = []
    for node in graph:
        if node not in visited:
            component = []
            q = [node]
            while q:
                vertex = q.pop(0)
                if vertex not in visited:
                    visited.add(vertex)
                    component.append(vertex)
                    q.extend(
                        neighbor
                        for neighbor in graph[vertex]
                        if neighbor not in visited
                    )
            components.append(component)
    return components


graph = defaultdict(list)
graph[0].append(1)
graph[1].append(2)
graph[2].append(3)
graph[3].append(0)
graph[4].append(5)
graph[5].append(6)

print(connected_components(graph))
# Here's an example implementation of checking if a graph is bipartite using BFS in Python:

from collections import defaultdict


def is_bipartite(graph):
    colors = defaultdict(lambda: None)
    for node in graph:
        if colors[node] is None:
            colors[node] = 0
            q = [node]
            while q:
                vertex = q.pop(0)
                for neighbor in graph[vertex]:
                    if colors[neighbor] is None:
                        colors[neighbor] = 1 - colors[vertex]
                        q.append(neighbor)
                    elif colors[neighbor] == colors[vertex]:
                        return False
    return True


graph = defaultdict(list)
graph[0].append(1)
graph[0].append(3)
graph[1].append(0)
graph[1].append(2)
graph[2].append(1)
graph[3].append(0)
graph[3].append(4)
graph[4].append(3)

print(is_bipartite(graph))
# Here's an example implementation of finding the shortest transformation sequence from a start word to an end word using BFS in Python:

from collections import defaultdict, deque


def word_ladder(start, end, dictionary):
    q = deque([(start, 1)])
    visited = set()
    while q:
        word, depth = q.popleft()
        if word == end:
            return depth
        for i in range(len(word)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + j + word[i + 1 :]
                if next_word in dictionary and next_word not in visited:
                    q.append((next_word, depth + 1))
                    visited.add(next_word)
    return 0


dictionary = set(['hot', 'dot', 'dog', 'lot', 'log', 'cog'])

print(word_ladder('hit', 'cog', dictionary))
# Here's an example implementation of finding the shortest path of a knight in a chess board using BFS in Python:

from collections import deque


def shortest_path(x1, y1, x2, y2):
    q = deque([(x1, y1, 0)])
    visited = set((x1, y1))
    while q:
        x, y, depth = q.popleft()
        if x == x2 and y == y2:
            return depth
        for dx, dy in (
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ):
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                q.append((nx, ny, depth + 1))
                visited.add((nx, ny))
    return -1


print(shortest_path(0, 0, 7, 7))


# Here's an example implementation of the Word Ladder problem using BFS in Python:

from collections import deque


def word_ladder(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return 0
    q = deque([beginWord])
    visited = set([beginWord])
    distance = 1
    while q:
        size = len(q)
        for _ in range(size):
            word = q.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                for j in range(26):
                    next_word = word[:i] + chr(97 + j) + word[i + 1 :]
                    if next_word in wordList and next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)
        distance += 1
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder(beginWord, endWord, wordList))


# Here's an example implementation of the Walls and Gates problem using BFS in Python:

from collections import deque


def wallsAndGates(rooms):
    if not rooms:
        return
    m, n = len(rooms), len(rooms[0])
    q = deque([(i, j) for i in range(m) for j in range(n) if rooms[i][j] == 0])
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and rooms[nx][ny] == 2147483647:
                rooms[nx][ny] = rooms[x][y] + 1
                q.append((nx, ny))


rooms = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
wallsAndGates(rooms)
for row in rooms:
    print(row)


# Here's an example implementation of the Minimum Steps to Reach a Target Word problem using BFS in Python:

from collections import deque


def ladderLength(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return 0
    q = deque([beginWord])
    visited = set([beginWord])
    distance = 1
    while q:
        size = len(q)
        for _ in range(size):
            word = q.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                for j in range(26):
                    next_word = word[:i] + chr(97 + j) + word[i + 1 :]
                    if next_word in wordList and next_word not in visited:
                        q.append(next_word)
                        visited.add(next_word)
        distance += 1
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(ladderLength(beginWord, endWord, wordList))

# Given an undirected, weighted graph, check whether there exist more than one shortest path between a source and destination node.


def moreShortestPath(adj, src, dst):
    vis, q = [False] * len(adj), [[0, src]]
    heapq.heapify(q)
    while q:
        d, u = heapq.heappop(q)
        if u == dst:
            return [d, u] == (q and heapq.heappop(q))
        vis[u] = True
        for v, w in adj[u]:
            if not vis[v]:
                heapq.heappush(q, [w + d, v])
