# https://atcoder.jp/contests/dp/tasks/dp_l

import sys
sys.setrecursionlimit(10**7)


# top-down version - TC: O(n^2), SC: O(n^2) due to memoization, O(n) due to recursion stack

n = int(input())
a = list(map(int, input().split()))

dp = [[None] * n for _ in range(n)]

def solve(l, r):
    if l > r:
        return 0
    if dp[l][r] is not None:
        return dp[l][r]
    
    if l == r:
        dp[l][r] = a[l]
        return a[l]
    
    take_left = a[l] - solve(l+1, r)
    take_right = a[r] - solve(l, r-1)
    
    dp[l][r] = max(take_left, take_right)
    return dp[l][r]

print(solve(0, n-1))



# bottom-up version - TC: O(n^2), SC: O(n^2)

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]

# base case
for i in range(n):
    dp[i][i] = a[i]

# build for increasing length
for length in range(2, n + 1):

    for l in range(n - length + 1):

        r = l + length - 1
        
        dp[l][r] = max(
            a[l] - dp[l+1][r],
            a[r] - dp[l][r-1]
        )

print(dp[0][n-1])


# space optimized version - TC: O(n^2), SC: O(n)

'''

The time complexity is determined by the nested loops:

Outer Loop: Runs from n-1 down to 0 (n iterations).

Inner Loop: Runs from l+1 up to n (averaging n/2 iterations).

Total operations: sum(i, i=1 to n) = n(n+1)/2 ≈ n^2/2
'''


n = int(input())
a = list(map(int, input().split()))

dp = [0] * n

for l in range(n - 1, -1, -1):

    dp[l] = a[l]  # base case dp[l][l]
    
    for r in range(l + 1, n):

        dp[r] = max(
            a[l] - dp[r],     # old dp[l+1][r]
            a[r] - dp[r-1]    # current dp[l][r-1]
        )

print(dp[n-1])