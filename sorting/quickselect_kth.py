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


'''
Random pivot selection adds an element of unpredictability that protects the algorithm from worst-case inputs (like sorted arrays), making average-case linear time O(n) more likely in practice.
While choosing random pivot, we can:
- Avoid deterministic bad splits
- Ensure better average-case balance
Random pivot is equally likely to be any element, so on average, it will land somewhere near the middle.
That means the partitions will usually be more balanced, e.g. around 50/50 split → leading to O(n) time on average.
'''

import random

def quickselect(arr, k):
    """
    Returns the k-th smallest element (0-based index).
    For example, k=0 returns the smallest element.
    """

    def partition(left, right, pivot_index):
        pivot_value = arr[pivot_index]
        # Move pivot to the end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        store_index = left

        # Move all smaller elements to the left
        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        # Move pivot to its final place
        arr[right], arr[store_index] = arr[store_index], arr[right]
        return store_index

    left, right = 0, len(arr) - 1

    while left <= right:
        # 🧠 Pick random pivot
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

