# https://leetcode.com/problems/remove-boxes/description


def removeBoxes(boxes):

    memo = {}

    def dp(l, r, k):
        # Base case: no boxes left
        if l > r:
            return 0

        if (l, r, k) in memo:
            return memo[(l, r, k)]

        # Extend the group of the same color as boxes[r]
        while l < r and boxes[r] == boxes[r - 1]:
            r -= 1
            k += 1

        # Case 1: Remove all boxes[r] together
        res = dp(l, r - 1, 0) + (k + 1) ** 2

        # Case 2: Merge boxes[r] with earlier groups of the same color
        for m in range(l, r):
            if boxes[m] == boxes[r]:
                res = max(res, dp(l, m, k + 1) + dp(m + 1, r - 1, 0))

        memo[(l, r, k)] = res

        return memo[(l, r, k)]

    return dp(0, len(boxes) - 1, 0)


print(removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]))  # Output: 23
