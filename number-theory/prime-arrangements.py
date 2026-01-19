#  https://leetcode.com/problems/prime-arrangements/

# Idea here is to find the number of prime numbers up to n and then find the number of permutations of prime numbers and non-prime numbers.
# We can use Sieve of Eratosthenes to find the number of prime numbers up to n.
# Then we can use permutations formula to find the number of permutations of prime numbers and non-prime numbers.

# We can use the formula: (permutation(prime_count) * permutation(n - prime_count)) % mod


def numPrimeArrangements(n):

    mod = 10**9 + 7

    def total_primes(n):

        if n < 2:
            return 0

        p = 2
        prime = [True] * (n + 1)

        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        return len([p for p in range(2, n + 1) if prime[p]])

    c = total_primes(n)  # prime_count from 1 to n

    def permutations(k):  # permutation formula n! = n * (n - 1) * (n - 2) * ... * 1
        res = 1
        for i in range(2, k + 1):
            res = (res * i) % mod
        return res

    return (permutations(c) * permutations(n - c)) % mod


print(numPrimeArrangements(5))  # 12
print(numPrimeArrangements(100))  # 682289015
print(numPrimeArrangements(1))  # 1
print(numPrimeArrangements(2))  # 1
