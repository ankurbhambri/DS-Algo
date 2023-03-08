# memoization
def frog_k_jumps(n, heights):

  memo = [-1] * n

  def helper(i):

    if i == 0:
      return 0

    if memo[i] != -1:
      return dp[i]

    res = float("inf")

    for j in range(1, k):
      if (i - j >= 0):
        jump = helper(i - j) + abs(heights[i] + heights[i - j])
        res = = min(res, jump)
        memo[i] = res

     return memo[i]
  
  return helper(n - 1)


# tabulation
def frog_k_jumps(n, heights):

  dp = [0] * n

  for i in range(1, n):

    res = float("inf")

    for j in range(1, k):

      if (i - j >= 0):

        jump = dp[i - j] + abs(heights[i] + heights[i - j])

        res = min(res, jump)

    dp[i] = res

  return dp[n - 1]

# space optimization
# here space optimixation can only be done till k also if k == N then answer will be same as above
