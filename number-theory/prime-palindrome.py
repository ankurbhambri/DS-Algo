# https://leetcode.com/problems/prime-palindrome/

class Solution:
    def primePalindrome(self, n: int) -> int:

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        # Special case for 8 to 11
        if 8 <= n <= 11:
            return 11
        
        # Hum palindromes generate karenge unke half-part se
        # 10**5 tak ki roots humein 9-digit palindromes tak le jayengi
        for i in range(1, 100000):

            s = str(i)

            # Odd length palindrome generate karna (e.g., '123' -> '123' + '21' = '12321')
            val = int(s + s[-2::-1])
            
            if val >= n and is_prime(val):
                return val

        return -1


print(Solution().primePalindrome(6))  # 7
print(Solution().primePalindrome(8))  # 11
print(Solution().primePalindrome(13))  # 101
print(Solution().primePalindrome(9989900))  # 100030001