"""
    Given an array of integers arr and an integer k, split the array into k contiguous subarrays. 
    The size of each subarray should be as equal as possible, meaning no two subarrays should differ in size by more than one element. 
    If there are not enough elements to fill all k subarrays, the remaining subarrays should be empty.

    Constraints:
    0 <= len(arr) <= 1000
    0 <= arr[i] <= 1000
    1 <= k <= 50
"""


def solution(arr, k):

    n = len(arr)
    parts = n // k
    rem = n % k
    res = []
    l = 0
    for i in range(k):
        custom_parts = parts + (1 if i < rem else 0)
        tmp = []
        if l <= n - 1:
            for _ in range(custom_parts):
                tmp.append(arr[l])
                l += 1
        res.append(tmp)
    return res


print(solution([1, 2, 3], 5))  # [[1], [2], [3], [], []]
print(
    solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
)  # [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
