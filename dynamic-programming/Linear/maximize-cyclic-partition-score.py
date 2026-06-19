# https://leetcode.com/problems/maximize-cyclic-partition-score/

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:

        # 3573. Best Time to Buy and Sell Stock V
        def maximumProfit(prices, k):

            sold = [0] * k
            res = [0] * (k + 1)
            bought = [float("-inf")] * k

            for price in prices:

                for j in range(k, 0, -1):

                    res[j] = max(res[j], bought[j - 1] + price, sold[j - 1] - price)

                    bought[j - 1] = max(bought[j - 1], res[j - 1] - price)

                    sold[j - 1] = max(sold[j - 1], res[j - 1] + price)

            return max(res)

        max_i = nums.index(max(nums))

        ans1 = maximumProfit(nums[max_i:] + nums[:max_i], k)  # nums[max_i] is the first element.

        ans2 = maximumProfit(nums[max_i + 1:] + nums[:max_i + 1], k)  # nums[max_i] is the last element.

        return max(ans1, ans2)


print(Solution().maximumScore([1, 2, 3, 4, 5], 1))  # 4
print(Solution().maximumScore([5, 4, 3, 2, 1], 1))  # 4
print(Solution().maximumScore([1, 2, 3, 4, 5], 2))  # 4