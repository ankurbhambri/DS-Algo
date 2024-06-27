# Find all permutations of string a in string b or Find All Anagrams in a String


# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/


def find_permutations_in_string(S, B):

    cs = {}
    cb = {}

    if len(S) > len(B):
        return []

    for i in range(len(S)):
        cs[S[i]] = 1 + cs.get(S[i], 0)
        cb[B[i]] = 1 + cb.get(B[i], 0)

    res = [0] if cs == cb else []

    l = 0
    for r in range(len(S), len(B)):

        cb[B[r]] = 1 + cb.get(B[r], 0)
        cb[B[l]] -= 1

        if cb[B[l]] == 0:
            del cb[B[l]]

        l += 1

        if cs == cb:
            res.append(l)

    return res


# space efficinet


def find_permutations_in_string_space(txt, pat):
    freq_p = {}
    freq_t = {}
    wn = len(pat)

    # Create frequency table for pattern and initialize variables
    for c in pat:
        freq_p[c] = 1 + freq_p.get(c, 0)

    need = len(freq_p)
    have = 0

    res = []

    for i in range(len(txt)):
        # Add current character to the window
        char = txt[i]
        freq_t[char] = 1 + freq_t.get(char, 0)

        # Check if we have the required frequency for this character
        if char in freq_p and freq_t[char] == freq_p[char]:
            have += 1

        # Remove leftmost character from the window when window size exceeds the pattern length
        if i >= wn:
            left_char = txt[i - wn]
            if left_char in freq_p and freq_t[left_char] == freq_p[left_char]:
                have -= 1
            freq_t[left_char] -= 1
            if freq_t[left_char] == 0:
                del freq_t[left_char]

        # If we have all needed characters with the required frequency, it's a valid permutation
        if have == need:
            if i - wn < 0:
                res.append(0)
            else:
                res.append(i - wn)

    return res


S = "abc"
B = "cbabcacab"
result = find_permutations_in_string(S, B)
print(result)  # Output: [0, 2, 3, 6]

S = "abc"
B = "defghicba"
result = find_permutations_in_string(S, B)
print(result)  # Output: [6]

S = "a"
B = "aaaaa"
result = find_permutations_in_string(S, B)
print(result)  # Output: [0, 1, 2, 3, 4]

S = "abc"
B = "aabbcc"
result = find_permutations_in_string(S, B)
print(result)  # Output: []
