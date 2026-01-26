# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices) -> int:

        l = 0
        res = 0

        for r in range(len(prices)):

            cur = prices[r] - prices[l]

            if cur < 0:
                l = r

            else:
                res = max(res, cur)

        return res

print(Solution().maxProfit([7, 6, 4, 3, 1]))  # 0
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5


# Variant: what if we were given two vectors instead, and the context of the problem changes to purchasing departure and returning flight tickets?

'''

You are given two arrays departures and returns where departures[i] and returns[i] are ticket prices for departing and returning flights on the ith
day, respectively.

You want to minimize your cost by choosing a single day to buy a departure flight and choosing a different day in the future to buy a returning flight.
Return the minimum cost you can achieve from a single round-trip flight.

Example 1:

Input: departures = [1,2,3,4], returns = [4,3,2,1]

Output: 2

Explanation: Buy a departure flight on day 0 (price = 1) and buy a return ticket on day 3 (price = 1), cost = 1+1 = 2.

'''

# Idea, we need to find a cheap departure today and a cheap return flight later.

class Solution:
    def minFlightCost(self, departures, returns) -> int:

        # We need at least one day to depart and a later day to return
        if len(departures) < 2:
            return 0 

        # Initialize min_dep with the first day's departure price
        min_dep = departures[0]

        # Initialize result with a very large number (infinity)
        # because we are looking for the minimum cost.
        res = float('inf')

        # Start from Day 1 because you can only return on Day 1 or later
        for r in range(1, len(returns)):
            # Calculate cost if we returned today using the best departure found so far
            current_trip_cost = min_dep + returns[r]
            
            # Update our best (minimum) result
            res = min(res, current_trip_cost)
            
            # Update min_dep for future return dates
            min_dep = min(min_dep, departures[r])

        return res

print(Solution().minFlightCost([1,2,3,4], [4,3,2,1]))  # Expected output: 2
print(Solution().minFlightCost([5,1,3], [2,4,1]))  # Expected output: 2 (Depart on day 1 at price 1, return on day 2 at price 1)