# https://leetcode.com/problems/reorganize-string/

from collections import Counter
import heapq


def reorganizeString(s):

    c = Counter(s)
    hm = [(-v, k) for k, v in c.items()]

    heapq.heapify(hm)

    prev = None
    res = ""

    while hm or prev:

        if prev and not hm:
            return ""

        cnt, ch = heapq.heappop(hm)
        res += ch
        cnt += 1

        if prev:
            heapq.heappush(hm, prev)
            prev = None

        if cnt != 0:
            prev = (cnt, ch)

    return res


print(reorganizeString("aab"))  # "aba"
print(reorganizeString("aaab"))  # ""
print(reorganizeString("aaabb"))  # "ababa"
print(reorganizeString("vvvlo"))  # "vlvov"
print(reorganizeString("aaab"))  # ""
