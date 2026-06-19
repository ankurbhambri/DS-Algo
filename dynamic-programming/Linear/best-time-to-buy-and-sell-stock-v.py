# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/


# TC: O(n * k)
# SC: O(k)
class Solution:
    def maximumProfit(self, nums: list[int], k: int) -> int:

        sold = [0] * k
        res = [0] * (k + 1)
        bought = [float("-inf")] * k

        for num in nums:

            for j in range(k, 0, -1):

                res[j] = max(res[j], bought[j - 1] + num, sold[j - 1] - num)

                bought[j - 1] = max(bought[j - 1], res[j - 1] - num)

                sold[j - 1] = max(sold[j - 1], res[j - 1] + num)

        return max(res)


print(Solution().maximumProfit([1, 2, 3, 4, 5], 2))  # 4
print(Solution().maximumProfit([3, 2, 6, 5, 0, 3], 2))  # 7
