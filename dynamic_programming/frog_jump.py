# https://www.codingninjas.com/codestudio/problems/frog-jump_3621012

# Top down (Memoization)

def frogJump(n: int, heights: List[int]) -> int:
    
    memo = [-1] * n
    
    def helper(i):

        if i == 0:
            return 0
        
        if dp[i] != -1:
            return dp[i]
        
        left = helper(i - 1) + abs(heights[i] - heights[i - 1])

        right = helper(i - 2) + abs(heights[i] - heights[i - 2]) if i > 1 else float("inf")

        memo[i] = min(left, right)

        return memo[i]
    
    return helper(n - 1)


# Bottom up (Tabulation)
def frogJump(n: int, heights: List[int]) -> int:

    dp = [0] * n
    for i in range(1,  n):
        left = dp[i - 1] + abs(heights[i] - heights[i - 1])
        right = dp[i - 2] + abs(heights[i] - heights[i - 2]) if i > 1 else float("inf")
        dp[i] = min(left, right)
    return dp[n - 1]


# Space optimized way
def frogJump(n: int, heights: List[int]) -> int:
    
    a = b = 0
    for i in range(1,  n):
        left = b + abs(heights[i] - heights[i - 1])
        right = a + abs(heights[i] - heights[i - 2]) if i > 1 else float("inf")
        a, b = b, min(left, right)
    return b
