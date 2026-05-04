"""
PROBLEM STATEMENT:

    Aapko 1 se N tak ke numbers ki ek permutation banani hai.
    Aapko ek string s di gayi hai jiski length N-1 hai.
    
    - Agar s[i] ki value '<' hai:
      Permutation ka (i)th element (i+1)th element se chota hona chahiye (P_i < P_{i+1})
      
    - Agar s[i] ki value '>' hai:
      Permutation ka (i)th element (i+1)th element se bada hona chahiye (P_i > P_{i+1})
    
    Question: Aapko aisi total kitni permutations possible hain? (modulo 10^9 + 7)

LOGIC and APPROACH:
    Agar hum seedha permutation banane ki koshish karenge:
    - Complexity: O(N!) ho jayegi, jo bahut zyada hai (N ≤ 3000)
    - Solution: Hum DP ka use karte hain
    
    1. DP STATE:
       Humein yeh track rakhna hoga:
       - Kitne numbers use kar liye hain
       - Aakhri number kya rakha tha
       
       dp[i][j] = Pehle i numbers ko use karke aisi kitni permutations ban sakti hain
                  jinka aakhri number (yaani i-th position par) j hai (relative ranking mein)
    
    2. TRANSITION (The Challenge):
       Jab hum (i+1)-th number add karte hain:
       - Agar s[i] == '<': Naya number pichle number se bada hona chahiye
       - Agar s[i] == '>': Naya number pichle number se chota hona chahiye
       
       Seedha transition: O(N^3) complexity (3000^3 = fail)
       Optimization: Prefix Sums use karte hain taaki range sum O(1) mein mil jaye
"""


import sys

def solve():
    """
    Main function to solve the permutation counting problem
    """
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    MOD = 10**9 + 7

    # Initialize DP table
    # dp[j] = number of permutations of length i ending with relative rank j
    dp = [0] * (n + 1)
    dp[1] = 1

    # Process each position from 2 to n
    for i in range(2, n + 1):

        new_dp = [0] * (n + 1)
        
        # Build prefix sum array for optimization
        pref = [0] * (i + 1)
        for j in range(1, i):
            pref[j] = (pref[j - 1] + dp[j]) % MOD
        
        # Get current constraint from string
        current_sign = s[i - 2]
        
        # Compute new DP values for each possible rank at position i
        for j in range(1, i + 1):
            if current_sign == '<':
                # Constraint: P[i-1] < P[i]
                # So previous rank should be 1 to j-1
                new_dp[j] = pref[j - 1]
            else:
                # Constraint: P[i-1] > P[i]
                # So previous rank should be j to i-1
                new_dp[j] = (pref[i - 1] - pref[j - 1] + MOD) % MOD
        
        # Update DP table for next iteration
        dp = new_dp

    # Sum all permutations and print result
    print(sum(dp) % MOD)


if __name__ == "__main__":
    solve()