# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/


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