# https://leetcode.com/problems/target-sum/

'''

p1 partition of +ve numbers
p2 partition fd -ve numbers

conditions: 1) p1 - p2 = target
            2) p1 + p2 = sum(arr)

equation:

    let p1 = X

    p2 = sum(arr) - x -------------- wrt p1 + p2 = sum(arr)

    put val in this eq

    p1 - p2 = target

    x - sum(arr) + x = target

    x = (sum(arr) + target) // 2  ------------- final eq will use in problem

x tends to p1 so we have to find number of x we can generate using p1 and 
this problem converts into Subset Sum Problem bcoz p1 is whole array and x is sum which
we have to find nos of times x can be genrated

'''


class Solution:
    def findTargetSumWays(self, nums, target):

        sm = sum(nums)
        mod = 10 ** 9 + 7

        if (sm + target) % 2 != 0 or abs(target) > abs(sm):
            return 0

        t = (sm + target) // 2

        dp = [0] * (t + 1)
        dp[0] = 1

        for n in nums:
            for j in range(t, n - 1, -1):
                dp[j] = (dp[j] + dp[j - n]) % mod

        return dp[t] % mod


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
print(Solution().findTargetSumWays([9, 7, 0, 3, 9, 8, 6, 5, 7, 6], 31))  # 8