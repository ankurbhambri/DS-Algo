"""
Idea behind this problem is to moving the sliding window on S2 word and counting the number of characters in that window length,
if that matches with S1 characters frequency then return True

Actual problem - https://leetcode.com/problems/permutation-in-string/

Similar problem - https://leetcode.com/problems/find-all-anagrams-in-a-string/

"""


def checkInclusion(s1, s2):

    c1 = {}
    c2 = {}

    if len(s1) > len(s2):
        return False

    for i in range(len(s1)):
        c1[s1[i]] = c1.get(s1[i], 0) + 1
        c2[s2[i]] = c2.get(s2[i], 0) + 1

    if c1 == c2:
        return True

    l = 0

    for r in range(len(s1), len(s2)):

        c2[s2[r]] = 1 + c2.get(s2[r], 0)

        c2[s2[l]] -= 1

        if c2[s2[l]] == 0:
            del c2[s2[l]]

        l += 1
        if c1 == c2:
            return True

    return False


print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("xy", "eidbaooo"))
