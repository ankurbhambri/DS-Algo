# https://leetcode.com/problems/range-addition/


class Solution:
    def getModifiedArray(self, length: int, updates: list[list[int]]) -> list[int]:

        arr = [0] * (length + 1)

        for i, j, v in updates:
            arr[i] += v
            arr[j + 1] -= v

        for i in range(1, length + 1):
            arr[i] += arr[i - 1]

        return arr[0:length]

print(Solution().getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
