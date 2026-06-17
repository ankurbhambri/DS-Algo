# https://leetcode.com/problems/minimum-time-to-finish-the-race


# TC: O(N + L), N = number of tires aur L = numLaps
# SC: O(L), L = numLaps
class Solution:
    def minimumFinishTime(self, tires: list[list[int]], changeTime: int, numLaps: int) -> int:

        # Max lap 18 isliye kyunki 2^18 = 262144 > 10^5 (max time limit)
        MAX_LAPS = min(18, numLaps)

        # Step 1: Bina tire badle x laps ka min time nikalna
        min_time_for_laps = [float("inf")] * (MAX_LAPS + 1)

        for f, r in tires:
            current_lap_time = f
            total_time = f
            lap = 1

            # Jab tak time limit se bahar na jaye, check karo
            while lap <= MAX_LAPS and current_lap_time < changeTime + f:
                min_time_for_laps[lap] = min(min_time_for_laps[lap], total_time)
                current_lap_time *= r
                total_time += current_lap_time
                lap += 1

        # Step 2: DP lagao pure laps ka answer nikalne ke liye
        dp = [float("inf")] * (numLaps + 1)
        dp[0] = 0 # 0 lap ke liye 0 time

        for i in range(1, numLaps + 1):

            # Option A: Agar bina tire badle direct i laps ho sake (sirf chote laps ke liye)
            if i <= MAX_LAPS:
                dp[i] = min_time_for_laps[i]

            # Option B: j laps pehle kiye, fir pit stop liya (tire badla), fir baaki laps kiye
            for j in range(1, min(i, MAX_LAPS + 1)):
                # iss recurrence ka meaning hai: i - j laps pehle kiye, fir changeTime lagaya, fir j laps ka time add kiya
                dp[i] = min(dp[i], dp[i - j] + changeTime + min_time_for_laps[j])

        return dp[numLaps]


# tires[i] = [fi, ri]
# fi (Initial Time / Base Time)
# ri (Multiplier / Cost Factor)
print(Solution().minimumFinishTime([[2, 3], [3, 4]], 5, 4))  # Output: 21
# print(Solution().minimumFinishTime([[1, 10], [2, 2], [3, 4]], 6, 5))  # Output: 25