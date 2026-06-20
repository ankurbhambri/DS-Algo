# https://leetcode.com/problems/count-of-smaller-numbers-after-self


# TC: O(n log n)
# SC: O(n)
class Solution:
    def countSmaller(self, nums):

        n = len(nums)

        ans = [0] * n

        # (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            merged = []

            i = j = 0

            # right side se kitne smaller elements aa chuke hain
            right_smaller = 0

            while i < len(left) and j < len(right):

                if left[i][0] <= right[j][0]:

                    _, idx = left[i]

                    ans[idx] += right_smaller

                    merged.append(left[i])

                    i += 1

                else:

                    merged.append(right[j])

                    right_smaller += 1

                    j += 1

            while i < len(left):

                _, idx = left[i]

                ans[idx] += right_smaller

                merged.append(left[i])

                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(arr)

        return ans


print(Solution().countSmaller([-1, -1]))
print(Solution().countSmaller([5, 2, 6, 1]))