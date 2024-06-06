from collections import Counter

"""
Idea behind this problem is to moving the sliding window on S2 word and counting the number of characters in that window length,
if that matches with S1 characters frequency then return True

"""


def checkInclusion(s1, s2):

    freqs1 = Counter(s1)
    freqs2 = Counter()

    winLen = len(s1)

    # checking whether starting length is equal then return from here.
    if freqs1 == Counter(s2[: winLen + 1]):
        return True

    i, j = 0, 0

    while j <= len(s2) - 1:

        freqs2[s2[j]] += 1

        if j - i + 1 == winLen:
            if freqs2 != freqs1:

                freqs2[s2[i]] -= 1
                i += 1

            else:
                return True

        j += 1

    return False


print(checkInclusion("ab", "eidbaooo"))
