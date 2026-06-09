# https://leetcode.com/problems/can-i-win/


from functools import lru_cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        # Base Case 1: Agar saare numbers ka total sum bhi desiredTotal se kam hai,
        # toh koi bhi kabhi nahi jeet payega, isliye False.
        total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if total_sum < desiredTotal:
            return False

        # Base Case 2: Agar desiredTotal 0 ya usse kam hai, toh pehla player bina kuch kiye hi jeet gaya.
        if desiredTotal <= 0:
            return True

        @lru_cache(None)
        def solve(mask, current_total):

            # Hum saare bache hue numbers try karenge (1 se lekar maxChoosableInteger tak)
            for i in range(1, maxChoosableInteger + 1):

                # Check karo kya number 'i' abhi available hai? (bit 0 honi chahiye)
                if not (mask & (1 << i)):

                    # Option A: Agar main 'i' chunta hoon aur seedhe jeet jata hoon
                    if current_total + i >= desiredTotal:
                        return True

                    # Option B: Main 'i' chunta hoon, aur apna naya mask aur naya total saamne wale ko de deta hoon.
                    # Agar saamne wala player us state se HAAR jata hai (solve(...) == False), 
                    # iska matlab MERI JEET pakki hai!
                    if not solve(mask | (1 << i), current_total + i):
                        return True

            # Agar koi bhi number chunne se meri jeet guaranteed nahi ho rahi, toh main haar gaya
            return False

        # Shuruat mein mask 0 hai (koi number nahi chuna) aur current total bhi 0 hai
        return solve(0, 0)


print(Solution().canIWin(10, 0))   # Output: True
print(Solution().canIWin(10, 11))  # Output: False