# https://leetcode.com/problems/wiggle-sort/

def wiggleSort(nums):

    # Idea here is, in even positions, we want the smaller number and in odd positions, we want the larger number
    # So we sort the array and then swap the elements in the even and odd positions based on the next element and it will make sure that the previous is in place.
 
    for i in range(1, len(nums)):
        # Odd index: want nums[i] >= nums[i-1]
        if i % 2 == 1 and nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
        # Even index: want nums[i] <= nums[i-1]
        elif i % 2 == 0 and nums[i] > nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums # no need to return, as we are modifying the original array


# https://leetcode.com/problems/wiggle-sort-ii/

def wiggleSort_II(nums):
    n = len(nums)
    sorted_nums = sorted(nums)
    
    # Place larger elements at odd indices (1,3,5...) in reverse order
    j = n - 1
    for i in range(1, n, 2):
        nums[i] = sorted_nums[j]
        j -= 1
    
    # Place smaller elements at even indices (0,2,4...) in reverse order
    for i in range(0, n, 2):
        nums[i] = sorted_nums[j]
        j -= 1

    return nums # no need to return, as we are modifying the original array


print(wiggleSort([1, 5, 1, 1, 6, 4]))  # Output: [1, 4, 1, 5, 1, 6]
print(wiggleSort_II([1, 3, 2, 2, 3, 1]))  # Output: [1, 3, 1, 3, 2, 2]
