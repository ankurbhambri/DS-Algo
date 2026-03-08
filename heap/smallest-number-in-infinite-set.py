# https://leetcode.com/problems/smallest-number-in-infinite-set/

import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.curr = 1                  # next smallest number from infinite stream
        self.heap = []                 # min-heap for added back numbers
        self.present = set()           # to avoid duplicates in heap

    def popSmallest(self) -> int:
        # If we have any added-back smaller number, use that
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.present.remove(smallest)
            return smallest

        # Otherwise return from infinite natural numbers
        ans = self.curr
        self.curr += 1
        return ans

    def addBack(self, num: int) -> None:
        # Only add back if:
        # 1) num is already popped (num < curr)
        # 2) not already present in heap
        if num < self.curr and num not in self.present:
            heapq.heappush(self.heap, num)
            self.present.add(num)
