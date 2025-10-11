# Given a string s, find the length of the longest substring without repeating characters.

def length_of_longest_substring(s: str) -> int:

    l = 0
    max_length = 0
    char_map = {}

    for r in range(len(s)):

        ch = s[r]

        if ch in char_map and char_map[ch] >= l:

            l = char_map[ch] + 1

        char_map[ch] = r

        max_length = max(max_length, r - l + 1)

    return max_length

print(length_of_longest_substring("abcabcbb"))  # Output: 3
print(length_of_longest_substring("bbbbb"))     # Output: 1
print(length_of_longest_substring("pwwkew"))    # Output: 3
print(length_of_longest_substring(""))          # Output: 0