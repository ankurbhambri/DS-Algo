# https://codeforces.com/contest/1324/problem/F

from sys import stdin


def solve() -> None:
  data = stdin.read().strip().split()
  it = iter(data)

  n = int(next(it))
  color = [int(next(it)) for _ in range(n)]

  graph = [[] for _ in range(n)]
  for _ in range(n - 1):
    u = int(next(it)) - 1
    v = int(next(it)) - 1
    graph[u].append(v)
    graph[v].append(u)

  # Convert colors: white(1) -> +1, black(0) -> -1
  value = [1 if c == 1 else -1 for c in color]

  # First DFS: best contribution from subtree rooted at each node.
  dp = [0] * n

  def dfs1(node: int, parent: int) -> None:

    cur = value[node]

    for nei in graph[node]:

      if nei == parent:
        continue

      dfs1(nei, node)

      cur += max(0, dp[nei])

    dp[node] = cur

  # Second DFS (rerooting): propagate parent-side contribution to children.
  ans = [0] * n

  def dfs2(node: int, parent: int) -> None:

    ans[node] = dp[node]

    for nei in graph[node]:

      if nei == parent:
        continue

      # Move root from node -> nei.
      dp[node] -= max(0, dp[nei])
      dp[nei] += max(0, dp[node])

      dfs2(nei, node)

      # Restore state after returning.
      dp[nei] -= max(0, dp[node])
      dp[node] += max(0, dp[nei])

  dfs1(0, -1)
  dfs2(0, -1)

  print(*ans)


if __name__ == "__main__":
  solve()

# Sample Input:
# 9
# 1 1 0 0 0 1 0 1 0
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 3 7
# 6 8
# 6 9