# Given a string s, find the length of the longest substring T that contains at most k distinct characters.

# TC: O(n)
# SC: O(k)

def longest_substring_k_unique(s, k):
    
    l = 0
    freq = {}
    max_len = 0
    
    for r in range(len(s)):

        freq[s[r]] = freq.get(s[r], 0) + 1

        while len(freq) > k:

            freq[s[l]] -= 1

            if freq[s[l]] == 0:
                del freq[s[l]]

            l += 1

        max_len = max(max_len, r - l + 1)
    
    return max_len


print(longest_substring_k_unique("aabacbebebe", 3))  # Output: 7
print(longest_substring_k_unique("aaaa", 1))  # Output: 4
print(longest_substring_k_unique("abc", 2))  # Output: 2
print(longest_substring_k_unique("abc", 3))  # Output: 3
