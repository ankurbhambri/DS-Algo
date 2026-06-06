# https://leetcode.com/problems/ugly-number/

def isUgly(n):
    
    if n <= 0:
        return False
    
    for p in [2,3,5]:
        while n % p == 0:
            n = n // p

    return n == 1

# https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        # DP array jisme hum saare ugly numbers store karenge
        dp = [0] * n
        dp[0] = 1 # Pehla ugly number hamesha 1 hota hai
        
        # Pointers for 2, 3, and 5
        p2 = p3 = p5 = 0
        
        for i in range(1, n):
            # Agle teen candidate nikalte hain
            next_2 = dp[p2] * 2
            next_3 = dp[p3] * 3
            next_5 = dp[p5] * 5
            
            # Jo sabse chota hai, wahi agla ugly number hoga
            next_ugly = min(next_2, next_3, next_5)
            dp[i] = next_ugly
            
            # Jis pointer ka candidate select hua, use aage badhao
            # Alag-alag 'if' isliye hain taaki duplicates handle ho sakein (jaise 6 ke case mein)
            if next_ugly == next_2:
                p2 += 1
            if next_ugly == next_3:
                p3 += 1
            if next_ugly == next_5:
                p5 += 1

        return dp[-1] # n-th ugly number return karo