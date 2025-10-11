def longestSubstring(s, k):
    left = 0
    max_len = 0
    freq = {}  # character frequency map
    
    for right in range(len(s)):
        # Right character ko add karo
        char = s[right]
        freq[char] = freq.get(char, 0) + 1
        
        # Jab tak koi character k se zyada repeat ho
        while any(count > k for count in freq.values()):
            # Left pointer aage badhao
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        
        # Valid window ka length check karo
        max_len = max(max_len, right - left + 1)
    
    return max_len

print(longestSubstring("aaabb", 3))  # Output: 5
print(longestSubstring("ababbc", 2))  # Output: 4
print(longestSubstring("aabbcc", 1))  # Output: 2
print(longestSubstring("abcde", 1))  # Output: 5
