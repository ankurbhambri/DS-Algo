# https://leetcode.com/problems/moving-average-from-data-stream/description/

'''
    Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
    Implement the MovingAverage class:

        • MovingAverage(int size) Initializes the object with the size of the window size.
        • double next(int val) Returns the moving average of the last size values of the stream.

    Example 1:
    Input
        ["MovingAverage", "next", "next", "next", "next"]
        [[3], [1], [10], [3], [5]]

    Output
        [null, 1.0, 5.5, 4.66667, 6.0]

    Explanation:
        MovingAverage movingAverage = new MovingAverage (3);
        movingAverage.next (1); // return 1.0 = 1 / 1
        movingAverage.next (10); // return 5.5 = (1 + 10) / 2
        movingAverage.next (3); // return 4.66667 = (1 + 10 + 3) / 3
        movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

    Constraints:
        • 1 <= size <= 1000
        • -105 < val < 105
        • At most 104 calls will be made to next.
'''

class Solution:

    def __init__(self, size):
        self.size = size
        self.window = []
        self.sum = 0

    def next(self, val):

        self.window.append(val)
        self.sum += val

        if len(self.window) > self.size:
            x = self.window.pop(0)
            self.sum -= x

        return self.sum / min(len(self.window), self.size)


print(Solution(3).next(1))
print(Solution(3).next(10))
print(Solution(3).next(3))
print(Solution(3).next(5))


# Variant

'''
    Given a list of integers nums and an integer size, compute the average of elements in a sliding window of exactly size elements.
    Return a list containing the results of these computations using integer division.

    Example 1:

    Input: nums = [5,2,8,14,3]

    Output: [5,8,8]

    Explanation:
        The first window is (5+2+8)/3=5
        The second window is (2+8+14)/3=8
        The third window is (8,14,3)/3=8
'''

def solution(nums, size):

    l = 0
    sm = 0
    res = []

    for r in range(len(nums)):

        if r - l + 1 > size:
            sm -= nums[l]
            l += 1

        sm += nums[r]
        if r - l + 1 == size:
            res.append(sm // size)

    return res


print(solution([5, 2, 8, 14, 3], 3))
print(solution([2, 18, 4, 3], 2))
