# https://leetcode.com/problems/profitable-schemes/

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: list[int], profit: list[int]) -> int:

        MOD = 10**9 + 7

        # dp[i][j] -> i bande, j minimum profit
        # Initializing with 0
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]

        # Base Case: Agar profit target 0 hai, toh chahe kitne bhi bande hon (0 se n), 
        # kuch na karne ka hamesha 1 tareeqa hota hai.
        for i in range(n + 1):
            dp[i][0] = 1

        # Har scheme par iterate karenge (Zip use karke dono arrays ko saath mein chalayenge)
        for p_req, p_gain in zip(group, profit):

            # Knapsack style: Reverse loops taaki same scheme baar-baar reuse na ho
            for i in range(n, p_req - 1, -1):

                for j in range(minProfit, -1, -1):

                    # Agar yeh scheme li, toh bacha hua kitna profit chahiye?
                    # Agar p_gain bada hai j se, toh target 0 ho jayega (max trick)
                    rem_profit = max(0, j - p_gain)

                    # Current combinations = Bina is scheme ke + Is scheme ko lekar
                    dp[i][j] = (dp[i][j] + dp[i - p_req][rem_profit]) % MOD

        return dp[n][minProfit]


print(Solution().profitableSchemes(n=5, minProfit=3, group=[2, 2], profit=[2, 3]))  # Output: 2
print(Solution().profitableSchemes(n=10, minProfit=5, group=[2, 3, 5], profit=[6, 7, 8]))  # Output: 7