# https://www.geeksforgeeks.org/sieve-of-eratosthenes/


# TC: O(n * log(log(n))) for counting primes, log(log(n)) is the number of times we can divide n by 2, then by 3, then by 5, and so on.
# SC: O(n) for storing the prime numbers

def sieve(n):

    # sabse pehle ek boolean array bana lo jisme initially sabhi numbers ko prime maan lo, except 0 and 1
    prime = [True] * (n + 1)

    # 0 aur 1 ko prime nahi hote
    prime[0] = prime[1] = False

    p = 2

    # uske baad 2 se start karke har number ke multiples ko false karte jao, kyunki wo prime nahi ho sakte
    while p * p <= n:

        # agar current number prime hai, toh uske multiples ko false kar do
        if prime[p]:
            
            # p ke multiples ko false kar do, starting from p*p, kyunki p se chhote multiples already false ho chuke hain
            for multiple in range(p * p, n + 1, p):
                prime[multiple] = False

        # increment p to check for the next number
        p += 1

    # finally, jo numbers abhi bhi prime hain unko return kar do
    return [p for p in range(n + 1) if prime[p]]


print(f"Prime numbers up to {50} are: {sieve(50)}") # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(f"Prime numbers up to {100} are: {sieve(100)}") # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]