from collections import deque

# https://leetcode.com/problems/alien-dictionary/
# https://www.geeksforgeeks.org/alien-dictionary/
# Similar question - https://leetcode.com/discuss/interview-question/4370961/google-interview-question/2404127



def alienOrder(words):

    adj = {c: set() for w in words for c in w}

    for i in range(len(words) - 1):
        
        w1, w2 = words[i], words[i + 1]
        minlen = min(len(w1), len(w2))
        
        # invalid case, e.g. ["abc", "ab"]
        if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
            return ""

        for j in range(minlen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visit = {}
    res = []

    def dfs(c):

        if c in visit:
            return visit[c]

        visit[c] = True

        for nei in adj[c]:
            if dfs(nei):
                return True

        visit[c] = False
        res.append(c)

    for c in adj:
        if dfs(c):
            return ""

    res.reverse()
    return "".join(res)


print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))


# using Khan's algo
def alienOrder(words):

    # Step 1: Create adjacency list and in-degree map
    adj = {c: set() for w in words for c in w}
    indegree = {c: 0 for w in words for c in w}

    # Step 2: Build the graph
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_length = min(len(w1), len(w2))
        
        # If word1 is a prefix of word2 but longer, it's an invalid order
        if w1[:min_length] == w2[:min_length] and len(w1) > len(w2):
            return ""

        for j in range(min_length):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                indegree[w2[j]] += 1
                break  # Stop after finding the first difference

    # Step 3: Topological Sort using BFS (Kahn’s Algorithm)
    queue = deque([c for c in indegree if indegree[c] == 0])  # Nodes with in-degree 0
    result = []

    while queue:
        char = queue.popleft()
        result.append(char)
        for neighbor in adj[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: If cycle detected (not all nodes processed), return ""
    if len(result) < len(indegree):
        return ""

    return "".join(result)

print(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
