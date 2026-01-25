# https://www.geeksforgeeks.org/sieve-of-eratosthenes/


# Way to check number is prime or not
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Here, we are simply finding all prime numbers up to n using Sieve of Eratosthenes
def sieve_of_eratosthenes(n):

    # A value in prime[i] will be false if i is Not a prime.
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # Collecting all prime numbers
    return [p for p in range(2, n + 1) if is_prime[p]]


print(is_prime(11))  # True
print(is_prime(15))  # False
print(f"Prime numbers up to {50} are: {sieve_of_eratosthenes(50)}") # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(f"Prime numbers up to {100} are: {sieve_of_eratosthenes(100)}") # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]