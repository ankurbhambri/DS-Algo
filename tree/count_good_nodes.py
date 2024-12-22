# https://leetcode.com/problems/count-the-number-of-good-nodes/

from collections import defaultdict


def countGoodNodes(edges):

    n = len(edges) + 1
    adj = defaultdict(list)

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    subtree_size = [0] * n
    visit = set()

    def dfs(node):

        visit.add(node)
        sm = 1

        for nei in adj[node]:
            if nei not in visit:
                sm += dfs(nei)
        subtree_size[node] = sm

        return sm

    dfs(0)

    good_nodes = 0

    for node in range(n):

        child_sizes = []

        for child in adj[node]:

            # Ensure not to count the parent as a child
            if subtree_size[child] < subtree_size[node]:
                child_sizes.append(subtree_size[child])

        # that means all child subtree sizes are equal
        if len(set(child_sizes)) <= 1:
            good_nodes += 1

    return good_nodes


print(countGoodNodes([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]))
