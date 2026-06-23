# https://leetcode.com/problems/minimum-cost-to-split-an-array/

# Similar concept to palindrome-partitioning-ii

# TC: O(n^2) for trimmed matrix + O(n^2) for recursion + memoization = O(n^2)
# SC: O(n^2) for trimmed matrix + O(n) for recursion stack + O(n) for memoization = O(n^2)
class Solution:
    def minCost(self, nums: list[int], k: int) -> int:

        memo = {}

        n = len(nums)

        # 1. Trimmed matrix ko sahi se calculate karna
        trimmed = [[0] * n for _ in range(n)]

        for i in range(n):

            c = 0
            mp = {}  # Har naye 'i' ke liye fresh frequency map

            for j in range(i, n):  # 'j' hamesha 'i' se start hoga

                val = nums[j]

                mp[val] = mp.get(val, 0) + 1

                if mp[val] == 2:
                    c += 2  # Doosri baar aane par dono count honge, jab count 1 tha uska to ignore jo gaya vo num.

                elif mp[val] > 2:
                    c += 1  # Do se zyada baar aane par sirf naya element count hoga, normal ho jayeag count increment by 1

                # Agar mp[val] == 1 hai, toh 'c' mein kuch add nahi hoga (unique element)
                trimmed[i][j] = c

        # 2. Helper function (Recursion + Memoization)
        # similar to palindrome partitioning-II, yaha bhi hum i se start karke har j ke liye cut maar ke dekhenge
        def helper(start):

            if start == n:
                return 0

            if start in memo:
                return memo[start]

            res = float("inf")
            for end in range(start, n):

                curr = k + trimmed[start][end]

                nextMin = helper(end + 1)

                res = min(res, curr + nextMin)

            memo[start] = res
            return res

        return helper(0)


print(Solution().minCost([1, 2, 1, 2, 1], 2))  # Output: 8
print(Solution().minCost([1, 2, 1, 2, 1], 5))  # Output: 6


# Bottom UP
# TC: O(n^2)
# SC: O(n)
class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # dp[i] store karega index i-1 tak ki minimum cost
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: empty array ki cost 0

        for i in range(1, n + 1):

            counts = {}
            trimmed_val = 0
            
            # Piche ki taraf jaakar saare possible splits check karenge
            for j in range(i):

                num = nums[j - 1]

                counts[num] = counts.get(num, 0) + 1
                
                # Agar element doosri baar aaya, toh dono counts add honge (+2)
                if counts[num] == 2:
                    trimmed_val += 2

                # Agar 2 se zyada baar aaya, toh sirf naya count add hoga (+1)
                elif counts[num] > 2:
                    trimmed_val += 1
                
                # Minimum cost update karein
                dp[i] = min(dp[i], dp[j - 1] + k + trimmed_val)
                
        return dp[n]