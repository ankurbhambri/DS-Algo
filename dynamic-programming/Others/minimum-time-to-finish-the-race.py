# https://leetcode.com/problems/minimum-time-to-finish-the-race/description/


class Solution:
    def minimumFinishTime(self, tires: list[list[int]], changeTime: int, numLaps: int) -> int:

        n = len(tires)

        # Step 1: Precomputation (without_change)
        # without_change[i][j] ka matlab: tire 'i' ko lagatar 'j' laps chalane ka total time
        # Hum max 20 laps tak hi check karenge kyunki uske baad changeTime se bada ho jayega.
        without_change = [[float('inf')] * 20 for _ in range(n)]

        for i in range(n):

            f_i, r_i = tires[i][0], tires[i][1]

            # Pehle lap ka time
            current_lap_time = f_i
            total_time = f_i
            without_change[i][1] = total_time

            for j in range(2, 20):
                current_lap_time *= r_i
                # Agar ek hi lap ka time bohot bada ho jaye toh aage check karne ka faayda nahi
                if current_lap_time >= 2e9: 
                    break
                total_time += current_lap_time
                without_change[i][j] = total_time

        # Step 2: Dynamic Programming
        # dp[x] = x laps khatam karne ka minimum time
        dp = [float('inf')] * (numLaps + 1)

        for x in range(1, numLaps + 1):
            # Case A: Agar x chota hai (< 20), toh ho sakta hai bina tyre badle hi chalaya ho
            if x < 20:
                for i in range(n):
                    dp[x] = min(dp[x], without_change[i][x])

            # Case B: Tyre change karne wala logic
            # Hum pichle sirf 18 laps tak check karenge (j >= x - 18)
            start_j = max(1, x - 18)
            for j in range(start_j, x):
                dp[x] = min(dp[x], dp[j] + changeTime + dp[x - j])

        return dp[numLaps]


print(Solution().minimumFinishTime([[2, 3], [3, 4]], 5, 4))  # Output: 21
print(Solution().minimumFinishTime([[1, 10], [2, 2], [3, 4]], 6, 5))  # Output: 25