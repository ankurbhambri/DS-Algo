# Find all permutations of string a in string b

# https://stackoverflow.com/questions/41515081/algorithm-find-all-permutations-of-string-a-in-string-b

from collections import Counter


def find_permutations_in_string(S, B):
    f1 = Counter(S)
    len_s = len(S)
    len_b = len(B)
    res = []

    if f1 == Counter(B[:len_s]):
        res.append(0)

    l, r = 1, len_s

    while r < len_b:

        f2 = Counter(B[l : r + 1])

        if f1 == f2:
            res.append(l)

        l += 1
        r += 1

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
