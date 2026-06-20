# https://leetcode.com/problems/sort-an-array/

# TC: O(n log n)
# SC: O(n)
def sortArray(nums):

    if len(nums) <= 1:
        return nums

    m = len(nums) // 2

    l = nums[:m]
    r = nums[m:]

    sortArray(l)
    sortArray(r)

    i = j = k = 0

    while i < len(l) and j < len(r):

        if l[i] > r[j]:    
            nums[k] = r[j]
            j += 1

        else:
            nums[k] = l[i]
            i += 1

        k += 1

    while i < len(l):
        nums[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        nums[k] = r[j]
        j += 1
        k += 1

    return nums


print(sortArray([5, 2, 3, 1]))
print(sortArray([38, 27, 43, 3, 9, 82, 10]))