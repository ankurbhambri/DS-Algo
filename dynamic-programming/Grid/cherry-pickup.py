from functools import lru_cache


# https://leetcode.com/problems/cherry-pickup

class Solution:
    def cherryPickup(self, grid):

        n = len(grid)
        memo = {}

        def dfs(r1, c1, r2):

            # Steps = r1 + c1 = r2 + c2
            # yha pe, c2 ko calculate kar rahe hain using the relationship between the positions of the two persons. 
            # Since both persons take the same number of steps (r1 + c1 for person 1 and r2 + c2 for person 2), we can derive c2 from the equation:
            # Because this algebraic equation is always true, we can rearrange it to isolate c2: c2 = r1 + c1 - r2
            c2 = r1 + c1 - r2

            # out of bounds
            if (
                r1 >= n or c1 >= n or
                r2 >= n or c2 >= n or 
                grid[r1][c1] == -1 or
                grid[r2][c2] == -1
            ):
                return float("-inf")


            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]

            # reached end
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            cherries = grid[r1][c1]

            if (r1, c1) != (r2, c2):
                cherries += grid[r2][c2]

            # Explore all 4 possible combinations of next moves:
            # 1. Person 1 Right, Person 2 Right
            # 2. Person 1 Right, Person 2 Down
            # 3. Person 1 Down,  Person 2 Right
            # 4. Person 1 Down,  Person 2 Down
            best = max(
                dfs(r1 + 1, c1, r2 + 1),  # D,D
                dfs(r1 + 1, c1, r2),      # D,R
                dfs(r1, c1 + 1, r2 + 1),  # R,D
                dfs(r1, c1 + 1, r2)       # R,R
            )

            memo[(r1, c1, r2)] = cherries + best

            return memo[(r1, c1, r2)]

        return max(0, dfs(0, 0, 0))


print(Solution().cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(Solution().cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 0, 2], [1, 0, 0, 0, 0, 0, 1]]))


# https://leetcode.com/problems/cherry-pickup-ii

class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:

        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(r, c1, c2):

            if r == m:
                return 0

            # agar dono robot same cell pe hain toh ek hi baar cherry count karni hai
            cherries = grid[r][c1] if c1 == c2 else grid[r][c1] + grid[r][c2]

            ans = 0

            for nc1 in range(c1 - 1, c1 + 2):

                for nc2 in range(c2 - 1, c2 + 2):

                    if 0 <= nc1 < n and 0 <= nc2 < n:
                        ans = max(ans, dfs(r + 1, nc1, nc2))

            return ans + cherries

        return dfs(0, 0, n - 1)


print(Solution().cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))
print(Solution().cherryPickup([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 0, 2], [1, 0, 0, 0, 0, 0, 1]]))