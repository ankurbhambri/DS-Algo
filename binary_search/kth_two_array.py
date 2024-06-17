# https://www.geeksforgeeks.org/k-th-element-two-sorted-arrays/
# https://leetcode.com/discuss/interview-question/351782/Google-or-Phone-Screen-or-Kth-Largest-Element-of-Two-Sorted-Arrays


def kthLargest(nums1, nums2, k):

    N1, N2 = len(nums1), len(nums2)

    if N1 + N2 < k:
        return float("inf")

    i = N1 - 1
    j = N2 - 1
    current = float("inf")

    while k > 0 and i >= 0 and j >= 0:
        # print(i, j, nums1[i], nums2[j])
        if nums1[i] > nums2[j]:
            current = nums1[i]
            i -= 1
        else:
            current = nums2[j]
            j -= 1
        # print(current, k)
        k -= 1
    return current if k == 0 else (nums2[j - k + 1] if i < 0 else nums1[i - k + 1])


print(kthLargest([-2, -1, 3, 5, 6, 8], [0, 1, 2, 5, 9], 4))
print("-" * 20)
print(kthLargest([1, 2, 3, 4, 5], [5], 3))
