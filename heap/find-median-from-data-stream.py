# https://leetcode.com/problems/find-median-from-data-stream/

from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.small = []   # max heap (store negatives)
        self.large = []   # min heap

    def addNum(self, num: int) -> None:
        # [-3,-2,-1]
        heappush(self.small, -num)
        # [4, 5, 6]
        heappush(self.large, -heappop(self.small))

        if len(self.large) > len(self.small):
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        # odd case
        if len(self.small) > len(self.large):
            return -self.small[0]
        # even case
        return (-self.small[0] + self.large[0]) / 2