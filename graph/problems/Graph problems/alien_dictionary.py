def alienOrder(words):

    adj = {c: set() for w in words for c in w}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minlen = min(len(w1), len(w2))
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
    
    adj = {c: set() for w in words for c in w}
    indegree = {c: 0 for w in words for c in w}
    
    for i in range(1, len(words)):
        w1, w2 = words[i - 1], words[i]
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                indegree[w2[j]] += 1
                break
     
    print(adj, indegree)     
    q = [k for k, v in indegree.items() if v == 0]
    res = []
    while q:
        node = q.pop(0)
        res.append(node)
        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    return res


# Similar question - https://leetcode.com/discuss/interview-question/4370961/google-interview-question/2404127
