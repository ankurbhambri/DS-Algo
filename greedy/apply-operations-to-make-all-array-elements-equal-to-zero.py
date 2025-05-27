# https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/description/

class Solution:
    def checkArray(self, A, k: int) -> bool:
        cur = 0
        for i, a in enumerate(A):
            if cur > a:
                return False
            A[i] -= cur
            cur = a
            if i >= k - 1:
                cur -= A[i - k + 1]
        return cur == 0
    

print(Solution().checkArray([2,2,3,1,1,0], 3))  # Output: True
print(Solution().checkArray([3, 7, 1, 6], 2))  # Output: False
