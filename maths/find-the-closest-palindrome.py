# https://leetcode.com/problems/find-the-closest-palindrome/


class Solution:
    def nearestPalindromic(self, n: str) -> str:

        L = len(n)
        num = int(n)

        candidates = set()

        # iska matlab hai ki agar n = 1000 hai, toh closest palindrome 999 hoga, ya agar n = 100 hai, toh closest palindrome 99 hoga
        candidates.add(10 ** (L - 1) - 1)

        # iska matlab hai ki agar n = 999 hai, toh closest palindrome 1001 hoga, ya agar n = 99 hai, toh closest palindrome 101 hoga
        candidates.add(10 ** L + 1)

        half = (L + 1) // 2

        # yha hum prefix ko half length ke digits ke saath le rahe hain, aur fir usse palindrome banane ke liye use kar rahe hain
        prefix = int(n[:half])

        # yha hum prefix ke aas paas ke 3 candidates ko consider kar rahe hain: prefix - 1, prefix, aur prefix + 1. 
        # Ye 3 candidates humein closest palindrome dhoondhne mein help karenge.
        for p in [prefix - 1, prefix, prefix + 1]:

            s = str(p)

            # odd ke case mein, hum middle digit ko repeat nahi karenge, aur even ke case mein hum middle digit ko repeat karenge
            if L % 2:
                pal = int(s + s[:-1][::-1])

            # even ke case mein, hum middle digit ko repeat karenge
            else:
                pal = int(s + s[::-1])

            candidates.add(pal)

        # Iss step mein hum closest palindrome ko find kar rahe hain. Hum har candidate ko check kar rahe hain aur usse compare kar rahe hain ki kaunsa closest hai.
        # Agar do candidates same distance par hain, toh hum chhota wala choose karenge
        ans = None
        for x in candidates:

            if x == num:
                continue

            if ans is None:
                ans = x
            
            # yha pe hum check kar rahe hain ki current candidate x aur num ke beech ka distance ans aur num ke beech ke distance se chhota hai ya nahi.
            elif abs(x - num) < abs(ans - num):
                ans = x

            # Agar distance same hai, toh chhota wala choose karenge
            elif abs(x - num) == abs(ans - num) and x < ans:
                ans = x

        return str(ans)