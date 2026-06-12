# https://leetcode.com/problems/filling-bookcase-shelves/


# Recursion + Memoization
class Solution:
    def minHeightShelves(self, books, shelfWidth):

        memo = {}
        n = len(books)

        def helper(i, rem, maxH):

            if i == n:
                return maxH

            state = (i, rem, maxH)

            if state in memo:
                return memo[state]

            bw, bh = books[i]

            keep = float("inf")

            if bw <= rem:
                keep = helper(
                    i + 1,
                    rem - bw,
                    max(maxH, bh)
                )

            skip = maxH + helper(
                i + 1,
                shelfWidth - bw,
                bh
            )

            memo[state] = min(keep, skip)

            return memo[state]

        first_w, first_h = books[0]

        return helper(1, shelfWidth - first_w, first_h)


print(Solution().minHeightShelves([[1, 3], [2, 4], [3, 2]], 6))  # Output: 4
print(Solution().minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))  # Output: 6


# Bottom-Up Dynamic Programming

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int):

        n = len(books)

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(n):

            width = 0
            height = 0

            for j in range(i, -1, -1):

                width += books[j][0]

                if width > shelfWidth:
                    break

                height = max(height, books[j][1])

                dp[i + 1] = min(
                    dp[i + 1],
                    dp[j] + height
                )

        return dp[n]

print(Solution().minHeightShelves([[1, 3], [2, 4], [3, 2]], 6))  # Output: 4
print(Solution().minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))  # Output: 6