'''
The Longest Common Substring problem is about finding the longest contiguous substring that is common between two given strings. For example:

Input:
    s1 = "ABCDGH", s2 = "ACDGHR"
Output:
    Longest Common Substring: "CDGH" (length = 4)

Note: Unlike the Longest Common Subsequence (LCS), the characters in the substring must be contiguous.

Approach: Dynamic Programming (DP)
    1. Use a 2D DP table where dp[i][j] represents the length of the longest common substring ending at s1[i-1] and s2[j-1].
    2. Transition:
        - If s1[i-1] == s2[j-1], then dp[i][j] = dp[i-1][j-1] + 1.
        - Otherwise, dp[i][j] = 0.
    3. Track the maximum length and the ending index of the longest common substring during the computation.
    4. Extract the substring using the ending index and the maximum length.

Complexity:
    - Time Complexity: O(m * n), where m and n are the lengths of the two strings.
    - Space Complexity: O(m * n) for the DP table. (Can be optimized to O(min(m, n)) using a rolling array.)

'''

def longestCommonSubstr(s1, s2, n, m): # (Strings)

    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    res = 0

    for i in range(1, n + 1):

        for j in range(1, m + 1):

            if s1[i - 1] == s2[j - 1]: # If characters match, we extend the substring, not like subsequence where we can skip characters.

                dp[i][j] = 1 + dp[i - 1][j - 1]

                res = max(res, dp[i][j])

    return res


print(longestCommonSubstr("ABC", "ACB", 3, 3))
print(longestCommonSubstr("ABCDGH", "ACDGHR", 6, 6))
print(longestCommonSubstr("BANANA", "ANANAS", 6, 6))


# Similar question - Maximum Length of Repeated Subarray 
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, nums1, nums2):

        res = 0

        m, n = len(nums1), len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if nums1[i - 1] == nums2[j - 1]:

                    dp[i][j] = 1 + dp[i - 1][j - 1]

                    res = max(res, dp[i][j])

        return res


print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3
print(Solution().findLength([0, 1, 1, 1, 1], [1, 0, 1, 0, 1]))  # 2
print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3
