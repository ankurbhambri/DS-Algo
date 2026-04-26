# https://leetcode.com/problems/detect-cycles-in-2d-grid


# TC: O(m * n), SC: O(m * n)
class Solution:
    def containsCycle(self, grid):

        seen = set()
        m, n = len(grid), len(grid[0])

        dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        def helper(r, c, pr, pc):

            seen.add((r, c))

            for dr, dc in dirs:

                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if grid[nr][nc] != grid[r][c]:
                    continue

                if (nr, nc) != (pr, pc): # should not equal to immediate parent

                    # here, (i, j) not in seen used to detect cycle
                    if (nr, nc) in seen or helper(nr, nc, r, c):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and helper(i, j, -1, -1):
                    return True

        return False


print(Solution().containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))
print(Solution().containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]))