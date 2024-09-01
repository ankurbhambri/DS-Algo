# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/


def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries it as true.
    # A value in prime[i] will be false if i is Not a prime.
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Updating all multiples of p to false
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Collecting all prime numbers
    return [p for p in range(2, n + 1) if prime[p]]


n = 100
print(f"Prime numbers up to {n} are: {sieve_of_eratosthenes(n)}")
