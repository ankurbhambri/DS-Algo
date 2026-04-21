# https://leetcode.com/problems/partition-array-for-maximum-sum/description/


# recursion + memoization

# TC: O(n * k), SC: O(n)
class Solution:
    def maxSumAfterPartitioning(self, arr, k):

        n = len(arr)
        dp = [-1] * len(arr)

        def helper(start):

            if start >= n:
                return 0

            if dp[start] != -1:
                return dp[start]
            
            cur_max = res = 0
            end = min(start + k, n)

            for i in range(start, end):

                cur_max = max(cur_max, arr[i])

                res = max(res, cur_max * (i - start + 1) + helper(i + 1))

            dp[start] = res

            return dp[start]

        return helper(0)

print(Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)) # 84
print(Solution().maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], 4)) # 83


# Bottom up - Tabulation
# TC: O(n * k), SC: O(n)
class Solution:
    def maxSumAfterPartitioning(self, arr, k):

        n = len(arr)

        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            curr_max = 0

            for j in range(1, min(k, i) + 1):

                # finding the max element in the current subarray of length j
                curr_max = max(curr_max, arr[i - j])
                # Here, curr_max of that subarray of length j and dp[i - j] is the max sum for the remaining array after that subarray
                dp[i] = max(dp[i],  curr_max * j + dp[i - j])

        return dp[n]


print(Solution().maxSumAfterPartitioning([1,15,7,9,2,5,10], 3)) # 84
print(Solution().maxSumAfterPartitioning([1,4,1,5,7,3,6,1,9,9,3], 4)) # 83