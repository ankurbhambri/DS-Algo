# https://leetcode.com/problems/race-car/


# TC: O(n * log(n))
# SC: O(n)
class Solution:
    def racecar(self, target: int) -> int:

        # DP array initialize karte hain jismein max steps store honge
        dp = [0] * (target + 1)

        for i in range(1, target + 1):

            # i ko cross karne ke liye kitne bits (ya steps) chahiye
            k = i.bit_length()

            # Case 1: Agar i perfectly 2^k - 1 ke barabar hai
            if i == (2 ** k) - 1:
                dp[i] = k
                continue

            # Case 2: Overshoot karke piche aana
            # k steps aage + 1 step Reverse + bacha hua distance cover karne ke steps
            dp[i] = k + 1 + dp[(2 ** k) - 1 - i]

            # Case 3: Target se pehle rukna, thoda piche jana, fir aage badhna
            for j in range(k - 1):

                # j steps piche jaane ke baad distance 
                forward_distance = (2 ** (k - 1)) - (2 ** j)

                # (k-1) steps aage + 1 Reverse + j steps piche + 1 Reverse + remaining distance cover karne ke steps
                dp[i] = min(dp[i], (k - 1) + 1 + j + 1 + dp[i - forward_distance])

        return dp[target]


print(Solution().racecar(3)) # 2 -> A A
print(Solution().racecar(6)) # 5 -> A A A R A