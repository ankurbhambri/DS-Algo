# https://leetcode.com/problems/last-stone-weight-ii


# TC: O(n * target) where n is the number of stones and target is half of the total sum of stones
# SC: O(target) for the dp array
class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:

        total_sum = sum(stones)
        target = total_sum // 2

        # dp[w] batayega ki kya 'w' weight banana possible hai ya nahi
        dp = [True] + [False] * target

        # Har stone ke liye check karo
        for stone in stones:
            # Ulta loop chalayenge taaki same stone baar-baar use na ho (0-1 Knapsack rule)
            for w in range(target, stone - 1, -1):
                dp[w] = dp[w] or dp[w - stone]

        # Target se piche aate hue pehla 'True' dhoondho (sabse bada possible sum jo target ke paas ho)
        for s1 in range(target, -1, -1):
            if dp[s1]:
                return total_sum - 2 * s1

        return 0

print(Solution().lastStoneWeightII([1, 2, 3]))  # Output: 0
print(Solution().lastStoneWeightII([1, 2, 7]))  # Output: 4