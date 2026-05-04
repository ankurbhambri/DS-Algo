# https://www.naukri.com/code360/problems/ninja-s-training_3621003


# Space optimization
def ninjaTraining(n: int, points) -> int:

    dp = [0, 0, 0, 0]

    for i in range(n):

        a, b, c = points[i]

        dp0 = a + max(dp[1], dp[2], dp[3])
        dp1 = b + max(dp[0], dp[2], dp[3])
        dp2 = c + max(dp[0], dp[1], dp[3])
        dp3 = max(dp[0], dp[1], dp[2])

        dp = [dp0, dp1, dp2, dp3]
    
    return max(dp)