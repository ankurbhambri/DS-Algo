from collections import Counter


def intersect(nums1, nums2):
    c = Counter(nums1)
    res = []
    for i in nums2:
        if i in c and c[i] > 0:
            res.append(i)
            c[i] -= 1
    return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # [2,2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))  # [4,9] or [9,4] both correct
