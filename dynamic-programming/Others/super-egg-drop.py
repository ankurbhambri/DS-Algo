# https://leetcode.com/problems/super-egg-drop/

# TC: O(n * k)
# SC: O(n * k)
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1): # i moves

            for j in range(1, k + 1): # j eggs

                # agar j eggs hain aur i moves hain toh hum maximum kitne floors check kar sakte hain

                # dp[i - 1][j - 1] -> agar egg tut jata hai toh humare paas j-1 eggs bache hain aur i-1 moves bache hain toh hum kitne floors check kar sakte hain

                # dp[i - 1][j] -> agar egg nahi tuti toh humare paas j eggs bache hain aur i-1 moves bache hain toh hum kitne floors check kar sakte hain

                dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]

            if dp[i][j] >= n:
                return i

        return -1

print(Solution().superEggDrop(1, 2))
print(Solution().superEggDrop(2, 6))