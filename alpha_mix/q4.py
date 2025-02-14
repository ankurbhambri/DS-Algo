# Given an array of integers, and an integer N, find the length of the longest “N-stable” continuous subarray.
# An array is defined to be “N-stable” when the pair-wise difference between any two elements in the array is smaller or equal to N.
# A subarray of a 0-indexed integer array is a contiguous non-empty sequence of elements within an array.
# For instance, for array [ 4, 2, 3, 6, 2, 2, 3, 2, 7 ], and N = 1
# The return value should be 4, since the longest 1-stable subarray is [ 2, 2, 3, 2 ].

from collections import deque


def func(arr, N):

    if not arr:
        return 0

    left = 0

    min_deque, max_deque = deque(), deque()

    res = 0

    for right in range(len(arr)):

        print("right", right)

        while min_deque and arr[min_deque[-1]] > arr[right]:
            min_deque.pop()
        min_deque.append(right)
        print("min_deque", min_deque)

        while max_deque and arr[max_deque[-1]] < arr[right]:
            max_deque.pop()
        max_deque.append(right)

        print("max_deque", max_deque)

        # processing
        while arr[max_deque[0]] - arr[min_deque[0]] > N:
            left += 1  # 1, 2
            print("left", left)
            while min_deque and min_deque[0] < left:
                min_deque.popleft()

                print("min_deque", min_deque)

            while max_deque and max_deque[0] < left:
                max_deque.popleft()

                print("max_deque", max_deque)

        res = max(res, right - left + 1)

        print("res", res)

    return res


print(func([4, 2, 3, 6, 2, 2, 3, 2, 7], 1))
