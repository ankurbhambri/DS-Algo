# https://leetcode.com/problems/maximum-profit-in-job-scheduling/


# Recursive solution with memoization
# TC: O(2^n) in the worst case due to the recursive calls, but memoization reduces it to O(n^2) in practice
def solution(jobs):
    memo = {}
    def helper(idx, current_time):
        if idx >= len(jobs):
            return 0
        if (idx, current_time) in memo:
            return memo[(idx, current_time)]
        
        # Skip the current job
        skip_profit = helper(idx + 1, current_time)
        
        # Take the current job if it starts after the current time
        take_profit = 0
        if jobs[idx][0] >= current_time:
            take_profit = jobs[idx][2] + helper(idx + 1, jobs[idx][1])
        
        memo[(idx, current_time)] = max(skip_profit, take_profit)
        return memo[(idx, current_time)]
    return helper(0, 0)


# TC: O(n^2) due to the nested loop in the DP solution
def dp_solution(jobs):
    # Sort jobs by end time
    jobs.sort(key=lambda x: x[1])

    n = len(jobs)
    dp = [0] * n

    for i in range(n):
        dp[i] = jobs[i][2]  # Profit of the current job
        for j in range(i):
            if jobs[j][1] <= jobs[i][0]:  # If job j ends before job i starts
                dp[i] = max(dp[i], dp[j] + jobs[i][2])
    
    return max(dp) if dp else 0


class Solution:
    def jobScheduling(self, start_time, end_time, profit) -> int:

        arr = sorted(zip(start_time, end_time, profit), key=lambda x: x[1])
        n = len(arr)

        starts = [s[0] for s in arr]
        ends = [s[1] for s in arr]
        profit = [s[2] for s in arr]

        dp = [0] * n
        dp[0] = profit[0]

        # @lru_cache(None)  # Python's built-in memoization
        # def helper(idx):

        #     # Base Case: Out of jobs to consider
        #     if idx >= n:
        #         return 0

        #     # Choice 1: Skip the current job
        #     skip_profit = helper(idx + 1)

        #     # Choice 2: Take the current job
        #     # We need to find the NEXT job that starts AFTER this one ends
        #     current_end_time = jobs[idx][1]

        #     # bisect_left finds the first index where start_time >= current_end_time
        #     next_valid_idx = bisect.bisect_left(start_times, current_end_time)

        #     take_profit = jobs[idx][2] + helper(next_valid_idx)

        #     return max(skip_profit, take_profit)

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

            # last show that ends before arr[i] starts, means hum aage ja ke dekh rhe h ji past mein kaun ka isse pehle ye equal pe end hua h, uska undex le ke profit add karlo current profit mein,
            # else skip the current job and uska prevoius profit le lo, dono mein se max le lo
            j = bs_right(starts[i]) - 1

            include = profit[i] + (dp[j] if j != -1 else 0)
            exclude = dp[i - 1]

            dp[i] = max(include, exclude)

        return dp[n - 1]


print(Solution().jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # Output: 120
print(Solution().jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))  # Output: 150 
