# https://www.geeksforgeeks.org/queries-to-print-the-character-that-occurs-the-maximum-number-of-times-in-a-given-range/

"""
    Given a string S of size N and Q queries. Every query consists of L and R ( 0 < = L < = R < N ).
    The task is to print the character that occurs the maximum number of times in the given range.
    If there are multiple characters that occur maximum number of times then print the lexicographically smallest of them.

"""


import string


def solution(s, q):
    n = len(s)
    pref = {}
    for ch in string.ascii_lowercase:
        tmp = [0] * (n + 1)
        for i in range(n):
            if s[i] == ch:
                tmp[i + 1] = 1

        for j in range(n):
            tmp[j + 1] += tmp[j]

        pref[ch] = tmp

    res = []
    for a, b in q:
        ans = [0, s[a]]
        for ch in string.ascii_lowercase:
            freq = pref[ch][b + 1] - pref[ch][a]
            if freq > ans[0]:
                ans = [freq, ch]
        res.append(ans)
    return res


print(solution("abcccabaaabb", [[2, 4], [1, 8]]))
print(solution("zbacd", [[1, 2], [1, 4]]))
