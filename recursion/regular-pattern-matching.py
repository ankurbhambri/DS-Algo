# https://leetcode.com/problems/regular-expression-matching/


def isMatch(s, p):

    memo = {}

    def helper(i, j):

        if j >= len(p):
            return i >= len(s)

        if (i, j) in memo:
            return memo[(i, j)]

        first_char = i < len(s) and (p[j] == s[i] or p[j] == ".")

        if j + 1 < len(p) and p[j + 1] == "*":

            notTake = helper(i, j + 2)
            take = first_char and helper(i + 1, j)

            memo[(i, j)] = notTake or take

            return memo[(i, j)]

        memo[(i, j)] = first_char and helper(i + 1, j + 1)

        return memo[(i, j)]

    return helper(0, 0)


print(isMatch("aa", "a"))  # False
print(isMatch("aa", "a*"))  # True
print(isMatch("ab", ".*"))  # True
