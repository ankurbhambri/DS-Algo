# https://leetcode.com/problems/paint-fence


class Solution:
    def numWays(self, n: int, k: int) -> int:

        if n == 1:
            return k

        a = k
        b = k * k

        for _ in range(3, n + 1):
            a, b = b, (k - 1) * (a + b)

        return b


print(Solution().numWays(1, 1)) # 1
print(Solution().numWays(3, 2)) # 6