# https://leetcode.com/problems/candy

'''

Each child must get at least one candy. Children with a higher rating than their immediate neighbors should get more candies.

The classic greedy solution involves two passes:

Left to right – ensure increasing sequence gets more candy.

Right to left – ensure decreasing sequence also gets more when needed.

'''

class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        # Left to right: ensure right > left gets more candy
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left: ensure left > right gets more candy
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)


print(Solution().candy([1, 0, 2]))  # Output: 5
print(Solution().candy([1, 2, 2]))  # Output: 4
print(Solution().candy([1, 3, 2, 2, 1]))  # Output: 9
print(Solution().candy([1, 2, 3, 4, 5]))  # Output: 15
