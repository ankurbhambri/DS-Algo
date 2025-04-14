# https://leetcode.com/problems/last-stone-weight/

import heapq

def lastStoneWeight(stones):

    lst = [-i for i in stones]
    heapq.heapify(lst)

    while len(lst) > 1:

        a = -heapq.heappop(lst)
        b = -heapq.heappop(lst)

        heapq.heappush(lst, -abs(b - a))
        
    return -lst[0]


print(lastStoneWeight([2,7,4,1,8,1]))  # Output: 1
print(lastStoneWeight([1]))  # Output: 1
print(lastStoneWeight([1,3]))  # Output: 2
print(lastStoneWeight([3,7,2,4,1]))  # Output: 1
print(lastStoneWeight([2,6,3,9,9,3,8]))  # Output: 0


# https://leetcode.com/problems/last-stone-weight-ii/