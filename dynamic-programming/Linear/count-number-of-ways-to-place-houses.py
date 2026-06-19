# https://leetcode.com/problems/count-number-of-ways-to-place-houses


class Solution:
    def countHousePlacements(self, n: int) -> int:

        MOD = 10**9 + 7

        # Base cases ek side ke liye
        # prev matlab n=0 ke liye (1 tarika: khali)
        # curr matlab n=1 ke liye (2 tarike: Khali ya Ghar)
        prev = 1
        curr = 2

        # Loop chalao n plots tak ek side ke liye value nikalne ko
        for _ in range(2, n + 1):
            next_ways = (curr + prev) % MOD
            prev = curr
            curr = next_ways

        # curr me ab ek side ke total tarike hain.
        # Dono sides ke liye: (one_side * one_side)
        total_ways = (curr * curr) % MOD

        return total_ways


print(Solution().countHousePlacements(1))  # Output: 4
print(Solution().countHousePlacements(2))  # Output: 9