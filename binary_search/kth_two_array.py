# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
# https://leetcode.com/discuss/interview-question/351782/Google-or-Phone-Screen-or-Kth-Largest-Element-of-Two-Sorted-Arrays

'''

Given two sorted arrays of sizes m and n respectively, the task is to find the element that would be at the k-th position in the final sorted array formed by merging these two arrays

Examples: 

Input: a[] = [2, 3, 6, 7, 9], b[] = [1, 4, 8, 10], k = 5
Output: 6
Explanation: The final sorted array is [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element is 6.


Input: a[] = [100, 112, 256, 349, 770], b[] = [72, 86, 113, 119, 265, 445, 892], k = 7
Output: 256
Explanation: The final sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892]. The 7th element is 256.

'''

# TC - O(log(min(n, m)) and O(1) Space

def kthLargest(arr1, arr2, m, n, k):
    if m > n:
        return kthLargest(arr2, arr1, n, m, k)  # Ensure arr1 is the smaller array

    low, high = max(0, k - n), min(k, m)

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1  # Remaining elements taken from arr2

        l1 = arr1[cut1 - 1] if cut1 > 0 else float('-inf')
        l2 = arr2[cut2 - 1] if cut2 > 0 else float('-inf')
        r1 = arr1[cut1] if cut1 < m else float('inf')
        r2 = arr2[cut2] if cut2 < n else float('inf')

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)  # Found the k-th element
        elif l1 > r2:
            high = cut1 - 1  # Move left
        else:
            low = cut1 + 1  # Move right

    return -1  # Should never reach here


print(kthLargest([2, 3, 6, 7, 9], [1, 4, 8, 10], 5)) # 6
print(kthLargest([-2, -1, 3, 5, 6, 8], [0, 1, 2, 5, 9], 4)) # 5
print(kthLargest([1, 2, 3, 4, 5], [5], 3)) # 4
