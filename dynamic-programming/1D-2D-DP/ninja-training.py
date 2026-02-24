# https://www.naukri.com/code360/problems/ninja-s-training_3621003

# Memoization
def ninjaTraining(n: int, points) -> int:

    memo = [[-1 for j in range(4)] for i in range(n)]

    def helper(day, last):

        if memo[day][last] != -1:
            return memo[day][last]

        if day == 0:
            maxi = 0
            for i in range(3):
                if i != last:
                    maxi = max(maxi, points[0][i])

            memo[day][last] = maxi
            return memo[day][last]

        res = 0
        for j in range(3):
            if j != last:
                activity = points[day][j] + helper(day - 1, j)
                res = max(res, activity)

        memo[day][last] = res
        return memo[day][last]

    return helper(n - 1, 3)


# Tabulation
def ninjaTraining(n: int, points) -> int:
    dp = [[0 for j in range(4)] for i in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        for last in range(4):
            for task in range(3):
                if task != last:
                    activity = points[day][task] + dp[day - 1][task]
                    dp[day][last] = max(dp[day][last], activity)

    return dp[n - 1][3]


# Space optimization
def ninjaTraining(n: int, points) -> int:
    prev = [0] * 4

    prev[0] = max(points[0][1], points[0][2])
    prev[1] = max(points[0][0], points[0][2])
    prev[2] = max(points[0][0], points[0][1])
    prev[3] = max(points[0][0], points[0][1], points[0][2])

    for day in range(1, n):
        curr = [0] * 4
        for last in range(4):
            curr[last] = 0
            for task in range(3):
                if task != last:
                    curr[last] = max(curr[last], points[day][task] + prev[task])
        prev = curr

    return prev[3]
