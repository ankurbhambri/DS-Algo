# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/


# TC: O(steps * min(arrLen, steps)) - We iterate through each step and for each step, we iterate through the possible indices up to min(arrLen, steps).
# SC: O(min(arrLen, steps)) - We use a DP array of size min

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10**9 + 7
        
        # Max index jo hum reach kar sakte hain
        max_idx = min(arrLen - 1, steps // 2)
        
        # dp[i] store karega index i par hone ke ways
        # Shuruat mein hum index 0 par hain, toh wahan 1 way hai
        dp = [0] * (max_idx + 1)
        dp[0] = 1
        
        # Har step ke liye calculate karein
        for _ in range(steps):

            next_dp = [0] * (max_idx + 1)

            for i in range(max_idx + 1):

                # 1. Stay (wahi rehna)
                ways = dp[i]
                
                # 2. Left se aana (agar left valid index hai)
                if i > 0:
                    ways = (ways + dp[i - 1]) % MOD
                    
                # 3. Right se aana (agar right valid index hai)
                if i < max_idx:
                    ways = (ways + dp[i + 1]) % MOD
                    
                next_dp[i] = ways
            
            # Agle step ke liye dp array ko update karein
            dp = next_dp
            
        # End mein index 0 par stay karne ke total ways
        return dp[0]


print(Solution().numWays(3, 2))  # Output: 4
print(Solution().numWays(2, 4))  # Output: 2