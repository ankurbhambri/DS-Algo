# https://leetcode.com/problems/unique-binary-search-trees/


# TC: O(n^2)
# SC: O(n)
class Solution:
    def numTrees(self, n: int) -> int:

        dp = [0] * (n + 1)

        dp[0] = dp[1] = 1

        for nodes in range(2, n + 1):

            for root in range(1, nodes + 1):

                dp[nodes] += (
                    dp[root - 1] *
                    dp[nodes - root]
                )

        return dp[n]


print(Solution().numTrees(3))
print(Solution().numTrees(1))