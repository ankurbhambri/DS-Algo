# https://leetcode.com/problems/target-sum/

'''
Maan lo humne kuch numbers ke aage '+' lagaya aur kuch ke aage '-'.
    - Jo numbers plus wale hain, unke group ko bolte hain S1.
    - Jo numbers minus wale hain, unke group ko bolte hain S2.

Toh hum equation likh sakte hain: 
    - S1 - S2 = target, (Yeh hume chahiye)
    - S1 + S2 = totalSum, (Yeh saare elements ka sum hai)

Ab dono equations ko plus (add) kar dete hain:

- (S1 - S2) + (S1 + S2) = target + totalSum, yahan S2 cancel ho jayega aur sirf 2 * S1 = target + totalSum bachega.

- 2 * S1 = target + totalSum => (target + totalSum) // 2
'''

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        total_sum = sum(nums)

        # Edge cases check karo
        if abs(target) > total_sum or (target + total_sum) % 2 != 0:
            return 0

        # Humara naya target (S1)
        S1 = (target + total_sum) // 2

        # dp array initialize karo, dp[0] = 1 kyunki 0 sum banane ka 1 tarika hai (kuch mat uthao)
        dp = [1] + [0] * S1

        for num in nums:
            # 0-1 Knapsack ki tarah loop ulta chalega taaki same element baar-baar use na ho
            for w in range(S1, num - 1, -1):
                dp[w] += dp[w - num]

        return dp[S1]

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
print(Solution().findTargetSumWays([9, 7, 0, 3, 9, 8, 6, 5, 7, 6], 31))  # 8