# https://leetcode.com/problems/beautiful-arrangement


# Backtracking approach

# TC: O(n!) (n = number of integers)
# SC: O(n) (used array ke liye)
class Solution:
    def countArrangement(self, n: int):

        self.res = 0

        used = [False] * (n + 1)
        
        def dfs(pos):

            if pos > n:
                self.res += 1
                return

            for num in range(1, n + 1):

                if not used[num] and (num % pos == 0 or pos % num == 0):

                    used[num] = True

                    dfs(pos + 1)

                    used[num] = False

        dfs(1)

        return self.res


# Bitmask + DP approach
# TC: O(n * 2^n) (n = number of integers)
# SC: O(2^n) (dp dictionary ke liye)

class Solution:
    def countArrangement(self, n: int):

        memo = {}

        def helper(mask):

            pos = mask.bit_count() + 1

            if pos > n:
                return 1

            if mask in memo:
                return memo[mask]

            ans = 0

            for num in range(1, n + 1):

                # yha pe hum check kar rahe hai ki kya yeh number already use ho chuka hai ya nahi (mask ke through)
                if not (mask & (1 << (num - 1))):

                    if num % pos == 0 or pos % num == 0:
                        
                        # agar condition satisfy ho rahi hai toh is number ko use karte hue next position ke liye recursive call karenge
                        # uske liye hum mask me is number ka bit set kar denge (mask | (1 << (num - 1)))

                        ans += helper(mask | (1 << (num - 1)))

            memo[mask] = ans
            return ans

        return helper(0)