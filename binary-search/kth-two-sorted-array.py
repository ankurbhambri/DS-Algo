# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
# https://leetcode.com/discuss/interview-question/351782/Google-or-Phone-Screen-or-Kth-Largest-Element-of-Two-Sorted-Arrays

'''

Given two sorted arrays of sizes m and n respectively, the task is to find the element that would be at the k-th either smallest or largest element in the combined sorted array formed by merging the two arrays.

Approach 1: Naive (Simple Merge) — Brute Force (Idea: Merge the two arrays like in merge sort and TC will be O(m + n)).

Approach 2: Binary Search (O(log(min(n, m))) time) — Efficient (Idea: Use binary search to find the k-th smallest element).

'''


# Kth Smallest Element in Two Sorted Arrays

# TC: O(log(min(m,n)))
# SC: O(1)

'''

A:  | ... Aleft | Aright ... |
B:  | ... Bleft | Bright ... |

At the partition point, Aleft <= Bright AND Bleft <= Aright

This condition ensures all elements in the left partition are ≤ all elements in the right partition, so we correctly found the k-th element.

If any of these conditions fail, we move the partition in A either left or right using binary search.



'''

def find_kth_smallest(A, B, k):

    # Ensure A is the smaller array

    if len(A) > len(B):
        return find_kth_smallest(B, A, k)
    
    m, n = len(A), len(B)
    
    # Set the binary search range
    low = max(0, k - n) # Minimum elements we can take from A atleast. If we take n elements from B, we can take at most k - n elements from A.
    high = min(k, m) # Maximum elements we can take from A at most. We have to take alteast k elements, so we can take at most k elements from A if m >= k.
    
    while low <= high:

        i = (low + high) // 2 # Number of elements we pick from array A for the left side of partition

        j = k - i # Number of elements we pick from array B for the left side of partition.

        # Last element in A's left partition.
        Aleft = A[i - 1] if i > 0 else float('-inf')

        # First element in A's right partition.
        Aright = A[i] if i < m else float('inf')

        # Last element in B's left partition.
        Bleft = B[j - 1] if j > 0 else float('-inf')

        # First element in B's right partition.
        Bright = B[j] if j < n else float('inf')
        
        # Check valid partition, if Aleft <= Bright and Bleft <= Aright, then we have found the k-th smallest element.
        if Aleft <= Bright and Bleft <= Aright:
            # max(Aleft, Bleft) is the boundary element that separates the first k smallest elements from the rest. Hence, it’s the exact k-th smallest element.
            return max(Aleft, Bleft)

        elif Aleft > Bright:
            high = i - 1
        else:
            low = i + 1
    
    return -1  # Should never reach here if input k is valid


print(find_kth_smallest([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # Output: 6
print(find_kth_smallest([-2, -1, 3, 5, 6, 8], [0, 1, 2, 5, 9], 4))  # Output: 1

# Kth Largest Element in Two Sorted Arrays

# Kth largest element from the end of the combined, sorted array (in ascending order)

# TC: O(log(min(m,n)))
# SC: O(1)

# Idea: To find the k-th largest element, we can find the (total - k + 1)-th smallest element in the combined sorted array.

def find_kth_largest(arr1, arr2, k):

    m, n = len(arr1), len(arr2)

    total = m + n

    k_smallest = total - k + 1 # example: total = 11 and 11 - 4 + 1 = 8th element from the start is the 4th largest element from the end.

    return find_kth_smallest(arr1, arr2, k_smallest)

print(find_kth_largest([2, 3, 6, 7, 9], [1, 4, 8, 10], 5))  # Output: 6
print(find_kth_largest([-2, -1, 3, 5, 6, 8], [0, 1, 2, 5, 9], 4))  # Output: 5
print(find_kth_largest([100, 112, 256, 349, 770], [72, 86, 113, 119, 265, 445, 892], 7))  # Output: 256
