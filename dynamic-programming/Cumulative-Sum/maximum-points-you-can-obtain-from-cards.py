# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:

        n = len(cardPoints)

        if k == n:
            return sum(cardPoints)

        # here, we have to find the length of n - k cards with minimum sum, so that when we subtract from the total sum of all elements we get the maximum value
        # for example N = 7, k = 3, then we have to find the minimum sum of 4 cards, so that when we subtract from the total sum of all elements we get the maximum value
        window = n - k

        # to start I took first window of n - k elements
        curr = sum(cardPoints[:window])

        mn = curr

        for i in range(window, n):

            # adding from the right and removing from the left
            curr += cardPoints[i]
            curr -= cardPoints[i - window]

            mn = min(mn, curr)

        # in the end will subtract the minimum sum of n - k cards from the total sum of all elements to get the maximum value
        return sum(cardPoints) - mn


print(Solution().maxScore([2, 2, 2], 2)) # 4
print(Solution().maxScore([1, 2, 3, 4, 5, 6, 1], 3)) # 12