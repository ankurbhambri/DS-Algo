# https://leetcode.com/problems/maximize-cyclic-partition-score/

fmax = lambda a, b: b if b > a else a

class Solution:
    # 3573. Best Time to Buy and Sell Stock V
    def maximumProfit(self, prices, k: int) -> int:

        f = [[-float('inf')] * 3 for _ in range(k + 2)]

        for j in range(1, k + 2):
            f[j][0] = 0

        for p in prices:

            for j in range(k + 1, 0, -1):

                f[j][0] = fmax(f[j][0], fmax(f[j][1] + p, f[j][2] - p))

                f[j][1] = fmax(f[j][1], f[j - 1][0] - p)

                f[j][2] = fmax(f[j][2], f[j - 1][0] + p)

        return f[-1][0]

    def maximumScore(self, nums, k: int) -> int:

        max_i = nums.index(max(nums))

        ans1 = self.maximumProfit(nums[max_i:] + nums[:max_i], k)  # nums[max_i] is the first element.

        ans2 = self.maximumProfit(nums[max_i + 1:] + nums[:max_i + 1], k)  # nums[max_i] is the last element.

        return fmax(ans1, ans2)


print(Solution().maximumScore([1, 2, 3, 4, 5], 1))  # 4
print(Solution().maximumScore([5, 4, 3, 2, 1], 1))  # 4
print(Solution().maximumScore([1, 2, 3, 4, 5], 2))  # 4