# https://leetcode.com/discuss/post/6644271/amazon-sde2-oa-by-anonymous_user-8402/

'''
A Company is planning to make a movie theatre. Shows will have start time , end time and number of person in the theatre between start time and end time. 
An array is given for all the three start_time[], end_time[], people_count[]. Return the maximum sum of people from non overlapping shows.

You are given:

    start_time[i]: Start time of the i-th show.

    end_time[i]: End time of the i-th show.

    people_count[i]: Number of people attending the i-th show.

You need to select a subset of non-overlapping shows such that the sum of people_count is maximized.

'''

def max_people_non_overlapping(start_time, end_time, people_count):

    # sort intervals by end_time
    shows = sorted(zip(start_time, end_time, people_count), key=lambda x: x[1])
    n = len(shows)

    starts = [s[0] for s in shows]
    ends = [s[1] for s in shows]
    people = [s[2] for s in shows]

    dp = [0] * n
    dp[0] = people[0]

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
        # last show that ends before shows[i] starts
        j = bs_right(starts[i]) - 1

        include = people[i] + (dp[j] if j != -1 else 0)
        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    return dp[-1]


print(max_people_non_overlapping([1, 3, 5], [2, 4, 6], [3, 5, 7]))  # Output: 15


# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
def jobScheduling(start_time, end_time, profit):

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

        # dp[j] means the maximum profit we can get from the jth job whoose end time is less than or equal to the start time of the current ith job, only if j is not -1
        include = profit[i] + (dp[j] if j != -1 else 0)
        exclude = dp[i - 1]

        dp[i] = max(include, exclude)

    return dp[-1]



print(jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # Output: 120
print(jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))  # Output: 150


# https://leetcode.com/problems/maximum-earnings-from-taxi/description/
def maxTaxiEarnings(n, rides):

    arr = sorted(rides, key=lambda x: x[1])
    n = len(arr)

    starts = [s[0] for s in arr]
    ends = [s[1] for s in arr]
    profit = [s[1] - s[0] + s[2] for s in arr] # profit = (endi - starti + tipi)

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

    return dp[-1]    

# https://leetcode.com/problems/two-best-non-overlapping-events/description/

# No need for DP or BST.
def maxTwoEvents(events):

    proc = []
    ans = max_val = 0

    for s, e, v in events:
        proc.append((s, 1, v))     # time, is_start, val
        proc.append((e + 1, 0, v))  # use e + 1 (inclusive)

    proc.sort()
    
    for time, is_start, val in proc:

        if is_start:
            ans = max(ans, max_val + val)
        else:
            max_val = max(max_val, val)

    return ans
