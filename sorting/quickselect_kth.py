'''
QuickSelect (Hoare's Selection Algorithm) is an efficient algorithm used to find the k-th smallest (or largest) element in an unsorted list. 
It's closely related to QuickSort, but instead of sorting the entire list, it focuses on partitioning to find the desired element, giving it better average performance for selection.
'''

def quickselect(arr, k):
    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    left, right = 0, len(arr) - 1
    while left <= right:
        pivot_index = partition(left, right)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

arr = [7, 10, 4, 3, 20, 15]
k = 2  # 3rd smallest (0-based index)
print(quickselect(arr, k))  # Output: 7
