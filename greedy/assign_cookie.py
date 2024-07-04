# https://leetcode.com/problems/assign-cookies/

# Idea here is to use two pointers to iterate over the two lists and check if the cookie size is greater than the greed factor.


def findContentChildren(g, s):

    g.sort(reverse=True)
    s.sort(reverse=True)

    i = j = 0

    while i < len(g) and j < len(s):

        if g[i] <= s[j]:
            j += 1  # if satisfied increment the child pointer

        i += 1  # increment cookie pointer

    return j


g = [1, 2, 3]
s = [1, 1]
print(findContentChildren(g, s))
