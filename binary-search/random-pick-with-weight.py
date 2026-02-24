# https://leetcode.com/problems/random-pick-with-weight/

import random

class Solution:
    def __init__(self, w):
        self.arr = []
        val = 0
        for weight in w:
            val += weight
            self.arr.append(val)

    def pickIndex(self) -> int:
        t = random.randint(1, self.arr[-1])  # Use 1 to total sum, not length
        l, r = 0, len(self.arr)
        while l < r:
            m = (l + r) // 2
            if self.arr[m] < t:
                l = m + 1
            else:
                r = m
        return l

print(Solution([1, 3]).pickIndex())  # return 1 with probability 3/4 and 0 with probability 1/4
print(Solution([2, 5, 3]).pickIndex())  # return 0 with probability 2/10, return 1 with probability 5/10 and return 2 with probability 3/10


# Variant: Given a map of city names to its population, return random city name with weight.

import random

class WeightedCityPicker:
    def __init__(self, city_map: dict):

        total = 0
        self.cities = []
        self.prefix_sums = []

        # We iterate in whatever order the dictionary provides
        for city, population in city_map.items():
            total += population
            # Each step increases the sum, ensuring the list is sorted
            self.prefix_sums.append(total)
            self.cities.append(city)

        self.total_sum = total

    def pick(self) -> str:
        target = random.randint(1, self.total_sum)

        # Binary Search works because self.prefix_sums is MONOTONIC (always increasing)
        low, high = 0, len(self.prefix_sums) - 1
        while low < high:
            mid = (low + high) // 2
            if self.prefix_sums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return self.cities[low]

# --- Example with Unsorted Input ---
unsorted_cities = {
    "London": 9,
    "Paris": 2,
    "Tokyo": 14,
    "New York": 8
}

picker = WeightedCityPicker(unsorted_cities)
print(f"Random City: {picker.pick()}")

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