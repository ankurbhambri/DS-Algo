from collections import Counter

# Same Question permutations of string A in string B or Find All Anagrams of A in String B, only difference is that we need to return the starting index of the anagram.


# https://leetcode.com/problems/permutation-in-string/


def checkInclusion(p, s):

    cs = Counter(s[: len(p)])
    cp = Counter(p)

    if cs == cp:
        return True

    l = 0

    for r in range(len(p), len(s)):

        cs[s[r]] = 1 + cs.get(s[r], 0)
        cs[s[l]] -= 1

        if cs[s[l]] == 0:
            del cs[s[l]]

        l += 1

        if cs == cp:
            return True

    return False


# Same as Above only storing in array the starting index
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


# space efficient approach using sliding window technique

def find_permutations_in_string_space(txt, pat):

    freq_t = {}
    freq_p = Counter(pat)

    wn = len(pat)

    need = wn
    have = 0

    res = []

    for r in range(len(txt)):

        char = txt[r]
        freq_t[char] = 1 + freq_t.get(char, 0)

        # Check if we have the required frequency for this character
        if char in freq_p and freq_t[char] == freq_p[char]:
            have += 1

        # Remove leftmost character from the window when window size exceeds the pattern length
        if r >= wn:

            left_char = txt[r - wn]

            if left_char in freq_p and freq_t[left_char] == freq_p[left_char]:
                have -= 1

            freq_t[left_char] -= 1

            if freq_t[left_char] == 0:
                del freq_t[left_char]

        # If we have all needed characters with the required frequency, it's a valid permutation
        if have == need:
            res.append(r - wn if r - wn > 0 else 0)

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
