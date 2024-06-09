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
