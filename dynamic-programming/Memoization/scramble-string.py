# https://leetcode.com/problems/scramble-string/description/


# TC: O(n^4)
# SC: O(n^3)

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        memo = {}

        def helper(a, b):

            n = len(a)

            if a == b:
                return True

            if n == 1 or len(b) != n:
                return False

            key = a + " " + b

            if key in memo:
                return memo[key]

            # For every iteration it can two condition
            # 1. We should proceed without swapping
            # 2. We should swap before looking next
            for i in range(1, n):

                # without swap
                # Left part of first and second string and right part of first and second string should be scramble
                if helper(a[:i], b[:i]) and helper(a[i:], b[i:]):
                    memo[key] = True
                    return True

                # with swap
                # Left part of first and right part of second and right part of first and left part of second string should be scramble
                if helper(a[:i], b[n - i:]) and helper(a[i:], b[:n - i]):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return helper(s1, s2)


print(Solution().isScramble("great", "rgeat"))
print(Solution().isScramble("abcde", "caebd"))