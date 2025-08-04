# https://leetcode.com/problems/fruit-into-baskets

# Here, the problem is asking for the length of the longest subarray with at most 2 distinct elements.
# This is a variation of the sliding window problem where we maintain a window that contains at most
# two types of fruits (or characters, or numbers, etc.).

class Solution:
    def totalFruit(self, fruits) -> int:

        l = 0
        res = 0
        freq = {}

        for r in range(len(fruits)):

            freq[fruits[r]] = 1 + freq.get(fruits[r], 0)

            while len(freq) > 2:

                freq[fruits[l]] -= 1

                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]

                l += 1

            res = max(res, r - l + 1)

        return res

print(Solution().totalFruit([1, 2, 1]))  # 3
print(Solution().totalFruit([0, 1, 2, 2]))  # 3
print(Solution().totalFruit([1, 2, 3, 2, 2]))  # 4
print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # 5