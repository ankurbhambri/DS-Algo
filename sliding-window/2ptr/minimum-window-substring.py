from collections import Counter

# https://leetcode.com/problems/minimum-window-substring/

# Question: Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

class Solution:
    def minWindow(self, s, t):
        
        if not s or not t:
            return ""

        dict_t = Counter(t)

        required = len(dict_t)

        formed = 0
        window_counts = {}
        
        # windows size, left pointer, right pointer
        ans = [float("inf"), None, None]

        l, r = 0, 0

        for r in range(len(s)):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = 1 + window_counts.get(character, 0)

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while formed == required:
                character = s[l]

                # Save the smallest window until now comparing with curr window size and previous window size.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

   
print(Solution().minWindow("ADOBECODEBANC", "ABC"))  # "BANC"
print(Solution().minWindow("a", "a"))  # "a"
print(Solution().minWindow("a", "aa"))  # ""
print(Solution().minWindow("a", ""))  # ""



# Variant of Minimum Window Substring

'''

Given two lists of strings - "sentence" and "words".- find the shortest substring such that "sentence" contains every word in "words".

Example:

    sentence = l'is', 'one', 'ok', 'you', 'the', 'frog', 'ok', 'one', 'the', ' 'you', 'is', "not',. 'frog']
    words = ['is', 'you',. 'frog']

Output: = "you is not frog"

'''

from collections import Counter, defaultdict

def shortest_substring(sentence, words):

    if not sentence or not words:
        return ""

    formed = 0
    required = len(target_count)
    target_count = Counter(words)  # required word frequencies
    window_count = defaultdict(int)

    left = 0
    min_len = float("inf")
    res = (0, 0)  # stores indices of the shortest valid window

    for right in range(len(sentence)):
        word = sentence[right]
        window_count[word] += 1

        # Check if word frequency matches the target requirement
        if word in target_count and window_count[word] == target_count[word]:
            formed += 1

        # Try shrinking the window from the left
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                res = (left, right)

            # Remove the leftmost word
            left_word = sentence[left]
            window_count[left_word] -= 1
            if left_word in target_count and window_count[left_word] < target_count[left_word]:
                formed -= 1

            left += 1

    if min_len == float("inf"):
        return ""

    # Return the result as a string (joined by space)
    return ' '.join(sentence[res[0]:res[1]+1])


print(shortest_substring(['is', 'one', 'ok', 'you', 'the', 'frog', 'ok', 'one', 'the', 'you', 'is', "not", 'frog'], ['is', 'you', 'frog']))  # Output: "you is not frog"

