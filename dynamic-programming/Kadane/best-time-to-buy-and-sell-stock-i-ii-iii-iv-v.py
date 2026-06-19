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


# Variant: What if we were given two vectors instead, and the context of the problem changes to purchasing departure and returning flight tickets?

'''

You are given two arrays departures and returns where departures[i] and returns[i] are ticket prices for departing and returning flights on the ith
day, respectively.

You want to minimize your cost by choosing a single day to buy a departure flight and choosing a different day in the future to buy a returning flight.
Return the minimum cost you can achieve from a single round-trip flight.

Example 1:

Input: departures = [1, 2, 3, 4], returns = [4, 3, 2, 1]

Output: 2

Explanation: Buy a departure flight on day 0 (price = 1) and buy a return ticket on day 3 (price = 1), cost = 1 + 1 = 2.

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


print(Solution().minFlightCost([5,1,3], [2,4,1]))  # Expected output: 2 (Depart on day 1 at price 1, return on day 2 at price 1)
print(Solution().minFlightCost([1,2,3,4], [4,3,2,1]))  # Expected output: 2



# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

#TC: O(n)
#SC: O(1)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res = 0
        for r in range(1, len(prices)):
            # Yha pe hum har adjacent pair ko check karenge, agar profit hai toh usko add kar denge, kyunki multiple transactions allowed hain
            cur = prices[r] - prices[r - 1]
            if cur < 0:
                cur = 0
            else:
                res += cur
        return res


print(Solution().maxProfit([1, 2, 3, 4, 5]))  # 4
print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 7


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# TC: O(n)
# SC: O(1)
class Solution:
    def maxProfit(self, prices):

        if not prices:
            return 0

        # Initialize our states for Day 0
        # Before we buy, we have 0 cash. After buying, we are in debt by prices[0].
        first_buy = -prices[0]
        first_sell = 0

        second_buy = -prices[0]
        second_sell = 0

        for price in prices:
            # State 1: Maximize cash after 1st buy. 
            # (Either keep previous buy, or buy at today's price)
            first_buy = max(first_buy, -price)

            # State 2: Maximize cash after 1st sell. 
            # (Either keep previous sell profit, or sell today using our 1st buy)
            first_sell = max(first_sell, first_buy + price)

            # State 3: Maximize cash after 2nd buy. 
            # (Either keep previous, or buy today using the profit made from 1st sell)
            second_buy = max(second_buy, first_sell - price)

            # State 4: Maximize ultimate cash after 2nd sell.
            # (Either keep previous, or sell today using our 2nd buy)
            second_sell = max(second_sell, second_buy + price)

        return second_sell

        # @lru_cache(None)
        # def helper(i, hold, transactions_left):
        #     # BASE CASES
        #     # 1. If we run out of days, or run out of allowed transactions, no more profit can be made.
        #     if i == len(prices) or transactions_left == 0:
        #         return 0

        #     if hold:
        #         # Choice 1: Skip selling today
        #         skip = helper(i + 1, True, transactions_left)
        #         # Choice 2: Sell today! We gain prices[i] cash, and we lose 1 transaction capacity.
        #         sell = prices[i] + helper(i + 1, False, transactions_left - 1)

        #         return max(skip, sell)
        #     else:
        #         # Choice 1: Skip buying today
        #         skip = helper(i + 1, False, transactions_left)
        #         # Choice 2: Buy today! We spend prices[i] cash. Transaction count doesn't change until we sell.
        #         buy = -prices[i] + helper(i + 1, True, transactions_left)

        #         return max(skip, buy)

        # # Start on Day 0, not holding anything, with 2 transactions left
        # return helper(0, False, 2)


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv

# TC: O(n * k)
# SC: O(k)
class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:

        if not prices or k == 0:
            return 0

        # Agar k bahut bada hai (n/2 se zyada), toh yeh simple "Buy low, Sell high" ban jata hai
        if k >= len(prices) // 2:
            return sum(max(0, prices[i] - prices[i-1]) for i in range(1, len(prices)))

        # Arrays ko initialize karein
        buy = [-float('inf')] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                # j-th baar kharidne ka decision: pehle wale sell profit se price minus karo
                buy[j] = max(buy[j], sell[j-1] - price)
                # j-th baar bechne ka decision: current buy price mein aaj ka price add karo
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k] # k transactions ke baad ka max profit

'''
        n = len(prices)
        if n == 0 or k == 0:
            return 0
            
        # Memoization table (cache) tabdeel karne ke liye
        memo = {}

        def dfs(i, tx_left, holding):
            # Base Case: Agar saare din khatam ya transactions khatam
            if i == n or tx_left == 0:
                return 0
                
            if (i, tx_left, holding) in memo:
                return memo[(i, tx_left, holding)]
            
            # Option 1: Kuch mat karo, agle din par jao (Skip)
            skip = dfs(i + 1, tx_left, holding)
            
            if holding:
                # Option 2: Stock bech do (+prices[i] profit milega)
                # Bechne par humara ek transaction complete hota hai -> tx_left - 1
                sell = prices[i] + dfs(i + 1, tx_left - 1, 0)
                memo[(i, tx_left, holding)] = max(skip, sell)
            else:
                # Option 2: Stock kharid lo (-prices[i] jeb se jayega)
                buy = -prices[i] + dfs(i + 1, tx_left, 1)
                memo[(i, tx_left, holding)] = max(skip, buy)
                
            return memo[(i, tx_left, holding)]

        return dfs(0, k, 0) # Day 0 se start, k transactions baaki, holding = 0
'''


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v

# TC: O(n * k)
# SC: O(k)
class Solution:
    def maximumProfit(self, nums: list[int], k: int) -> int:

        sold = [0] * k
        res = [0] * (k + 1)
        bought = [-float('inf')] * k

        for num in nums:

            for j in range(k, 0, -1):

                res[j] = max(res[j], bought[j - 1] + num, sold[j - 1] - num)

                bought[j - 1] = max(bought[j - 1], res[j - 1] - num)

                sold[j - 1] = max(sold[j - 1], res[j - 1] + num)

        return max(res)


print(Solution().maximumProfit([1, 2, 3, 4, 5], 2))  # Expected output: 4 (Buy on day 0 at price 1, sell on day 4 at price 5)
print(Solution().maximumProfit([7, 1, 5, 3, 6, 4], 2))  # Expected output: 7 (Buy on day 1 at price 1, sell on day 4 at price 6)