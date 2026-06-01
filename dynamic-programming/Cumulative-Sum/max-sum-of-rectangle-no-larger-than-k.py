# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/

from bisect import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        ans = float('-inf')

        # prefix sum of every row
        for i in range(rows):
            for j in range(1, cols):
                matrix[i][j] += matrix[i][j-1]

        # try every possible width of subarray
        for start in range(cols):

            for end in range(start, cols):

                arr = [0] 
                pref_sum = 0

                # for current width of rectangle
                for i in range(rows):

                    sum_val = matrix[i][end] - (matrix[i][start - 1] if start > 0 else 0)

                    pref_sum += sum_val

                    # --- BINARY SEARCH LOGIC FOR CURRENT ROW ---

                    # Target Formula: Current_Sum - Submatrix_Sum <= k
                    # Isko rearrange karein toh: Current_Sum - k <= Previous_Sum
                    # Yani hamein 'arr' mein ek aisa Previous_Sum dhoodhna hai jo >= target ho.
                    target = pref_sum - k

                    # Binary Search: 'arr' (jo ki sorted hai) mein target ki sahi jagah dhoodho.
                    # Yeh hamein woh sabse pehla index dega jahan value >= target hogi.
                    idx = bisect.bisect_left(arr, target)

                    # Agar idx valid hai, matlab 'arr' mein target se bada ya barabar element mil gaya hai
                    if idx < len(arr):
                        # Current prefix sum mein se us purane sum (arr[idx]) ko minus karo.
                        # Yeh guaranteed ek aisa submatrix sum dega jo <= k hoga.
                        # Hum check karte hain kya yeh ab tak ka sabse bada (maximum) sum hai?
                        ans = max(ans, pref_sum - arr[idx])

                    # Maan lo hamara k = 2 hai (hamein sum <= 2 chahiye).
                    # Hum upar se neeche rows ka sum nikal rahe hain aur hamari sorted list arr mein purane prefix sums pehle se saved hain: arr = [0, 1, 5]

                    # 1. target = pref_sum - k = 6 - 2 = 4
                    # (Iska matlab: Agar hamein submatrix ka sum <= 2 chahiye, toh hamein arr mein se kam se kam 4 ya usse bada number minus karna padega: 6 - 4 = 2)

                    # 2. bisect.bisect_left(arr, 4) -> Yeh arr ([0, 1, 5]) mein check karega ki 4 ya 4 se bada sabse pehla element kahan hai. Woh element hai 5 (index 2 par). Toh idx = 2.

                    # 3. idx < len(arr) -> 2 < 3 (Condition True hai, yani element mil gaya).

                    # 4. ans = max(ans, pref_sum - arr[idx]) -> 6 - 5 = 1. Dekho! Jo sum mila (1), woh hamare k (2) se chhota hai aur valid hai.

                    # arr.insert(pref_sum) -> List ko sorted rakhne ke liye insort use kiya
                    bisect.insort(arr, pref_sum)

        return ans