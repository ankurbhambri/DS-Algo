import heapq
from collections import Counter


"""
Idea behind this logic is to keep the frequency of every character in heap and the oen by one will pop the max frequencey character and add it to the result string.
But after removal will kept it in the prev and next iteration will add it back, this way will ensure the adjacent characters are not same.
"""


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


print(reorganizeString("aab"))
print(reorganizeString("aaab"))
print(reorganizeString("baaba"))
print(reorganizeString("vvvlo"))
