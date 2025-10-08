"""
    https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

    Given a string s, find the length of the longest substring T that contains at most k distinct characters.

    Note - same as above replace static value 2 with k only

    Similar question - https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/ replace k with 2
"""

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        n = len(s)
        if n < k:
            return 0
        
        # Count unique characters
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        max_unique = len(char_count)
        
        max_length = 0
        
        # Try for each possible unique count (1 to max_unique)
        for curr_unique in range(1, max_unique + 1):
            # Reset window variables
            char_freq = {}
            window_unique = 0
            window_valid = 0
            left = 0
            
            # Sliding window
            for right in range(n):
                # Add right character to window
                char = s[right]
                char_freq[char] = char_freq.get(char, 0) + 1
                
                # If new character, increase unique count
                if char_freq[char] == 1:
                    window_unique += 1
                # If count becomes k, increase valid count
                if char_freq[char] == k:
                    window_valid += 1
                    
                # Shrink window if unique count exceeds
                while window_unique > curr_unique:
                    left_char = s[left]
                    # If count becomes k-1, decrease valid count
                    if char_freq[left_char] == k:
                        window_valid -= 1
                    char_freq[left_char] -= 1
                    # If character is removed, decrease unique count
                    if char_freq[left_char] == 0:
                        window_unique -= 1
                    left += 1
                
                # Check if window is valid
                if window_unique == curr_unique and window_unique == window_valid:
                    max_length = max(max_length, right - left + 1)
        
        return max_length


print(Solution.longestSubstring("aaabb", 3))  # Output: 3 ("aaa")
print(Solution.longestSubstring("ababbc", 2))  # Output: 5 ("ababb")
print(Solution.longestSubstring("aabbcc", 1))  # Output: 2 ("aa" or "bb" or "cc")
print(Solution.longestSubstring("abcde", 1))  # Output: 1 ("a" or "b" or "c" or "d" or "e")
print(Solution.longestSubstring("aabbcc", 2))  # Output: 6 ("aabbcc")
print(Solution.longestSubstring("aabbccdd", 3))  # Output: 8 ("aabbccdd")
