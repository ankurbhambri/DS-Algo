#  https://leetcode.com/problems/prime-arrangements/

'''
Idea here is to find the number of prime numbers up to n and then find the number of permutations of prime numbers and non-prime numbers.
We can use Sieve of Eratosthenes to find the number of prime numbers up to n.
Then we can use Factorial formula to find the number of permutations of prime numbers and non-prime numbers.
'''

class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        MOD = 10**9 + 7

        # 1. Function to count primes up to n
        def count_primes(n):
            if n < 2: return 0
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for p in range(2, int(n**0.5) + 1):
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
            return sum(is_prime)

        # 2. Factorial function with modulo
        def factorial(k):
            res = 1
            for i in range(1, k + 1):
                res = (res * i) % MOD
            return res

        # Main Logic
        num_primes = count_primes(n)
        num_non_primes = n - num_primes

        # Total Ways = Ways to arrange Primes * Ways to arrange Non-Primes
        return (factorial(num_primes) * factorial(num_non_primes)) % MOD


print(Solution().numPrimeArrangements(5))  # Output: 12
print(Solution().numPrimeArrangements(100))  # Output: 682289015