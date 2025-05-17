# https://leetcode.com/problems/sort-colors

def dutch_national_flag_sort(nums):

    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


print(dutch_national_flag_sort([2, 0, 2, 1, 1, 0]))  # Output: [0, 0, 1, 1, 2, 2]
print(dutch_national_flag_sort([2, 0, 1]))  # Output: [0, 1, 2]
print(dutch_national_flag_sort([0]))  # Output: [0]
print(dutch_national_flag_sort([1]))  # Output: [1]
print(dutch_national_flag_sort([2]))  # Output: [2]
print(dutch_national_flag_sort([0, 1, 2]))  # Output: [0, 1, 2]
