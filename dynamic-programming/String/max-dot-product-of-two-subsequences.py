# https://leetcode.com/problems/max-dot-product-of-two-subsequences

class Solution:
    def maxDotProduct(self, nums1, nums2):

        n, m = len(nums1), len(nums2)
        # 2D DP Table: rows = n+1, cols = m+1
        # Shuru mein bohot choti value (negative infinity) se fill karenge
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                # Aaj ke do numbers ka product
                current_product = nums1[i-1] * nums2[j-1]

                # Chaar options mein se best pick karna:
                dp[i][j] = max(
                    current_product,                    # 1. Sirf ye dono pick karo
                    current_product + dp[i-1][j-1],     # 2. Ye dono + purana best
                    dp[i-1][j],                         # 3. nums1 ka element skip karo
                    dp[i][j-1]                          # 4. nums2 ka element skip karo
                )

        return dp[n][m]

print(Solution().maxDotProduct([2,1,-2,5], [3,0,-6]))  # Output: 18
print(Solution().maxDotProduct([-1,-1], [1,1]))      # Output: -1