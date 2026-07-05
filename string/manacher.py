# Manacher's alogorithm is used to find the longest palindromic substring in linear time.

# TC: O(n)
# SC: O(n)
def manacher(s: str) -> str:

    # Step 1: String ko transform karo (Even/Odd ka jhanjhat khatam)
    # 'aba' ban jayega '^#a#b#a#$'
    # '^' aur '$' isliye lagaye hain taaki boundary check karte waqt loop break ho jaye
    T = '#'.join(f'^{s}$')
    
    n = len(T)
    P = [0] * n  # Yeh har index ka palindrome radius store karega
    C = 0        # Current Center
    R = 0        # Current Right Boundary
    
    for i in range(1, n - 1):

        # i' nikal lo (Mirror of i around Center C)
        i_mirror = 2 * C - i
        
        # Agar i humari boundary R ke andar hai, toh mirror ka data use karo
        if R > i:
            P[i] = min(R - i, P[i_mirror])
        else:
            P[i] = 0
            
        # Ab iske aage expand karke check karo agar kuch naya milta hai toh
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # Agar naya palindrome humari purani boundary R ko cross kar gaya,
        # toh Center aur Right boundary ko update kar do
        if i + P[i] > R:
            C = i
            R = i + P[i]
            
    # Ab P array mein se maximum value dhundho
    max_len = max(P)
    center_index = P.index(max_len)
    
    # Original string mein convert karne ka hisaab
    start = (center_index - max_len) // 2
    return s[start : start + max_len]


print(manacher("babad"))  # Output: "bab" or "aba"
print(manacher("cbbd"))   # Output: "bb"