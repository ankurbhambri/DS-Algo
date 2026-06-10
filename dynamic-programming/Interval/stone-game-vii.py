# https://leetcode.com/problems/stone-game-vii/


# TC: O(n^2) - 2 nested loops
# SC: O(n^2) - DP table
class Solution:
    def stoneGameVII(self, stones: list[int]) -> int:

        n = len(stones)

        # 1. Prefix Sum bana rahe hain taaki kisi bhi range ka sum jaldi (O(1) mein) nikal sake
        preSum = [0] * (n + 1)

        for i in range(n):
            preSum[i + 1] = preSum[i] + stones[i]

        # Chhota sa helper function: left se right tak ke saare stones ka sum nikalne ke liye
        def getSum(left, right):
            return preSum[right + 1] - preSum[left]

        # 2. DP Table (2D Array) banayi jisme saare answers store honge
        # dp[l][r] ka matlab hai: 'l' se 'r' tak ke stones bache ho toh max kitna score difference ban sakta hai
        dp = [[0] * n for _ in range(n)]

        # 3. 'l' (left) ko piche se shuru kar rahe hain (n-1 se 0)
        # Kyunki dp[l][r] nikalne ke liye niche wali row yaani dp[l + 1][r] ka answer pehle se ready hona chahiye
        for l in range(n - 1, -1, -1):

            # 'r' (right) hamesha 'l' ke aage se shuru hoga (l+1 se lekar n-1 tak)
            for r in range(l + 1, n):

                # OPTION 1: Agar pehla (l) stone uthaya, toh bache hue stones ka sum (l+1 se r) milega
                L = getSum(l + 1, r)

                # OPTION 2: Agar aakhri (r) stone uthaya, toh bache hue stones ka sum (l se r-1) milega
                R = getSum(l, r - 1)

                # APNA FAYDA MAXIMIZE KARO:
                # (Mera mila hua score) - (Agle player ka best score jo bache hue game se milega)
                dp[l][r] = max(L - dp[l + 1][r], R - dp[l][r - 1])

        # 4. Poori line (0 se n-1) ka final maximum score difference return kar do
        return dp[0][n - 1]


print(Solution().stoneGameVII([5, 3, 1, 4, 2]))  # Output: 6
print(Solution().stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]))  # Output: 122