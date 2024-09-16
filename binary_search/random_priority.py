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


class Solution:
    def __init__(self, arr):
        self.arr = arr
        self.state_arr = []
        self.c = random.randint(0, max(self.arr))

    def state(self):
        val = 0
        for i in range(len(self.arr)):
            self.state_arr.append(val + self.arr[i])
            val = i + self.arr[i]
        return self.state_arr

    def serve(self):
        l, r = 0, len(self.state_arr)

        print(self.c, self.state_arr)

        while l < r:
            mid = (l + r) // 2

            if self.c <= self.state_arr[mid]:
                return mid

            elif self.c > self.state_arr[mid]:
                l = mid + 1

            else:
                r = mid

        return -1


obj = Solution([1, 7, 2, 500])
print(obj.state())

print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
print(obj.serve())
