#  https://leetcode.com/problems/prime-arrangements/

# Pehle nikalo ki 1 se n ke beech mein kitne prime numbers hain, aur kitne non-prime numbers hain.

# Fir unka factorial nikal ke multiply kar do, aur answer ko 10^9 + 7 se mod kardo.

# Factorial isliye nikalna hai kyunki hum prime numbers ko alag se arrange kar sakte hain, aur non-prime numbers ko bhi alag se arrange kar sakte hain. 

# Formula - Total arrangements = (prime_count)! * (non_prime_count)!

# TC: O(n * sqrt(n)) for counting primes + O(n) for calculating factorials
# SC: O(1) if we don't consider the space used for recursion in factorial calculation
class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        MOD = 10**9 + 7

        # check karo number prime hai ya nahi
        def isPrime(num):

            if num < 2:
                return False

            d = 2
            while d * d <= num:
                if num % d == 0:
                    return False
                d += 1

            return True

        prime_count = 0

        # agar hai toh prime_count ko increment karo
        for num in range(1, n + 1):
            if isPrime(num):
                prime_count += 1

        # yha pe factorial nikal rhe h count ka
        def factorial(x):
            ans = 1

            for i in range(2, x + 1):
                ans = (ans * i) % MOD

            return ans

        return (factorial(prime_count) * factorial(n - prime_count)) % MOD


print(Solution().numPrimeArrangements(5))  # Output: 12
print(Solution().numPrimeArrangements(100))  # Output: 682289015