'''
  The Levenshtein Distance
  aproach   a b
            c min(a, b, c) + 1
 '''

class Solution:
    def minDistance(self, a: str, b: str) -> int:
        
        M, N = len(a), len(b)

        dp = [[0] * (N + 1) for _ in range (M + 1)]
        
        for r in range(1, M + 1):
            dp[r][0] = r

        for c in range(1, N + 1):
            dp[0][c] = c
            

        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if a[i - 1] != b[j - 1]:
                    dp[i][j] = 1 + min(min(dp[i - 1][j - 1], dp[i - 1][j]), dp[i][j - 1])
                else:
                    dp[i][j] = dp[i - 1][j - 1]
        
        return dp[M][N]
  


