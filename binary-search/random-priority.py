import random

"""

Given an array of positive integers, where each value within the array represents a multiple times weight of the corresponding index, 
implement a structure which can be invoked to pick a random index within that array according to in proportion to its weight.

array [1, 7, 2]

With N 10 times called:
- 0 index returned 1 time
- 1 index returned 7 times
- 2 index returned 2 times

"""

# Similar question - https://leetcode.com/problems/random-pick-with-weight/


class Solution:

    def __init__(self, w):
        self.arr = []
        val = 0
        for weight in w:
            val += weight
            self.arr.append(val)

    def pickIndex(self):

        # Use 1 to total sum, not length
        t = random.randint(1, self.arr[-1])
        l, r = 0, len(self.arr)

        while l < r:
            m = (l + r) // 2
            if t > self.arr[m]:
                l = m + 1
            else:
                r = m

        return l


obj = Solution([1, 7, 2])

# Test case
print(obj.pickIndex())
print(obj.pickIndex())

# Variation of the problem with cities and populations

'''

You are conducting an A/B test and need to randomly pick a person from a
user base spread across multiple cities. Each city has a known population, and
you need to ensure that the probability of choosing a user from each city is
proportional to the city's population.

You are given a 0-indexed array of pairs city_populations, where each pair
consists of a string representing the name of the ith city, and an integer
representing the population of the ith city (in millions, but treat these values
as if in ones for computation purposes).

You need to implement the function pickIndex(), which randomly picks a
person in and returns the name of the city the person is in.

Example 1:

Input
["Solution","pickIndex","pickIndex"]
[[["Seattle", 500], ["New York", 900], ["Los Angeles",
400]], [], []]

Output
[null, "New York", "Los Angeles"]

Explanation
Solution solution = new Solution([["Seattle", 500],
["New York", 900], ["Los Angeles", 400]]);
solution.pickIndex(); // return "New York". It is
returning the second element (index = 1) that has a
probability of 900/(500+900+400).

'''

class Solution:

    def __init__(self, city_populations):

        val = 0
        self.arr = []

        # 0 - 499,  500 - 1399, 1400 - 1799
        for city, population in city_populations:
            val += population
            self.arr.append((city, val))

    def pickIndex(self):

        t = random.randint(1, self.arr[-1][1])
        l, r = 0, len(self.arr)

        while l < r:
            m = (l + r) // 2
            if t > self.arr[m][1]:
                l = m + 1
            else:
                r = m

        return self.arr[l][0]


obj = Solution([["Seattle", 500], ["New York", 900], ["Los Angeles", 400]])

# Test case
print(obj.pickIndex())
print(obj.pickIndex())