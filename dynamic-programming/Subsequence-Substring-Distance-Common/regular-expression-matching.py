# https://leetcode.com/problems/regular-expression-matching/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True # Empty string aur empty pattern match hote hain

        # Base Case: Pattern like a*, a*b* can match empty string
        for j in range(2, n + 1):
            if p[j-1] == '*':
                # Agar '*' hai, toh 2 kadam peeche wala result uthao
                dp[0][j] = dp[0][j-2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: Simple Match ya '.'
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1] # Diagonal (Piche ka result)
                
                # Case 2: Asterisk '*'
                elif p[j-1] == '*':
                    # Pehle hamesha skip karne ki koshish karo (2 steps left)
                    dp[i][j] = dp[i][j-2]
                    
                    # Agar pichla character match ho raha hai, toh consume karo (1 step up)
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                        
        return dp[m][n]


print(Solution().isMatch("aab", "c*a*b"))  # True
print(Solution().isMatch("mississippi", "mis*is*p*."))  # False