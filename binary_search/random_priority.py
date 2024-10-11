import random

"""

Given an array of positive integers, where each value within the array represents a multiple times weight of the corresponding index, 
implement a structure which can be invoked to pick a random index within that array according to in proportion to its weight.

array [1, 7, 2]

With N 10 times called:
- O index retuned 1 time
- 1 index retuned 7 times
- 2 index retuned 2 times

"""

# Similar question - https://leetcode.com/problems/random-pick-with-weight/


class Solution:

    def __init__(self, w):
        self.arr = []
        val = 0
        for weight in w:
            val += weight
            self.arr.append(val)

    def pickIndex(self):

        # Use 1 to total sum, not length
        t = random.randint(1, self.arr[-1])
        l, r = 0, len(self.arr)

        while l < r:
            m = (l + r) // 2
            if t > self.arr[m]:
                l = m + 1
            else:
                r = m

        return l


obj = Solution([1, 7, 2])

# Test case
for _ in range(10):
    print(obj.pickIndex())
