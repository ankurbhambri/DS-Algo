# https://leetcode.com/problems/maximize-grid-happiness/

# Constraints: not too large, so we can use bitmasking and memoization to solve the problem efficiently.
# 1 <= m, n <= 5
# 0 <= introvertsCount, extrovertsCount <= min(m * n, 6) 

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:

        # Shuruat mein grid khali hai, toh mask = 0
        self.memo = {}

        def solve(r, c, i_count, e_count, mask):

            # Base Case: Agar saari rows khatam ho gayi hain
            if r == m:
                return 0

            # Agar column khatam ho jaye, toh agli row ke pehle column par jao
            if c == n:
                return solve(r + 1, 0, i_count, e_count, mask)

            # Memoization check: Agar yeh state pehle solve ho chuki hai
            state = (r, c, i_count, e_count, mask)
            if state in self.memo:
                return self.memo[state]

            # Hum is cell ke upar aur left wale padosi ka status nikalte hain
            # Mask ka sabse left-most digit 'Up' padosi hota hai
            up_neighbor = mask // (3 ** (n - 1))

            # Left padosi tabhi valid hoga agar hum row ke pehle column par nahi hain
            left_neighbor = mask % 3 if c > 0 else 0
 
            # Naya mask banane ke liye purane 'up' ko hatana padega
            next_mask_base = (mask % (3 ** (n - 1))) * 3
 
            # Choice 1: Is cell ko khali chhod do (0)
            res = solve(r, c + 1, i_count, e_count, next_mask_base + 0)
 
            # Padosiyon ke sath happiness change calculate karne ka inline function
            def get_diff(p1, p2):
                if p1 == 0 or p2 == 0: return 0
                if p1 == 1 and p2 == 1: return -60
                if p1 == 2 and p2 == 2: return 40
                return -10 # Ek introvert, ek extrovert
 
            # Choice 2: Introvert bitha do (1)
            if i_count > 0:
                take_i = 120 + get_diff(1, up_neighbor) + get_diff(1, left_neighbor)
                res = max(res, take_i + solve(r, c + 1, i_count - 1, e_count, next_mask_base + 1))
 
            # Choice 3: Extrovert bitha do (2)
            if e_count > 0:
                take_e = 40 + get_diff(2, up_neighbor) + get_diff(2, left_neighbor)
                res = max(res, take_e + solve(r, c + 1, i_count, e_count - 1, next_mask_base + 2))
 
            self.memo[state] = res
            return res
 
        return solve(0, 0, introvertsCount, extrovertsCount, 0)


print(Solution().getMaxGridHappiness(m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2))  # Output: 240
print(Solution().getMaxGridHappiness(m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1))  # Output: 260