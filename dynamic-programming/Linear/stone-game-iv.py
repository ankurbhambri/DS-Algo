# https://leetcode.com/problems/stone-game-iv/


# TC: O(n * sqrt(n)) - For each number from 1 to n, we check all perfect squares less than or equal to that number.
# SC: O(n) - We use a dp array of size n+1 to store the results for each number of stones.
class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        # dp[i] batayega ki 'i' stones hone par current player jeetega (True) ya haarega (False)
        dp = [False] * (n + 1)

        # 0 stones par hamesha False hoga (Base case)

        # Har ek stone count ke liye check karenge
        for i in range(1, n + 1):

            k = 1

            # Hum saare perfect squares check karenge jo 'i' se chote ya barabar hain
            while k * k <= i:

                # Agar hum i - k*k stones bacha dein, aur wo samne wale ke liye LOSING state ho (False)
                # Toh hum wo chaal chalkar samne wale ko hara denge, matlab hum JEET gaye!

                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Ek bhi winning move mil gayi toh aage check karne ki zaroorat nahi

                k += 1

        return dp[n]


print(Solution().winnerSquareGame(1))  # True
print(Solution().winnerSquareGame(2))  # False