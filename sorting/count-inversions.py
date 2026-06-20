# https://www.geeksforgeeks.org/problems/inversion-of-array-1587115620/1

# Will be using merge sort to count inversions in an array.

class Solution:
    def inversionCount(self, arr):

        n = len(arr)

        self.inverse_count = 0

        def sortArray(nums):

            if len(nums) <= 1:
                return nums

            m = len(nums) // 2

            left = nums[:m]
            right = nums[m:]

            sortArray(left)

            sortArray(right)

            i = j = k = 0

            while i < len(left) and j < len(right):

                if left[i] > right[j]:    

                    nums[k] = right[j]

                    # agar left ki value badi h to uske baad ke saare elements bhi badi honge, to unki count bhi add karni padegi.
                    # kyuki left aur right dono sorted hain, to agar left[i] > right[j] hai, to left ke baad ke saare elements bhi right[j] se bade honge.
                    # islite len(left) - i or (i ... mid) tak ke saare elements right[j] se bade honge, to unka count bhi add karni padegi.

                    self.inverse_count += len(left) - i

                    j += 1

                else:
                    nums[k] = left[i]

                    i += 1

                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

            return nums

        sortArray(arr)

        return self.inverse_count

print(Solution().inversionCount([2, 4, 1, 3, 5])) # Output: 3
print(Solution().inversionCount([1, 20, 6, 4, 5])) # Output: 5