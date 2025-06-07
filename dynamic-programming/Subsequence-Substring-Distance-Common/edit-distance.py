# https://leetcode.com/problems/edit-distance/description/

"""
    The problem is to determine the minimum number of operations required to convert one string (word1) into another string (word2).

    The allowed operations are:
        1. Insert a character
        2. Delete a character
        3. Replace a character

    This is a classic dynamic programming problem known as the "Edit Distance" or "Levenshtein Distance" problem.

    The approach involves using a 2D DP table where:

        - dp[i][j] represents the minimum number of operations required to convert the first i characters of word1 to the first j characters of word2.

        - If the characters at the current position are different, the value is calculated as:
            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            where:
                dp[i-1][j-1] -> Replace operation
                dp[i-1][j]   -> Delete operation
                dp[i][j-1]   -> Insert operation

        - If the characters are the same, no operation is needed, so:
            dp[i][j] = dp[i-1][j-1]

"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        M, N = len(word1), len(word2)

        # Initialize DP table
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        
        # Base cases - To convert any non-empty string to an empty string: We must delete all characters or insert all characters.

        '''
            dp[1][0] = 1   # delete 1 char
            dp[2][0] = 2   # delete 2 chars
            .............. and so on
            dp[i][0] = i   # delete i chars
            
            Either:
                Case 1: dp[i][0] — Convert the first i characters of word1 to an empty string "" (word2). We must delete all characters. Here, we are deleting because we are converting word1 to word2, so if word2 is empty, we need to empty word1 as well.
                OR
                Case 2: dp[0][j] — Convert an empty string "" (word1) to the first j characters of word2. We must insert all characters. Here, if word1 is empty and we want to convert it to word2, then we need to insert all characters of word2 into word1.

                ''  a   b   c
            ''  0   1   2   3
            a   1
            b   2
            c   3

        '''

        for i in range(M + 1):
            dp[i][0] = i  # delete all characters from word1 to convert to empty string

        for j in range(N + 1):
            dp[0][j] = j  # insert all characters to word1 to convert to word2

        # Fill DP table
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if word1[i - 1] == word2[j - 1]:
                    # No operation needed if characters match
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Choose min of insert, delete, or replace
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],    # delete
                        dp[i][j - 1],    # insert
                        dp[i - 1][j - 1] # replace
                    )
        
        return dp[M][N]


print(Solution().minDistance("horse", "ros"))  # Output: 3
print(Solution().minDistance("intention", "execution"))  # Output: 5
print(Solution().minDistance("kitten", "sitting"))  # Output: 3
print(Solution().minDistance("flaw", "lawn"))  # Output: 2
