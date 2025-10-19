# https://leetcode.com/problems/sort-an-array/

# TC: O(n log n)
# SC: O(n)
def merge(left, right):

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])

    result.extend(right[j:])

    return result

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

arr = [38, 27, 43, 3, 9, 82, 10]
print("Recusive Sorted array:", merge_sort(arr))


# Another way

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


arr = [38, 27, 43, 3, 9, 82, 10]
print("In place Sorted array:", sortArray(arr))
