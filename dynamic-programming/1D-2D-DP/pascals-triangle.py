# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int):
        res = []
        for i in range(1, numRows + 1):
            if i == 1:
                res.append([i])
            else:
                old = [0] + res[-1] + [0]
                nn = []
                for i in range(len(old) - 1):
                    nn.append(old[i] + old[i + 1])
                res.append(nn)
        return res


print(Solution().generate(2))  # [[1], [1, 1]]
print(Solution().generate(5))  # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]