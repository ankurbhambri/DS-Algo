# https://cses.fi/problemset/task/1130/

# Greedy solution to find maximum matching in a tree

'''
Greedy ka logic yeh hai: Hamesha "Leaf Nodes" (neeche wale nodes) se shuru karo.

Agar ek node leaf hai (uska sirf ek hi neighbor hai), toh uske paas matching banane ka sirf ek hi chance hai—apne parent ke saath. 
Agar hum niche se matching karte hue upar jayenge, toh hum maximum edges cover kar paayenge.

'''


import sys

# Recursion limit
sys.setrecursionlimit(300000)

# TC: O(n)
# SC: O(n) for recursion stack and adjacency list
def find_max_matching(adj, n):

    used = [False] * (n + 1)
    matching_count = 0

    def dfs(u, p):

        nonlocal matching_count

        for v in adj[u]:

            if v != p:

                dfs(v, u)

                # Agar child (v) aur parent (u) dono khali hain
                if not used[v] and not used[u]:
                    used[v] = True
                    used[u] = True
                    matching_count += 1

    # Node 1 se start karte hain (root)
    dfs(1, 0)
    return matching_count


# --- EXAMPLE TEST CASE ---
# Maan lijiye tree aisa dikhta hai:
#      1
#     / \
#    2   3
#       / \
#      4   5

n = 5
edges = [(1, 2), (1, 3), (3, 4), (3, 5)]

# Adjacency list banana
adj = [[] for _ in range(n + 1)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

result = find_max_matching(adj, n)
print(f"Maximum Matching: {result}")