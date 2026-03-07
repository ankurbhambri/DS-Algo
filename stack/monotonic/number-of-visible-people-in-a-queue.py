# https://leetcode.com/problems/number-of-visible-people-in-a-queue

class Solution:
    def canSeePersonsCount(self, heights):

        st = []
        res = [0] * len(heights)

        for i in range(len(heights) - 1, -1, -1):

            while st and st[-1] < heights[i]:
                res[i] += 1
                st.pop()

            if st:
                res[i] += 1

            st.append(heights[i])

        res[-1] = 0
        return res


print(Solution().canSeePersonsCount([5, 1, 2, 3, 10]))  # [4, 1, 1, 1, 0]
print(Solution().canSeePersonsCount([10, 6, 8, 5, 11, 9]))  # [3, 1, 2, 1, 1, 0]