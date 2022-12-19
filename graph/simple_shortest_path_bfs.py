def shortest_path(arr):
    adj = defaultdict(list)
    for u, v in arr:
        adj[u].append(v)
    visit = set()
    q = ["A"]
    depth = 1
    while q:
        for i in range(len(q)):
            node = q.pop(0)
            if node == "E":
                return depth
            for ch in adj[node]:
                if ch not in visit:
                    visit.add(ch)
                    q.append(ch)
        depth += 1
    return 0

arr = [["A", "B"], ["B", "E"], ["A", "C"], ["C", "D"], ["D", "E"]]
arr2 = [["A", "B"], ["B", "G"], ["A", "C"], ["C", "D"], ["D", "E"], ["G", "F"], ["F", "E"]]

print(shortest_path(arr))
print(shortest_path(arr2))
