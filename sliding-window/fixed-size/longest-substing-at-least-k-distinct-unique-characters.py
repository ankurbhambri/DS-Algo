# Given a string s, find the length of the longest substring T that contains at least k distinct characters.

def longest_substring_k_unique(s, k):

    """
    Longest substring with at least K unique characters
    Time: O(n), Space: O(k)
    """

    if k == 0:
        return len(s), s
    
    l = 0
    max_len = 0
    char_freq = {}
    max_substring = ""
    
    for r in range(len(s)):

        char_freq[s[r]] = char_freq.get(s[r], 0) + 1
        

        while len(char_freq) >= k:

            current_len = r - l + 1

            if current_len > max_len:
                max_len = current_len
                max_substring = s[l: r + 1]

            # l ko aage badhane ki try karo (greedy approach)
            # Lekin unique chars >= k maintain karo
            char_freq[s[l]] -= 1
            if char_freq[s[l]] == 0:
                del char_freq[s[l]]

            l += 1
    
    return max_len, max_substring

print(longest_substring_k_unique("aabacbebebe", 3))  # Output: (5, "aabac")
print(longest_substring_k_unique("aaaa", 1))  # Output: (1, "a")
print(longest_substring_k_unique("abc", 2))  # Output: (2, "ab" or "bc" or "ac")
print(longest_substring_k_unique("abc", 3))  # Output: (3, "abc")


# Variation of above problem - exactly  k unique characters

def longest_substring_exactly_k_unique(s, k):
    """
    Longest substring with exactly K unique characters
    Time: O(n), Space: O(k)
    """
    max_len = 0
    max_substring = ""
    l = 0
    char_freq = {}
    
    for r in range(len(s)):
        # r character add karo
        char_freq[s[r]] = char_freq.get(s[r], 0) + 1
        
        # Agar unique chars > k ho gaye, l ko move karo
        while len(char_freq) > k:
            char_freq[s[l]] -= 1
            if char_freq[s[l]] == 0:
                del char_freq[s[l]]
            l += 1
        
        # Agar exactly k unique chars hain
        if len(char_freq) == k:
            current_len = r - l + 1
            if current_len > max_len:
                max_len = current_len
                max_substring = s[l: r + 1]
    
    return max_len, max_substring

print(longest_substring_exactly_k_unique("aabacbebebe", 3))  # Output: (7, "cbebebe")
print(longest_substring_exactly_k_unique("aaaa", 1))  # Output: (4, "aaaa")

# Variation of above problem - count substrings with at least k unique characters

def at_least_k_unique(s, k):

    n = len(s)
    if k == 0:
        # all substrings are valid
        return n * (n + 1) // 2
    
    count = 0
    l = 0
    char_freq = {}
    
    for r in range(n):

        # r char add karo
        char_freq[s[r]] = char_freq.get(s[r], 0) + 1

        # at least k unique chars
        while len(char_freq) >= k:

            # Current position se sab valid substrings count
            count += n - r
            
            # l char remove
            char_freq[s[l]] -= 1
            if char_freq[s[l]] == 0:
                del char_freq[s[l]]

            l += 1

    return count

print(at_least_k_unique("abaaca", 2)) # Output: 15


# Variation of above problem - count substrings with exactly k unique characters

def count_exactly_k_unique(s, k):
    """
    Exactly k unique characters wale substrings
    """
    def at_least(k):
        count = 0
        l = 0
        char_freq = {}
        
        for r in range(len(s)):

            char_freq[s[r]] = char_freq.get(s[r], 0) + 1
            
            while len(char_freq) >= k:
                count += len(s) - r
                char_freq[s[l]] -= 1
                if char_freq[s[l]] == 0:
                    del char_freq[s[l]]
                l += 1
        
        return count
    
    # Exactly K = (At least K) - (At least K+1)
    return at_least(k) - at_least(k + 1)


print(count_exactly_k_unique("abaaca", 2))  # 10
print(count_exactly_k_unique("abc", 2))     # 2
print(count_exactly_k_unique("aa", 1))      # 3
print(count_exactly_k_unique("aabbcc", 2))  # 8
print(count_exactly_k_unique("aabbcc", 3))  # 4
