# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012

def frogJump(n: int, heights: List[int]) -> int:

    dp = [0] * n
    for i in range(1,  n):
        left = dp[i - 1] + abs(heights[i] - heights[i - 1])
        right = dp[i - 2] + abs(heights[i] - heights[i - 2]) if i > 1 else float("inf")
        dp[i] = min(left, right)
    return dp[n - 1]
