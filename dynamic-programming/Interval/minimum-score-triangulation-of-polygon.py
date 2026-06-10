# https://leetcode.com/problems/minimum-score-triangulation-of-polygon


# similar to https://leetcode.com/problems/burst-balloons

# TC: O(n^3)
# SC: O(n^2)
class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:

        n = len(values)

        dp = [[0] * n for _ in range(n)]

        # length = number of vertices in current interval
        # 3 vertices => one triangle (base case cost = product)
        for length in range(3, n + 1):

            # starting vertex
            for i in range(n - length + 1):

                # ending vertex
                j = i + length - 1

                dp[i][j] = float("inf")

                # choose k as the third vertex of triangle (i, k, j)
                # k must lie strictly between i and j
                for k in range(i + 1, j):

                    # triangle (i, k, j) splits polygon into:
                    # 1. vertices i..k
                    # 2. vertices k..j
                    #
                    # total cost =
                    # left polygon cost
                    # + right polygon cost
                    # + current triangle cost

                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + (values[i] * values[k] * values[j]))

        # answer for whole polygon
        return dp[0][n-1]


print(Solution().minScoreTriangulation([1, 2, 3]))  # Output: 6 (one triangle with vertices 1, 2, 3)
print(Solution().minScoreTriangulation([3, 7, 4, 5]))  # Output: 144 (triangles (3, 7, 4) and (3, 4, 5))