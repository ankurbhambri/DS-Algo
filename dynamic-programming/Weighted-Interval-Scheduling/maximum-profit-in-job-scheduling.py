# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution:
    def jobScheduling(self, start_time, end_time, profit) -> int:

        arr = sorted(zip(start_time, end_time, profit), key=lambda x: x[1])
        n = len(arr)

        starts = [s[0] for s in arr]
        ends = [s[1] for s in arr]
        profit = [s[2] for s in arr]

        dp = [0] * n
        dp[0] = profit[0]

        def bs_right(x):

            """Find the index of the rightmost value less than or equal to x."""
            lo, hi = 0, len(ends)

            while lo < hi:
                mid = (lo + hi) // 2
                if ends[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid

            return lo

        for i in range(1, n):
            # last show that ends before arr[i] starts
            j = bs_right(starts[i]) - 1

            include = profit[i] + (dp[j] if j != -1 else 0)
            exclude = dp[i - 1]

            dp[i] = max(include, exclude)

        return dp[n - 1]


print(Solution().jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # Output: 120
print(Solution().jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))  # Output: 150 
