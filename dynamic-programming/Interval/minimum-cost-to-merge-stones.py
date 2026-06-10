# https://leetcode.com/problems/minimum-cost-to-merge-stones/

# TC: O(n^3 / k)
# SC: O(n^2)
class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:

        n = len(stones)

        # 1. Check agar merge karna possible bhi hai ya nahi
        if (n - 1) % (k - 1) != 0:
            return -1

        # 2. Correct Prefix Sum implementation
        ps = [0] * (n + 1)

        for i in range(n):
            ps[i + 1] = ps[i] + stones[i]

        # 3. DP Table initialized with 0
        dp = [[0] * n for _ in range(n)]

        # length 2 se lekar n tak chalegi
        for length in range(k, n + 1):

            for l in range(n - length + 1):

                r = l + length - 1

                dp[l][r] = float("inf")

                # 'k' variable ka collision avoid karne ke liye 'mid' use kiya
                # mid ko (k - 1) ke steps se badhayenge taaki valid splits milein
                for mid in range(l, r, k - 1):
                    dp[l][r] = min(dp[l][r], dp[l][mid] + dp[mid + 1][r])

                # Agar ye range perfectly merge ho sakti hai ek single pile mein
                if (r - l) % (k - 1) == 0:
                    dp[l][r] += ps[r + 1] - ps[l]

        # 0-indexed array ke liye poori range 0 se n-1 hogi
        return dp[0][n - 1]